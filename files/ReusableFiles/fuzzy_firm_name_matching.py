"""
Fuzzy Firm Name Matching
========================

Matches firm names across two datasets using a multi-stage strategy:
  1. Standardize names (capitalization, punctuation, business-type suffixes).
  2. Exact match on cleaned names.
  3. Subsidiary match: link unmatched names to parent firms via a subsidiary
     crosswalk (e.g., WRDS Subsidiary data).
  4. Fuzzy match on remaining unmatched names using Levenshtein distance,
     then manually inspect candidates above a similarity threshold.

Originally used to match BoardEx (board-of-directors database) to GS1 company
prefixes (which map to UPC barcodes in Nielsen/Kilts retail scanner data).
Adapt the data-loading sections to your own datasets.

Requirements: pandas, python-Levenshtein (or rapidfuzz)
"""

import re
import pandas as pd
import Levenshtein


# ---------------------------------------------------------------------------
# Stage 0: Name standardization
# ---------------------------------------------------------------------------

def clean_name(name: str) -> str:
    """Capitalize, strip punctuation, and normalize common character variants."""
    name = name.upper()
    for old, new in [("É", "E"), ("é", "E"), ("\x00", ""), (".", ""),
                     ("/", ""), (",", ""), ("'", ""), ("-", " "),
                     ("&AMP;", "&"), ("AND;", "&")]:
        name = name.replace(old, new)
    return name.strip()


# Suffixes are checked longest-first so that "FOODS INTERNATIONAL INC" is
# removed before "INC" alone.  Add or remove entries as needed.
_SUFFIXES = [
    " FOODS INTERNATIONAL INC", " WORLD TRADING CO INC",
    " (PRIVATE) LIMITED", " UNITED STATES INC", " NORTH AMERICA INC",
    " INTERNATIONAL LTD", " INTERNATIONAL INC", " INTERNATIONAL BV",
    " ENTERPRISES INC", " FOODS COMPANY", " FOOD COMPANY",
    " FOODS CO LLC", " INCORPORATED", " HOLDINGS INC",
    " COMPANY LTD", " COMPANY LLC", " COMPANY INC",
    " CORPORATION", " AMERICA INC", " FOODS GROUP", " FOOD GROUP",
    " FOODS CORP", " GROUP INC", " FOODS INC", " FOOD CORP",
    " (PTY) LTD", " FOOD INC", " FOODS CO", " BOTTLING",
    " FOOD CO", " PVT LTD", " PTE LTD", " USA INC",
    " COMPANY", " CO LTD", " CO LLC", " CENTER", " CO INC",
    " US INC", " (THE)", " MEATS", " (USA)", " BTTLG",
    " CORP", " MEAT", " INC", " LLC", " LLP", " CTR", " LTD",
    " USA", " AG", " CO", " LP", " SE", " LC",
]

_PREFIXES = ["THE "]


def strip_business_type(name: str) -> str:
    """Remove common business-type suffixes and prefixes (e.g., INC, LLC)."""
    for suffix in _SUFFIXES:
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break                       # remove at most one suffix
    for prefix in _PREFIXES:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    return name


def standardize(name: str) -> str:
    """Full pipeline: clean characters, then strip business type."""
    return strip_business_type(clean_name(name))


# ---------------------------------------------------------------------------
# Stage 0b: Parse "formerly known as" and similar name variants
# ---------------------------------------------------------------------------

_VARIANT_PATTERNS = [
    r"(.*)\s+\(DE-LISTED\b.*?\)",
    r"(.*)\s+\(LISTED\b.*?\)",
    r"(.*)\s+\(CEASED TRADING\b.*?\)",
]

_ALIAS_PATTERNS = [
    r"(.*)\s+\(FORMERLY KNOWN AS\s+(.*)\)",
    r"(.*)\s+\(\s*FORMERLY KNOWN AS\s+(.*)\)",
    r"(.*)\s+\((.*?)\s+PRIOR TO\b",
]


