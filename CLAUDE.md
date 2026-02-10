# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic personal website for Renping Li (renpingli.com), built with Jekyll. Forked from AcademicPages template (derived from Minimal Mistakes theme). Hosted on GitHub Pages with custom domain configured via CNAME.

## Build & Development Commands

```bash
# Install Ruby dependencies (delete Gemfile.lock first if errors occur)
bundle install

# Local dev server with live reload at localhost:4000
bundle exec jekyll liveserve

# Dev server with development config overrides (expanded SASS, no analytics)
bundle exec jekyll serve --config _config.yml,_config.dev.yml

# Rebuild minified JavaScript (after editing assets/js/)
npm run build:js

# Generate publication/talk markdown from TSV data
cd markdown_generator && python publications.py
cd markdown_generator && python talks.py
```

Note: `_config.yml` is NOT auto-reloaded by `jekyll serve`; restart the server after config changes.

## Architecture

**Jekyll static site** with four collections defined in `_config.yml`:
- `_publications/` — research papers (generated from `markdown_generator/publications.tsv`)
- `_talks/` — presentations (generated from `markdown_generator/talks.tsv`)
- `_teaching/` — course materials
- `_portfolio/` — research projects

**Content pipeline:** TSV files → Python scripts in `markdown_generator/` → Markdown with YAML front matter → Jekyll builds to `_site/`.

**Template hierarchy:** `_layouts/` (7 layouts, `default.html` is base) → `_includes/` (36 partials) → `_sass/` (SCSS styles). Key layout: `single.html` handles most page rendering.

**Main pages** live in `_pages/` — the landing page is `about.md`. Navigation is configured in `_data/navigation.yml`.

**Static files** (CV PDF, profile images, slides) go in `files/`. Site images go in `images/`.

## Key Configuration

- `_config.yml` — all site settings, collection definitions, author metadata, plugin config
- `_config.dev.yml` — development overrides (localhost URL, no analytics)
- `_data/navigation.yml` — top nav menu structure
- `_includes/head/custom.html` — favicon, MathJax, academicons CSS

## Content Conventions

- Publication/talk filenames: `YYYY-MM-DD-url-slug.md`
- YAML front matter must HTML-escape special characters (`&amp;`, `&quot;`, `&#39;`)
- MathJax is enabled for math rendering (`$...$` inline, `$$...$$` display)
- Collections use `permalink: /:collection/:path/` pattern
