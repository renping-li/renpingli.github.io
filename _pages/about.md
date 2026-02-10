---
permalink: /
title:
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LK2GPXZMWH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-LK2GPXZMWH');
</script>

<style>
/* Section spacing to account for sticky header */
section[id] {
  scroll-margin-top: 90px;
}
section[id] + section[id] {
  margin-top: 2em;
  padding-top: 1em;
  border-top: 1px solid #eee;
}


/* Publication styles */
.pub-title {
  font-size: 110%;
  font-weight: bold;
}
.pub-entry {
  margin-bottom: 1.5em;
}
details.abstract {
  margin-top: 0.25em;
  margin-bottom: 0.5em;
}
details.abstract summary {
  cursor: pointer;
  font-weight: 600;
  font-size: 0.85em;
  color: #7B2D8E;
  list-style: none;
  display: inline-block;
}
details.abstract summary::-webkit-details-marker {
  display: none;
}
details.abstract summary::before {
  content: "► ";
  font-size: 0.8em;
}
details.abstract[open] summary::before {
  content: "▼ ";
}
details.abstract p {
  margin-top: 0.5em;
  padding: 0.75em 1em;
  background: #f8f8f8;
  border-left: 3px solid #006747;
  font-size: 0.9em;
  line-height: 1.6;
}

/* Citation modal */
.cite-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  justify-content: center;
  align-items: center;
}
.cite-overlay.active {
  display: flex;
}
.cite-modal {
  background: #fff;
  border-radius: 6px;
  max-width: 700px;
  width: 90%;
  max-height: 80vh;
  overflow: auto;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  border-top: 4px solid #006747;
}
.cite-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75em 1em;
  border-bottom: 1px solid #eee;
}
.cite-modal-header h3 {
  margin: 0;
  font-size: 1em;
  color: #006747;
}
.cite-modal-close {
  background: none;
  border: none;
  font-size: 1.4em;
  cursor: pointer;
  color: #999;
  padding: 0 0.25em;
  line-height: 1;
}
.cite-modal-close:hover {
  color: #333;
}
.cite-modal-body {
  padding: 1em;
}
.cite-modal-body pre {
  background: #f8f8f8;
  border-left: 3px solid #7B2D8E;
  padding: 0.75em 1em;
  font-size: 0.82em;
  line-height: 1.5;
  white-space: pre-wrap;
  word-wrap: break-word;
  margin: 0;
  font-family: Monaco, Consolas, "Lucida Console", monospace;
}
.cite-copy-btn {
  display: inline-block;
  margin-top: 0.75em;
  padding: 0.35em 0.9em;
  font-size: 0.8em;
  font-weight: 600;
  color: #fff;
  background: #7B2D8E;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.cite-copy-btn:hover {
  background: #5e2270;
}
.pub-links {
  margin-top: 0.3em;
}
.pub-links a, .pub-links .cite-link {
  display: inline-block;
  padding: 0.15em 0.55em;
  margin: 0.15em 0.1em;
  font-size: 0.82em;
  font-weight: 500;
  color: #7B2D8E;
  border: 1px solid rgba(123, 45, 142, 0.35);
  border-radius: 3px;
  text-decoration: none;
  transition: all 0.15s ease;
}
.pub-links a:hover, .pub-links .cite-link:hover {
  background: #7B2D8E;
  color: #fff;
  text-decoration: none;
  border-color: #7B2D8E;
}
.cite-link {
  cursor: pointer;
  font-weight: 500;
}

/* Data & Code styles */
.data-entry {
  margin-bottom: 1.5em;
}
.data-title {
  font-size: 110%;
  font-weight: bold;
}
.data-row {
  margin-top: 0.35em;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.2em;
}
.data-label {
  font-size: 0.82em;
  font-weight: 600;
  color: #006747;
  margin-right: 0.2em;
  white-space: nowrap;
}
.data-row a {
  display: inline-block;
  padding: 0.15em 0.55em;
  font-size: 0.82em;
  font-weight: 500;
  color: #7B2D8E;
  border: 1px solid rgba(123, 45, 142, 0.35);
  border-radius: 3px;
  text-decoration: none;
  transition: all 0.15s ease;
}
.data-row a:hover {
  background: #7B2D8E;
  color: #fff;
  text-decoration: none;
  border-color: #7B2D8E;
}
.data-note {
  margin-top: 0.15em;
  margin-left: 0.1em;
  font-size: 0.82em;
  color: #555;
}

