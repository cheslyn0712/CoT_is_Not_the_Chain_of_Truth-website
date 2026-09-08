"""Convert CogniDir LaTeX figure PDFs (latex/figs/) to PNG for the project website."""

from __future__ import annotations

from pathlib import Path

import fitz

SRC = Path(r"D:\桌面\PhD_Reseach\EMNLP_2026\EMNLP2026\latex\figs")
OUT = Path(__file__).resolve().parents[1] / "data" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Source PDFs referenced in acl_latex.tex — render each file in full, never crop from paper.pdf.
FIGURES = {
    "cognidir_teaser.png": "Teaser0120_clean_noborder.pdf",
    "cognidir_framework.png": "Method1833_clean_notext_0826.pdf",
    "cognidir_asr_before.png": "ASR_ori_grid.pdf",
    "cognidir_asr_after.png": "ASR_com_grid.pdf",
    "cognidir_convergence.png": "VAL_grid.pdf",
}

SCALE = 3.0


def render_pdf(pdf_path: Path, out_path: Path) -> None:
    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), alpha=False)
    pix.save(out_path)
    print(f"saved {out_path.name} ({pix.width}x{pix.height}) from {pdf_path.name}")


def main() -> None:
    if not SRC.is_dir():
        raise SystemExit(f"Missing figure source directory: {SRC}")
    for out_name, src_name in FIGURES.items():
        src = SRC / src_name
        if not src.is_file():
            raise SystemExit(f"Missing source figure: {src}")
        render_pdf(src, OUT / out_name)


if __name__ == "__main__":
    main()
