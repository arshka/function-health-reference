"""CLI for validation and game-plan generation.

Usage:
    uv run python -m fhetl.cli validate data/
    uv run python -m fhetl.cli plan --apob 110 --budget 3
    uv run python -m fhetl.cli plan --apob 110 --south-asian --budget 3
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml
from pydantic import ValidationError

from fhetl.schemas import Effect, Intervention, Marker
from fhetl.solver import UserProfile, solve
from fhetl.validator import Registry, ValidationResult, validate_effect, validate_intervention


CANONICAL_DIR = Path(__file__).resolve().parent / "canonical"
DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _classify_yaml(path: Path) -> str:
    parent = path.parent.name
    if parent == "effects":
        return "effect"
    if parent == "interventions":
        return "intervention"
    if parent == "markers":
        return "marker"
    return "unknown"


def _load_dataset(data_dir: Path) -> tuple[
    dict[str, Marker], dict[str, Intervention], list[Effect]
]:
    markers: dict[str, Marker] = {}
    interventions: dict[str, Intervention] = {}
    effects: list[Effect] = []
    for path in sorted(data_dir.rglob("*.yaml")):
        kind = _classify_yaml(path)
        data = yaml.safe_load(path.read_text())
        if kind == "marker":
            m = Marker.model_validate(data)
            markers[m.id] = m
        elif kind == "intervention":
            iv = Intervention.model_validate(data)
            interventions[iv.id] = iv
        elif kind == "effect":
            effects.append(Effect.model_validate(data))
    return markers, interventions, effects


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------

def cmd_validate(args: argparse.Namespace) -> int:
    registry = Registry.from_canonical(
        markers_yaml=CANONICAL_DIR / "markers.yaml",
        mechanisms_yaml=CANONICAL_DIR / "mechanisms.yaml",
    )
    print(f"Loaded registry: {len(registry.marker_ids)} markers, {len(registry.mechanism_ids)} mechanisms")

    n_ok = n_err = n_warn = 0
    for path in sorted(args.path.rglob("*.yaml")):
        kind = _classify_yaml(path)
        rel = path.relative_to(args.path)
        try:
            data = yaml.safe_load(path.read_text())
            if kind == "effect":
                model = Effect.model_validate(data)
                result = validate_effect(model, registry)
            elif kind == "intervention":
                model = Intervention.model_validate(data)
                result = validate_intervention(model, registry)
            elif kind == "marker":
                Marker.model_validate(data)
                result = ValidationResult()
            else:
                print(f"  SKIP  {rel} (unknown kind)")
                continue
        except ValidationError as e:
            print(f"  FAIL  {rel}")
            for err in e.errors():
                loc = ".".join(str(x) for x in err["loc"])
                print(f"        {loc}: {err['msg']}")
            n_err += 1
            continue

        if result.ok:
            tag = "OK   " if not result.warnings else "WARN "
            print(f"  {tag} {rel}")
            for w in result.warnings:
                print(f"        ⚠ {w}")
                n_warn += 1
            n_ok += 1
        else:
            print(f"  FAIL  {rel}")
            for err in result.errors:
                print(f"        ✗ {err}")
            n_err += 1

    print(f"\n{n_ok} ok, {n_err} failed, {n_warn} warnings")
    return 0 if n_err == 0 else 1


# ---------------------------------------------------------------------------
# plan
# ---------------------------------------------------------------------------

# Short aliases for common markers (in addition to the auto-derived
# --{marker_id_with_dashes} flag for every canonical marker).
MARKER_ALIASES = {
    "triglycerides": "--tg",
    "vitamin_d_25oh": "--vitamin-d",
    "vitamin_b12": "--b12",
    "homocysteine": "--hcy",
    "fasting_glucose": "--glucose",
    "fasting_insulin": "--insulin",
}


def _build_marker_flags() -> dict[str, list[str]]:
    """Return {marker_id: [flag, ...]} derived from canonical/markers.yaml.

    Every marker gets a `--{id_with_dashes}` flag plus any aliases above.
    """
    canonical_path = CANONICAL_DIR / "markers.yaml"
    flags: dict[str, list[str]] = {}
    data = yaml.safe_load(canonical_path.read_text()) or {}
    for entry in data.get("markers", []):
        mid = entry["id"]
        primary = "--" + mid.replace("_", "-")
        flags[mid] = [primary]
        if mid in MARKER_ALIASES:
            flags[mid].append(MARKER_ALIASES[mid])
    return flags


MARKER_FLAGS = _build_marker_flags()


def cmd_plan(args: argparse.Namespace) -> int:
    data_dir = args.data_dir or DEFAULT_DATA_DIR
    markers, interventions, effects = _load_dataset(data_dir)

    marker_values: dict[str, float] = {}
    for marker_id in MARKER_FLAGS:
        val = getattr(args, marker_id, None)
        if val is not None:
            marker_values[marker_id] = val

    if not marker_values:
        print("error: no marker values provided. use e.g. --apob 110", file=sys.stderr)
        return 2

    phenotype = "lean" if args.lean else "elevated"
    exclusions = set(args.exclude or [])
    traits: set[str] = set()
    if args.south_asian:
        traits.add("south_asian")
    profile = UserProfile(
        marker_values=marker_values,
        phenotype=phenotype,
        exclusions=exclusions,
        traits=traits,
    )

    plan = solve(profile, markers, interventions, effects, budget=args.budget)

    # --- presentation ---
    print(f"\nProfile: {phenotype}-baseline" + (f", south-asian optimal targets" if args.south_asian else ""))
    print(f"Budget: ≤ {args.budget} interventions")
    print(f"\nCurrent → projected marker values:")
    for mid, current in profile.marker_values.items():
        m = markers.get(mid)
        if m is None:
            print(f"  {mid}: {current} (marker not in dataset; skipped)")
            continue
        projected = plan.projected_marker_values.get(mid, current)
        opt_hi = m.opt_hi
        opt_lo = m.opt_lo
        if args.south_asian:
            for d in m.demographic_modifiers:
                if d.trait == "south_asian":
                    if d.opt_hi is not None: opt_hi = d.opt_hi
                    if d.opt_lo is not None: opt_lo = d.opt_lo
        in_range = opt_lo <= projected <= opt_hi
        marker_emoji = "✓" if in_range else "•"
        print(f"  {marker_emoji} {mid}: {current:.0f} → {projected:.1f} {m.units}"
              f"  (optimal {opt_lo:.0f}–{opt_hi:.0f}; "
              f"improvement {plan.improvements_pct.get(mid, 0):.1f}%)")

    if plan.interventions:
        print(f"\nRecommended stack ({len(plan.interventions)} of ≤{args.budget}):")
        for i, iv_id in enumerate(plan.interventions, 1):
            iv = interventions.get(iv_id)
            if iv:
                mech = ", ".join(iv.mechanisms) if iv.mechanisms else "—"
                print(f"  {i}. {iv.canonical_name} ({iv.dose_amount} {iv.dose_unit})")
                print(f"     mechanisms: {mech}")
            else:
                print(f"  {i}. {iv_id}")
    else:
        print("\nNo interventions recommended.")

    if plan.uncovered_markers:
        print(f"\n⚠ Uncovered (no lifestyle intervention in dataset):")
        for mid in plan.uncovered_markers:
            print(f"  • {mid}: still at {profile.marker_values[mid]:.0f}, no eligible intervention")
        print("  → these may require pharmacotherapy or are immutable (e.g., Lp(a) is largely genetic)")

    print()
    return 0


# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(prog="fhetl")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="validate a directory of YAML data files")
    p_validate.add_argument("path", type=Path)
    p_validate.set_defaults(func=cmd_validate)

    p_plan = sub.add_parser("plan", help="generate a game plan for given marker values")
    p_plan.add_argument("--data-dir", type=Path, default=None)
    p_plan.add_argument("--budget", type=int, default=3,
                        help="max number of interventions in stack (default 3)")
    p_plan.add_argument("--lean", action="store_true",
                        help="lean-baseline phenotype (reduces effect magnitudes)")
    p_plan.add_argument("--south-asian", action="store_true",
                        help="apply south-asian optimal targets when available")
    p_plan.add_argument("--exclude", nargs="*", default=[],
                        help="intervention ids to exclude")
    for marker_id, flags in MARKER_FLAGS.items():
        p_plan.add_argument(*flags, type=float, default=None,
                            dest=marker_id,
                            help=f"current {marker_id} value")
    p_plan.set_defaults(func=cmd_plan)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