/* CV styles */
.cv-btn {
  display: inline-block;
  width: 120px;
  text-align: center;
  background-color: #7B2D8E !important;
}
.cv-btn:hover {
  background-color: #5e2270 !important;
}
.cv-embed {
  width: 100%;
  max-width: 100%;
  overflow: hidden;
}
.cv-embed iframe {
  border: none;
  width: 100%;
  height: 700px;
}
@media screen and (max-width: 768px) {
  .cv-embed {
    display: none;
  }
}
</style>

<section id="about" markdown="1">

Hi. I am an Assistant Professor of Finance at Tulane University. I hold a PhD in Finance from Washington University in St. Louis. I studied at The Ohio State University prior to PhD. You are welcome to check my <a href="/files/CV.pdf" target="_blank">CV</a>.

## Research Interests

AI & FinTech, Financial Intermediation, Corporate Governance

</section>

<section id="papers" markdown="1">

## Working Papers

<ol>
<li>
<div class="pub-entry">
<div class="pub-title">The Effects of Investment Bank Consolidation on Municipal Finance</div>
<div><em>Under Review</em></div>
<div>Recipient of <a href="https://easternfinance.org/best-paper-awards-of-2025/" target="_blank">Outstanding Doctoral Paper Award at EFA 2025 (Philadelphia)</a></div>
<div class="pub-links"><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4687748" target="_blank">SSRN</a> <a href="/files/slides_Li_UnderwriterMA.pdf" target="_blank">Slides</a> <a href="https://www.promarket.org/2024/05/20/banking-consolidation-raises-the-costs-for-local-governments-to-issue-new-debt/" target="_blank">ProMarket</a> <span class="cite-link" onclick="openCite('cite1')">Citation</span></div>
<details class="abstract"><summary>Abstract</summary><p>Antitrust regulators historically focused on commercial banking. Does investment bank consolidation have competitive effects? Using the municipal bond market as a natural laboratory, I find that underwriting spreads increase by 4.5% of their sample mean following within-market consolidation. The effects double for larger M&As or in concentrated markets. Narrative analysis and placebo tests support a causal interpretation. Consolidation does not generate efficiency gains that manifest as lower bond yields or substitution of other issuer-paid services. Further, Census data indicate a decline in issuance after consolidation. My findings provide a novel perspective on bank antitrust regulations.</p></details>
</div>
</li>

<li>
<div class="pub-entry">
<div class="pub-title">The Welfare Benefits of Pay-As-You-Go Financing</div>
<div>(<em>with Paul Gertler, Brett Green, &amp; David Sraer</em>)</div>
<div><em>Revise &amp; Resubmit at <b>Review of Economic Studies</b></em></div>
<div class="pub-links"><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4641559" target="_blank">SSRN</a> <a href="https://www.nber.org/papers/w33484" target="_blank">NBER Working Paper</a> <a href="/files/slides_GertlerGreenLiSraer.pdf" target="_blank">Slides</a> <span class="cite-link" onclick="openCite('cite2')">Citation</span></div>
<details class="abstract"><summary>Abstract</summary><p>The rapid expansion of digital financial products in low- and middle-income countries has increased access to credit but raises important questions about their welfare effects. Pay-as-you-go (PAYGo) financing is one such product, relying on lockout technology that allows lenders to remotely disable the collateral's flow benefits when borrowers miss payments. This paper quantifies the welfare effects of PAYGo financing. We build a dynamic structural model of consumer behavior and estimate it using a large-scale, multi-arm pricing experiment conducted by a fintech lender that offers PAYGo financing for smartphones. We find that the welfare gains from access to PAYGo financing are equivalent to a 3.4% increase in income while remaining highly profitable for the lender. The welfare gains are larger for low-risk borrowers and those in the middle of the income distribution. Under plausible assumptions, PAYGo dominates traditional secured loans for all but the riskiest consumers. We explore contract design and show that variations of PAYGo contracts can deliver further welfare improvements.</p></details>
</div>
</li>

