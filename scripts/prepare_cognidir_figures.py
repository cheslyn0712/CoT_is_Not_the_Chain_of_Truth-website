"""Extract CogniDir figures from arXiv PDF into data/figures/."""

from pathlib import Path

import fitz

PDF = Path(r"D:\桌面\PhD_Reseach\EMNLP_2026\EMNLP2026\latex\paper.pdf")
OUT = Path(__file__).resolve().parents[1] / "data" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

CROPS = {
    "cognidir_teaser.png": (1, fitz.Rect(50, 120, 560, 420)),
    "cognidir_framework.png": (4, fitz.Rect(40, 120, 560, 320)),
    "cognidir_asr_before.png": (6, fitz.Rect(40, 80, 560, 340)),
    "cognidir_asr_after.png": (6, fitz.Rect(40, 360, 560, 620)),
}

doc = fitz.open(PDF)
for name, (page_no, rect) in CROPS.items():
    page = doc[page_no - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), clip=rect, alpha=False)
    path = OUT / name
    pix.save(path)
    print("saved", path.name, pix.width, pix.height)
