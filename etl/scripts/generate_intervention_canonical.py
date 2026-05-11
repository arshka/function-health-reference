"""Dump the canonical intervention dictionary from data/interventions/.

Output is fed back into extraction-agent prompts as `{EXISTING_IV_IDS}` so
each new agent reuses existing IDs verbatim instead of inventing variants.

Usage:
    uv run python scripts/generate_intervention_canonical.py
"""
from __future__ import annotations

from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INTERVENTIONS_DIR = REPO_ROOT / "data" / "interventions"
DEFAULT_OUTPUT_PATH = REPO_ROOT / "fhetl" / "canonical" / "interventions.yaml"


def generate(*, interventions_dir: Path, output_path: Path) -> dict:
    entries: list[dict] = []
    for path in sorted(interventions_dir.glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        if not data.get("id"):
            continue
        entries.append({
            "id": data["id"],
            "canonical_name": data.get("canonical_name", ""),
            "type": data.get("type", ""),
        })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(yaml.safe_dump(
        {"interventions": entries}, sort_keys=False, default_flow_style=False
    ))
    return {"count": len(entries), "output_path": str(output_path)}


def main() -> int:
    summary = generate(
        interventions_dir=DEFAULT_INTERVENTIONS_DIR,
        output_path=DEFAULT_OUTPUT_PATH,
    )
    print(f"Wrote {summary['count']} interventions to {summary['output_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
