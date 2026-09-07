# CoT is Not the Chain of Truth — Project Website

Static, SEO-friendly academic project pages built from structured paper metadata.

## Live URLs

- Hub: `https://cheslyn0712.github.io/CoT_is_Not_the_Chain_of_Truth-website/`
- Paper page: `https://cheslyn0712.github.io/CoT_is_Not_the_Chain_of_Truth-website/projects/cot-chain-of-truth/`

## Local preview

Open the **paper page** directly (content is static HTML, no JS required):

```bash
cd CoT_is_Not_the_Chain_of_Truth-website
python -m http.server 8000
```

Visit: http://localhost:8000/projects/cot-chain-of-truth/

## Build system

```bash
python scripts/build_pages.py
```

This generates:

- `projects/<slug>/index.html` — full static paper page
- `projects/<slug>/paper.bib` — downloadable BibTeX
- `index.html` — publication hub
- `sitemap.xml`, `robots.txt`

## Add a new paper

1. Create `papers/<slug>.json` using `papers/cot-chain-of-truth.json` as template
2. Run `python scripts/build_pages.py`
3. Page will be available at `/projects/<slug>/`

## Architecture

- **Metadata:** `papers/*.json`
- **Template engine:** `scripts/build_pages.py` (single reusable `PaperPage` renderer)
- **Styles:** `styles.css`, `site-overrides.css`, `static/paper.css`
- **Progressive enhancement:** `static/copy-bibtex.js` (copy button only)

All title, abstract, authors, contributions, and BibTeX are rendered as visible HTML for search engines and readers without JavaScript.
