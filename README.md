<div align="center">

# Research Project Pages

Static, SEO-friendly project pages for published papers — summaries, figures, HTML tables, BibTeX, and links to code and PDFs.

[![Hub](https://img.shields.io/badge/Project-Hub-102033?style=for-the-badge&logo=googlechrome&logoColor=white)](https://cheslyn0712.github.io/CoT_is_Not_the_Chain_of_Truth-website/projects/)

</div>

---

## Papers

### CoT is Not the Chain of Truth · ICML 2026

[![Project](https://img.shields.io/badge/Project-Page-102033?style=for-the-badge&logo=googlechrome&logoColor=white)](https://cheslyn0712.github.io/CoT_is_Not_the_Chain_of_Truth-website/projects/cot-chain-of-truth/)
[![Code](https://img.shields.io/badge/Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cheslyn0712/CoT_is_Not_the_Chain_of_Truth)
[![arXiv](https://img.shields.io/badge/arXiv-2602.04856-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.04856)

Reasoning LLMs can harbor unsafe planning inside Chain-of-Thought traces even when the final answer refuses.

### CogniDir · EMNLP 2026

[![Project](https://img.shields.io/badge/Project-Page-102033?style=for-the-badge&logo=googlechrome&logoColor=white)](https://cheslyn0712.github.io/CoT_is_Not_the_Chain_of_Truth-website/projects/cognidir/)
[![Code](https://img.shields.io/badge/Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cheslyn0712/CogniDir)
[![arXiv](https://img.shields.io/badge/arXiv-2510.09712-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.09712)

Adaptive distributional learning for robust fake news detection against cognitive malicious comments.

---

## Build

```bash
python scripts/prepare_cognidir_figures.py   # CogniDir: render latex/figs PDFs → PNG
python scripts/build_pages.py
python -m http.server 8000
# open http://localhost:8000/projects/
```

## Custom domain (optional)

To serve at `https://chunlingong.me/projects/<slug>/` instead of `github.io/<repo>/projects/<slug>/`:

1. Add a `CNAME` file with `chunlingong.me` and configure DNS → GitHub Pages.
2. Set `siteBase` in each `papers/*.json` to `https://chunlingong.me`.
3. Re-run `python scripts/build_pages.py`.

This changes the public URL only; page structure and SEO metadata stay the same.