<li>
<div class="pub-entry">
<div class="pub-title">Board Connections, Firm Profitability, and Product Market Actions</div>
<div>(<em>with Radha Gopalan &amp; Alminas Žaldokas</em>)</div>
<div><em>Revise &amp; Resubmit at <b>Journal of Financial Economics</b></em></div>
<div>Recipient of <a href="https://weinberg.udel.edu/2024-corporate-governance-symposium/" target="_blank">John L. Weinberg/IRRCi Research Paper Award</a></div>
<div>Recipient of <a href="http://ewfs.org/award/" target="_blank">Sudipto Bhattacharya Memorial Prize</a></div>
<div class="pub-links"><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4053853" target="_blank">SSRN</a> <a href="/files/slides_GopalanLiZaldokas.pdf" target="_blank">Slides</a> <a href="https://clsbluesky.law.columbia.edu/2023/04/11/do-board-connections-between-product-market-peers-impede-competition/" target="_blank">CLS Blue Sky Blog</a> <span class="cite-link" onclick="openCite('cite3')">Citation</span></div>
<details class="abstract"><summary>Abstract</summary><p>A firm's gross margin increases by 0.8 p.p. after forming a new direct board connection to a product market peer. Gross margin also rises by 0.4 p.p. after a connection is formed to a peer indirectly through a third intermediate firm. Further, using barcode-level data of 2.7 million products, we show that new board connections are related to higher consumer good prices, a greater tendency for market allocation, and slower new product introductions. The effects are stronger when the newly connected peers share corporate customers or have similar business descriptions and hold when controlling for other inter-firm relationships.</p></details>
</div>
</li>
</ol>

<!-- Citation Modals -->
<div class="cite-overlay" id="cite1" onclick="closeCite(event, 'cite1')">
<div class="cite-modal" onclick="event.stopPropagation()">
<div class="cite-modal-header"><h3>Citation</h3><button class="cite-modal-close" onclick="closeCiteBtn('cite1')">&times;</button></div>
<div class="cite-modal-body">
<pre id="cite1-text">@techreport{Li2025underwriter,
  author    = {Li, Renping},
  title     = {The Effects of Investment Bank Consolidation on Municipal Finance},
  year      = {2025},
  type      = {Working Paper},
  institution = {Tulane University},
  url       = {https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4687748}
}</pre>
<button class="cite-copy-btn" onclick="copyBib('cite1-text')">Copy BibTeX</button>
</div>
</div>
</div>

<div class="cite-overlay" id="cite2" onclick="closeCite(event, 'cite2')">
<div class="cite-modal" onclick="event.stopPropagation()">
<div class="cite-modal-header"><h3>Citation</h3><button class="cite-modal-close" onclick="closeCiteBtn('cite2')">&times;</button></div>
<div class="cite-modal-body">
<pre id="cite2-text">@techreport{GertlerGreenLiSraer2025,
  author    = {Gertler, Paul and Green, Brett and Li, Renping and Sraer, David},
  title     = {The Welfare Benefits of Pay-As-You-Go Financing},
  year      = {2025},
  type      = {Working Paper},
  institution = {UC Berkeley, Washington University in St.~Louis, Tulane University, UC Berkeley},
  url       = {https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4641559}
}</pre>
<button class="cite-copy-btn" onclick="copyBib('cite2-text')">Copy BibTeX</button>
</div>
</div>
</div>

<div class="cite-overlay" id="cite3" onclick="closeCite(event, 'cite3')">
<div class="cite-modal" onclick="event.stopPropagation()">
<div class="cite-modal-header"><h3>Citation</h3><button class="cite-modal-close" onclick="closeCiteBtn('cite3')">&times;</button></div>
<div class="cite-modal-body">
<pre id="cite3-text">@techreport{GopalanLiZaldokas2025,
  author    = {Gopalan, Radha and Li, Renping and \v{Z}aldokas, Alminas},
  title     = {Board Connections, Firm Profitability, and Product Market Actions},
  year      = {2025},
  type      = {Working Paper},
  institution = {Washington University in St.~Louis, Tulane University, Hong Kong University of Science and Technology},
  url       = {https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4053853}
}</pre>
<button class="cite-copy-btn" onclick="copyBib('cite3-text')">Copy BibTeX</button>
</div>
</div>
</div>

