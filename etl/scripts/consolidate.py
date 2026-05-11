"""Atomically merge two intervention IDs in the data/ tree.

Use after reconcile.py surfaces a duplicate. Rewrites every effect file's
intervention_id field, renames the effect filenames, and removes the now-orphan
intervention YAML.

Usage:
    uv run python scripts/consolidate.py --from old_id --to new_id [--data-dir PATH]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = REPO_ROOT / "data"


def consolidate(*, data_dir: Path, old_id: str, new_id: str) -> dict:
    """Merge old_id into new_id across data_dir.

    Returns a summary dict with counts of files touched. Raises:
      - FileNotFoundError if either intervention YAML is missing
      - FileExistsError if a target effect filename already exists
    """
    interventions_dir = data_dir / "interventions"
    effects_dir = data_dir / "effects"

    old_iv = interventions_dir / f"{old_id}.yaml"
    new_iv = interventions_dir / f"{new_id}.yaml"
    if not old_iv.exists():
        raise FileNotFoundError(f"Old intervention YAML not found: {old_iv}")
    if not new_iv.exists():
        raise FileNotFoundError(f"New intervention YAML not found: {new_iv}")

    # Find effect files belonging to old_id (filename prefix match)
    old_effect_files = sorted(effects_dir.glob(f"{old_id}__*.yaml"))

    # Pre-flight: ensure no target collisions before any mutation
    renames: list[tuple[Path, Path]] = []
    for src in old_effect_files:
        suffix = src.name[len(old_id) + 2:]  # after "old_id__"
        dst = effects_dir / f"{new_id}__{suffix}"
        if dst.exists():
            raise FileExistsError(
                f"Target effect file already exists: {dst} "
                f"(consolidating {old_id}->{new_id} would clobber). "
                f"Resolve manually before retrying."
            )
        renames.append((src, dst))

    # Mutate: rewrite intervention_id field then rename file
    pattern = re.compile(rf"^(intervention_id:\s*){re.escape(old_id)}\s*$", re.MULTILINE)
    for src, dst in renames:
        text = src.read_text()
        new_text, n = pattern.subn(rf"\g<1>{new_id}", text)
        if n == 0:
            # Filename matched but field doesn't — odd, but fix by rewriting via yaml load
            data = yaml.safe_load(text) or {}
            data["intervention_id"] = new_id
            new_text = yaml.safe_dump(data, sort_keys=False)
        dst.write_text(new_text)
        src.unlink()

    # Drop the old intervention YAML
    old_iv.unlink()

    return {
        "old_id": old_id,
        "new_id": new_id,
        "effects_renamed": len(renames),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="old_id", required=True)
    parser.add_argument("--to", dest="new_id", required=True)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    args = parser.parse_args()

    summary = consolidate(
        data_dir=args.data_dir, old_id=args.old_id, new_id=args.new_id
    )
    print(
        f"Consolidated {summary['old_id']} -> {summary['new_id']}: "
        f"{summary['effects_renamed']} effect file(s) renamed, "
        f"intervention YAML removed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
