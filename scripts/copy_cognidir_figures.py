"""Copy original CogniDir figure PDFs from latex/figs/ into the website.

No rasterization, no cropping, no screenshots — only verbatim copies of source files.
"""

from __future__ import annotations

import shutil
from pathlib import Path

SRC = Path(r"D:\桌面\PhD_Reseach\EMNLP_2026\EMNLP2026\latex\figs")
OUT = Path(__file__).resolve().parents[1] / "data" / "figures" / "cognidir"

FIGURES = (
    "Teaser0120_clean_noborder.pdf",
    "Method1833_clean_notext_0826.pdf",
    "ASR_ori_grid.pdf",
    "ASR_com_grid.pdf",
    "VAL_grid.pdf",
)


def main() -> None:
    if not SRC.is_dir():
        raise SystemExit(f"Missing figure source directory: {SRC}")
    OUT.mkdir(parents=True, exist_ok=True)
    for name in FIGURES:
        src = SRC / name
        if not src.is_file():
            raise SystemExit(f"Missing source figure: {src}")
        dst = OUT / name
        shutil.copy2(src, dst)
        print(f"copied {name} ({src.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