</section>

<section id="teaching" markdown="1">

## Teaching

### Tulane University

Fall 2025: Financial Management (FINE 3010)

</section>

<section id="data-code" markdown="1">

## Data & Code

<ol>
<li>
<div class="data-entry">
<div class="data-title">Investment Bank Consolidation and Municipal Finance</div>
<div>(<em>Li, 2025</em>)</div>
<div class="data-row"><span class="data-label">Replication:</span> <a href="https://github.com/renping-li/MuniUnderwriterMA" target="_blank">GitHub Repository</a></div>
<div class="data-row"><span class="data-label">Data:</span> <a href="https://github.com/renping-li/MuniUnderwriterMA/blob/main/SCRIPT_hand_search_M%26A.csv" target="_blank">Municipal Bond Underwriter M&As, 1970-2022</a></div>
</div>
</li>

<li>
<div class="data-entry">
<div class="data-title">The Welfare Benefits of Pay-As-You-Go Financing</div>
<div>(<em>Gertler, Green, Li, &amp; Sraer, 2025</em>)</div>
<div class="data-row"><span class="data-label">Code:</span> <a href="https://github.com/renping-li/renpingli.github.io/blob/master/files/ReusableFiles/TikTak_global.m" target="_blank">TikTak_global.m</a> <a href="https://github.com/renping-li/renpingli.github.io/blob/master/files/ReusableFiles/TikTak_local.m" target="_blank">TikTak_local.m</a></div>
<div class="data-note">A working example of <a href="https://www.fatihguvenen.com/tiktak" target="_blank">TikTak Global Optimizer</a> in Matlab</div>
</div>
</li>

<li>
<div class="data-entry">
<div class="data-title">Board Connections, Firm Profitability, and Product Market Actions</div>
<div>(<em>Gopalan, Li, &amp; Žaldokas, 2025</em>)</div>
<div class="data-row"><span class="data-label">Code:</span> <a href="https://github.com/renping-li/renpingli.github.io/blob/master/files/ReusableFiles/3_Match_BoardEx_UPCPrefix.ipynb" target="_blank">Match_BoardEx_UPCPrefix.ipynb</a></div>
<div class="data-note">Matching between GS1 (UPC prefixes) and BoardEx by firm name</div>
</div>
</li>
</ol>

</section>

<section id="cv" markdown="1">

## CV

<a href="/files/CV.pdf" download><button class="btn cv-btn"><i class="fa fa-download"></i> Download</button></a>
<a href="/files/CV.pdf" target="_blank"><button class="btn cv-btn"><i class="fa fa-eye"></i> View</button></a>
<br>
<br>
<div class="cv-embed">
  <iframe src="/files/CV.pdf#navpanes=0"></iframe>
</div>

</section>

<script>
// Citation modal functions
function openCite(id) {
  document.getElementById(id).classList.add('active');
}
function closeCite(event, id) {
  if (event.target === document.getElementById(id)) {
    document.getElementById(id).classList.remove('active');
  }
}
function closeCiteBtn(id) {
  document.getElementById(id).classList.remove('active');
}
function copyBib(preId) {
  var text = document.getElementById(preId).textContent;
  navigator.clipboard.writeText(text).then(function() {
    var btns = document.querySelectorAll('.cite-copy-btn');
    btns.forEach(function(b) {
      if (b.closest('.cite-modal-body').querySelector('pre').id === preId) {
        var orig = b.textContent;
        b.textContent = 'Copied!';
        b.style.background = '#006747';
        setTimeout(function() { b.textContent = orig; b.style.background = ''; }, 1500);
      }
    });
  });
}

// Scroll-based active nav highlighting
(function() {
  var sections = document.querySelectorAll('section[id]');
  var navLinks = document.querySelectorAll('#site-nav .visible-links a[href*="#"]');

  if (!sections.length || !navLinks.length) return;

  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        var id = entry.target.getAttribute('id');
        navLinks.forEach(function(link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '/#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }, {
    rootMargin: '-80px 0px -50% 0px',
    threshold: 0
  });

  sections.forEach(function(section) {
    observer.observe(section);
  });
})();
</script>