def extract_name_variants(raw_name: str) -> list[str]:
    """Return one or more cleaned names from a raw company name string.

    Handles patterns like "Foo Inc (Formerly Known As Bar Corp)" by returning
    both the current and former names.
    """
    name = raw_name.upper()

    # Strip status notes
    for pat in _VARIANT_PATTERNS:
        m = re.search(pat, name)
        if m:
            name = m.group(1)
            break

    # Extract aliases
    for pat in _ALIAS_PATTERNS:
        m = re.search(pat, name)
        if m:
            return [standardize(m.group(1)), standardize(m.group(2))]

    # Generic parenthetical (keep only if long enough to be meaningful)
    m = re.search(r"(.*)\s+\((.*)\)", name)
    if m:
        main, paren = m.group(1), m.group(2)
        names = [standardize(main)]
        if len(paren) > 4:
            names.append(standardize(paren))
        return names

    return [standardize(name)]


# ---------------------------------------------------------------------------
# Stage 1: Exact matching
# ---------------------------------------------------------------------------

def exact_match(df_left: pd.DataFrame, df_right: pd.DataFrame,
                left_name_col: str, right_name_col: str) -> tuple:
    """Exact-merge two DataFrames on standardized firm names.

    Returns (matched, unmatched_left) DataFrames.  Both inputs should already
    have a column of standardized names.
    """
    merged = pd.merge(df_left, df_right,
                       left_on=left_name_col, right_on=right_name_col,
                       how="outer", indicator=True)
    matched = merged[merged["_merge"] == "both"].drop(columns="_merge")
    unmatched = merged[merged["_merge"] == "left_only"].drop(columns="_merge")
    return matched, unmatched


# ---------------------------------------------------------------------------
# Stage 2: Subsidiary matching
# ---------------------------------------------------------------------------

def subsidiary_match(unmatched: pd.DataFrame, subsidiaries: pd.DataFrame,
                     name_col: str, sub_name_col: str,
                     parent_id_col: str) -> tuple:
    """Try to link unmatched names to a parent firm via a subsidiary crosswalk.

    `subsidiaries` should have columns for the cleaned subsidiary name and the
    parent firm identifier.  Returns (matched, still_unmatched).
    """
    merged = pd.merge(unmatched, subsidiaries,
                       left_on=name_col, right_on=sub_name_col, how="left")
    matched = merged[merged[parent_id_col].notna()]
    still_unmatched = merged[merged[parent_id_col].isna()]
    return matched, still_unmatched


# ---------------------------------------------------------------------------
# Stage 3: Fuzzy matching
# ---------------------------------------------------------------------------

def fuzzy_match(unmatched_names: list[str], candidate_names: list[str],
                threshold: float = 0.85, limit: int = 3) -> pd.DataFrame:
    """For each unmatched name, find the closest candidates by Levenshtein ratio.

    Returns a DataFrame with columns: [query, match, score].
    Rows where score >= threshold are plausible matches to review manually.
    """
    results = []
    for query in unmatched_names:
        scored = [(cand, Levenshtein.ratio(query, cand))
                  for cand in candidate_names]
        scored.sort(key=lambda x: x[1], reverse=True)
        for cand, score in scored[:limit]:
            if score >= threshold:
                results.append({"query": query, "match": cand, "score": score})
    return pd.DataFrame(results)


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    # --- Adapt this section to your data ---

    # Example: two small DataFrames with raw firm names
    left = pd.DataFrame({"firm": ["Apple Inc.", "MICROSOFT CORP",
                                   "Alphabet (Formerly Known As Google)"]})
    right = pd.DataFrame({"company": ["APPLE", "GOOGLE", "AMAZON"]})

    # Standardize names
    left["clean"] = left["firm"].apply(standardize)
    right["clean"] = right["company"].apply(standardize)

    # Stage 1: exact match
    matched, unmatched = exact_match(left, right, "clean", "clean")
    print("=== Exact matches ===")
    print(matched[["firm", "company"]])

    # Stage 3: fuzzy match on remaining
    if not unmatched.empty:
        fuzzy = fuzzy_match(
            unmatched["clean"].tolist(),
            right["clean"].tolist(),
            threshold=0.5,
        )
        print("\n=== Fuzzy match candidates (review manually) ===")
        print(fuzzy)
