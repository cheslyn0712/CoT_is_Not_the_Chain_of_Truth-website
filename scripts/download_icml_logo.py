import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "static"
ROOT.mkdir(parents=True, exist_ok=True)

urls = {
    "icml-logo.svg": "https://icml.cc/media/Press/ICML-logo.svg",
    "icml-logo.png": "https://icml.cc/media/Press/ICML-logo.png",
    "icml-navbar-logo.svg": "https://icml.cc/static/core/img/icml-navbar-logo.svg",
}

for name, url in urls.items():
    try:
        data = urllib.request.urlopen(url, timeout=30).read()
        out = ROOT / name
        out.write_bytes(data)
        print(f"OK {name} ({len(data)} bytes)")
    except Exception as e:
        print(f"FAIL {name}: {e}")
