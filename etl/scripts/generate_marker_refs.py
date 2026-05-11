"""Generate canonical/markers.yaml from biomarker_interventions/ folder structure.

This is a one-shot generator. Run it whenever a new marker file is added.
The output is the canonical ID enum; full Marker records (with ref/opt ranges)
are extracted separately from the panel files.
"""
from pathlib import Path
import re
import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
INTERVENTIONS_DIR = REPO_ROOT / "biomarker_interventions"
OUTPUT = Path(__file__).resolve().parent.parent / "fhetl" / "canonical" / "markers.yaml"


def canonicalize(filename: str) -> str:
    """ApoB.md -> apob; non-HDL-C.md -> non_hdl_c; Lp(a).md -> lp_a; HOMA-IR.md -> homa_ir."""
    stem = Path(filename).stem
    # Replace non-alnum with underscore
    s = re.sub(r"[^A-Za-z0-9]+", "_", stem)
    # Collapse repeats and trim
    s = re.sub(r"_+", "_", s).strip("_")
    return s.lower()


def main() -> None:
    skip = {"INDEX", "README", "_TEMPLATE"}
    markers = []
    for path in sorted(INTERVENTIONS_DIR.rglob("*.md")):
        if path.stem in skip:
            continue
        panel = path.parent.name
        markers.append({"id": canonicalize(path.name), "panel": panel, "source_file": str(path.relative_to(REPO_ROOT))})

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w") as f:
        yaml.safe_dump({"markers": markers}, f, sort_keys=False, default_flow_style=False)
    print(f"Wrote {len(markers)} markers to {OUTPUT}")


if __name__ == "__main__":
    main()
