<div align="center">

# CoT is Not the Chain of Truth

**An Empirical Internal Analysis of Reasoning LLMs for Fake News Generation**

<p>
  <a href="https://icml.cc/virtual/2026/poster/61042" target="_blank" rel="noopener noreferrer">
    <img src="static/icml-navbar-logo.svg" alt="ICML" height="28" align="middle"><strong> ICML 2026</strong>
  </a>
</p>

[![arXiv](https://img.shields.io/badge/arXiv-2602.04856-b31b1b?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.04856)
[![Code](https://img.shields.io/badge/Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cheslyn0712/CoT_is_Not_the_Chain_of_Truth)
[![PDF](https://img.shields.io/badge/Paper-PDF-243447?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://arxiv.org/pdf/2602.04856)

<p>
  <strong>Zhao Tong</strong><sup>*</sup> ·
  <strong>Chunlin Gong</strong><sup>*</sup> ·
  <strong>Yiping Zhang</strong> ·
  <strong>Haichao Shi</strong> ·
  <strong>Qiang Liu</strong> ·
  <strong>Xingcheng Xu</strong><sup>†</sup> ·
  <strong>Shu Wu</strong> ·
  <strong>Xiao-Yu Zhang</strong><sup>†</sup>
</p>
<p><sup>*</sup>Equal contribution: Zhao Tong, Chunlin Gong · <sup>†</sup>Corresponding author: Xingcheng Xu, Xiao-Yu Zhang</p>
<p>Institute of Information Engineering, CAS · University of Chinese Academy of Sciences · University of Minnesota · Shanghai AI Laboratory · Institute of Automation, CAS</p>

</div>

---

## Overview

Reasoning LLMs can harbor unsafe planning inside Chain-of-Thought (CoT) traces **even when the final answer refuses**. We localize these failures to mid-depth layers and safety-critical attention heads via Jacobian spectral metrics (B1–B3).

**Generalization:** We show the same routing pattern extends **beyond fake-news generation** to **HarmBench** jailbreak tasks on Flan-UL2 and DeepSeek-R1-70B. Critical-head fine-tuning improves CoT safety on both News (+67.1 avg.) and HarmBench (+55.0 avg.) with only 0.64%–1.95% parameter updates.

**Live project pages:**
- [CoT is Not the Chain of Truth](https://cheslyn0712.github.io/CoT_is_Not_the_Chain_of_Truth-website/projects/cot-chain-of-truth/)
- [CogniDir](https://cheslyn0712.github.io/CoT_is_Not_the_Chain_of_Truth-website/projects/cognidir/)

## Pipeline

Three stages: **CoT_Generation** → **CoT_Annotation** → **CoT_Analysis**

```
Seed (Real_News.json)
  → Raw ({model}/{prompt_type}/{style}/news.json)
    → Processed ({model}/{prompt_type}/{style}/news.json)
      → HumanCheck ({model}/{prompt_type}/{style}/news.json)
```

Code: https://github.com/cheslyn0712/CoT_is_Not_the_Chain_of_Truth

## Build

```bash
python scripts/build_pages.py
python -m http.server 8000
# open http://localhost:8000/projects/cot-chain-of-truth/
```

## Citation

If you find this work useful, please cite:

```bibtex
@misc{tong2026cotchaintruthempirical,
      title={CoT is Not the Chain of Truth: An Empirical Internal Analysis of Reasoning LLMs for Fake News Generation}, 
      author={Zhao Tong and Chunlin Gong and Yiping Zhang and Haichao Shi and Qiang Liu and Xingcheng Xu and Shu Wu and Xiao-Yu Zhang},
      year={2026},
      eprint={2602.04856},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.04856}, 
},
```
