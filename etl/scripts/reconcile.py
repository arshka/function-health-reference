"""Reconciliation pass after parallel agent extraction.

Run after the 6 (or 118) extraction agents finish. Checks:
1. Every intervention_id referenced in an effect file has a matching intervention YAML
2. Detects near-duplicate intervention IDs (different agents naming the same thing)
3. Reports per-marker effect counts (gives a sense of coverage)
4. Reports per-mechanism intervention counts
5. Surfaces interventions with multiple mechanisms (potential overlap-modeling gaps)

Does NOT auto-resolve dupes — surfaces them for human review.

Usage:
    uv run python scripts/reconcile.py
"""
from __future__ import annotations

import difflib
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"


def _strip_dose(intervention_id: str) -> str:
    """psyllium_husk_10g -> psyllium_husk; aerobic_zone2_150min_wk -> aerobic_zone2."""
    # Remove trailing dose-like tokens (digit+unit)
    parts = intervention_id.split("_")
    while parts and re.match(r"^\d+([a-z]+)?$", parts[-1]):
        parts.pop()
    # Also strip common unit tail tokens
    while parts and parts[-1] in {"wk", "week", "weekly", "daily", "day", "kg", "ml", "g", "mg", "iu", "min"}:
        parts.pop()
    return "_".join(parts)


def main() -> int:
    effects_dir = DATA_DIR / "effects"
    interventions_dir = DATA_DIR / "interventions"
    markers_dir = DATA_DIR / "markers"

    # --- 1. Collect intervention references from effect files ---
    refs_by_marker: dict[str, list[str]] = defaultdict(list)
    effect_count = 0
    for path in sorted(effects_dir.glob("*.yaml")):
        data = yaml.safe_load(path.read_text())
        if not data:
            continue
        iv = data.get("intervention_id")
        mk = data.get("marker_id")
        if iv and mk:
            refs_by_marker[mk].append(iv)
            effect_count += 1

    # --- 2. List intervention files actually on disk ---
    on_disk = {p.stem for p in interventions_dir.glob("*.yaml")}

    # --- 3. Find orphan references (effect references an intervention with no YAML) ---
    all_referenced: set[str] = set()
    for refs in refs_by_marker.values():
        all_referenced.update(refs)
    orphans = all_referenced - on_disk

    # --- 4. Detect near-duplicate intervention IDs ---
    # Group by stripped-dose stem; flag groups with more than one entry
    by_stem: dict[str, list[str]] = defaultdict(list)
    for iv_id in on_disk:
        by_stem[_strip_dose(iv_id)].append(iv_id)
    near_dupes = {k: v for k, v in by_stem.items() if len(v) > 1}

    # Also fuzzy-match for typos / different conventions (e.g., almonds_60g vs almond_60g)
    fuzzy_pairs = []
    iv_list = sorted(on_disk)
    for i, a in enumerate(iv_list):
        for b in iv_list[i + 1:]:
            ratio = difflib.SequenceMatcher(None, a, b).ratio()
            if 0.85 < ratio < 1.0 and _strip_dose(a) != _strip_dose(b):
                fuzzy_pairs.append((a, b, ratio))

    # --- 5. Per-marker effect counts ---
    marker_files = {p.stem for p in markers_dir.glob("*.yaml")}
    marker_coverage = {m: len(refs_by_marker.get(m, [])) for m in marker_files}

    # --- 6. Mechanism histogram ---
    mech_counter: Counter[str] = Counter()
    multi_mech_ivs: list[tuple[str, list[str]]] = []
    for path in interventions_dir.glob("*.yaml"):
        data = yaml.safe_load(path.read_text()) or {}
        mechs = data.get("mechanisms") or []
        mech_counter.update(mechs)
        if len(mechs) >= 2:
            multi_mech_ivs.append((data.get("id"), mechs))

    # --- Report ---
    print("=" * 60)
    print("RECONCILIATION REPORT")
    print("=" * 60)
    print(f"\nTotals:")
    print(f"  Effect files: {effect_count}")
    print(f"  Intervention files: {len(on_disk)}")
    print(f"  Marker files: {len(marker_files)}")
    print(f"  Unique interventions referenced: {len(all_referenced)}")

    print(f"\nPer-marker effect coverage:")
    for m in sorted(marker_coverage, key=lambda x: -marker_coverage[x]):
        bar = "█" * min(marker_coverage[m], 30)
        print(f"  {m:20s} {marker_coverage[m]:3d}  {bar}")

    if orphans:
        print(f"\n⚠  Orphan intervention references (no YAML): {len(orphans)}")
        for o in sorted(orphans):
            print(f"     • {o}")
    else:
        print(f"\n✓ No orphan intervention references.")

    if near_dupes:
        print(f"\n⚠  Near-duplicate intervention IDs (same stem, different doses — verify intentional):")
        for stem, ivs in sorted(near_dupes.items()):
            print(f"     {stem}: {', '.join(sorted(ivs))}")
    else:
        print(f"\n✓ No near-duplicate intervention IDs.")

    if fuzzy_pairs:
        print(f"\n⚠  Fuzzy-matched intervention pairs (possible naming inconsistency):")
        for a, b, r in fuzzy_pairs:
            print(f"     {a}  ↔  {b}  ({r:.2f} similarity)")
    else:
        print(f"\n✓ No fuzzy-matched intervention pairs.")

    print(f"\nTop mechanisms by intervention count:")
    for mech, count in mech_counter.most_common(10):
        bar = "▌" * count
        print(f"  {mech:35s} {count:3d}  {bar}")

    print(f"\nMulti-mechanism interventions: {len(multi_mech_ivs)} (note: v1 solver only uses FIRST mechanism)")

    return 0 if not orphans else 1


if __name__ == "__main__":
    raise SystemExit(main())
