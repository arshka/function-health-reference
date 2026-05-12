"""Personal game-plan UI.

Run with:
    cd etl && uv run streamlit run app.py

Single-user, no auth, no deploy. Reads the live data/ corpus and calls the
MILP solver directly.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import pandas as pd
import streamlit as st

from fhetl.cli import _load_dataset
from fhetl.schemas import EVIDENCE_WEIGHTS
from fhetl.solver import UserProfile, solve
from personal_labs import load_personal_labs, DEFAULT_DUMP

DATA_DIR = Path(__file__).resolve().parent / "data"

st.set_page_config(page_title="Game Plan", layout="wide")

# --- load corpus once per session ---
@st.cache_resource
def load_corpus():
    return _load_dataset(DATA_DIR)


markers, interventions, effects = load_corpus()

# Pre-loaded values from .context/biomarker_dump.json (your Function labs)
@st.cache_resource
def load_my_labs():
    return load_personal_labs()


PERSONAL, PERSONAL_RANGES = load_my_labs()

# Index effects by marker for the coverage matrix later
effects_by_marker: dict[str, list] = defaultdict(list)
for e in effects:
    effects_by_marker[e.marker_id].append(e)
effects_by_intervention_marker: dict[tuple[str, str], list] = defaultdict(list)
for e in effects:
    effects_by_intervention_marker[(e.intervention_id, e.marker_id)].append(e)

# Group markers by panel
markers_by_panel: dict[str, list] = defaultdict(list)
for m in markers.values():
    markers_by_panel[m.panel].append(m)
for panel in markers_by_panel:
    markers_by_panel[panel].sort(key=lambda m: m.id)

# Markers that have at least one effect file (worth showing first)
markers_with_effects = {e.marker_id for e in effects}

# --- sidebar: profile + budget ---
with st.sidebar:
    st.header("Profile")
    phenotype = st.radio(
        "Baseline phenotype",
        ["elevated", "lean"],
        help="`elevated` = effect estimates assume an out-of-range starting point. "
             "`lean` halves effect magnitudes (best near-optimal users).",
    )
    south_asian = st.checkbox(
        "South-Asian targets",
        help="Tighter optimal cutoffs for ApoB, LDL-P, A/B-ratio, etc. where the "
             "research file documents elevated baseline cardiovascular risk.",
    )
    budget = st.slider("Max interventions in stack", 1, 10, 5)
    st.caption(
        "Solver picks ≤ this many interventions to maximize total marker improvement."
    )

    st.header("Exclusions")
    iv_options = sorted(interventions.keys())
    # Single source of truth for exclusions — sidebar multiselect AND the
    # per-row Remove buttons in the results section both write here.
    st.session_state.setdefault("excluded", [])
    excluded = st.multiselect(
        "Don't recommend these interventions",
        iv_options,
        key="excluded",
        help="E.g. you can't tolerate niacin, or you're vegan and want to skip "
             "fish-oil-named entries. The ✕ button next to each recommended "
             "intervention below also adds it here.",
    )

    st.header("Lab values")
    if PERSONAL:
        st.caption(f"Loaded {len(PERSONAL)} markers from `.context/biomarker_dump.json`")
        use_personal = st.checkbox("Use my labs as defaults", value=True)
    else:
        st.caption(f"No personal labs found at `{DEFAULT_DUMP}`")
        use_personal = False

    if st.button("Clear all entered values"):
        for k in list(st.session_state.keys()):
            if k.startswith("marker_"):
                del st.session_state[k]
        st.rerun()


# --- main: marker entry ---
st.title("Game Plan")
st.caption(
    f"Corpus: {len(markers)} markers · {len(interventions)} interventions · "
    f"{len(effects)} effects. Enter your lab values below; only entered markers are scored."
)

# Tabs by panel — sorted with fullest panels first for ergonomics
panel_order = sorted(
    markers_by_panel.keys(),
    key=lambda p: -sum(1 for m in markers_by_panel[p] if m.id in markers_with_effects),
)
tabs = st.tabs(panel_order)

entered_values: dict[str, float] = {}
for tab, panel in zip(tabs, panel_order):
    with tab:
        cols = st.columns(2)
        for i, m in enumerate(markers_by_panel[panel]):
            col = cols[i % 2]
            opt_lo, opt_hi = m.opt_lo, m.opt_hi
            if south_asian:
                for d in m.demographic_modifiers:
                    if d.trait == "south_asian":
                        if d.opt_lo is not None: opt_lo = d.opt_lo
                        if d.opt_hi is not None: opt_hi = d.opt_hi
            has_data = m.id in markers_with_effects
            label = f"{m.name}" + ("" if has_data else " *")
            help_text = (
                f"units: {m.units}  ·  "
                f"reference {m.ref_lo:g}–{m.ref_hi:g}  ·  "
                f"optimal {opt_lo:g}–{opt_hi:g}  ·  "
                f"{'lower better' if m.direction == 'lower_is_better' else 'higher better' if m.direction == 'higher_is_better' else 'in band'}"
            )
            if not has_data:
                help_text += "  ·  ⚠ no intervention effects in dataset (* asterisk)"
            default = PERSONAL.get(m.id) if use_personal else None
            val = col.number_input(
                label + (" 🟢" if default is not None else ""),
                key=f"marker_{m.id}",
                value=default,
                step=0.1,
                format="%g",
                help=help_text,
                placeholder=f"e.g. {(opt_lo + opt_hi) / 2:g}",
            )
            if val is not None:
                entered_values[m.id] = float(val)

# --- solve ---
st.divider()

if not entered_values:
    st.info("Enter at least one lab value above, then results will appear here.")
    st.stop()

profile = UserProfile(
    marker_values=entered_values,
    phenotype=phenotype,
    exclusions=set(excluded),
    traits={"south_asian"} if south_asian else set(),
)
plan = solve(profile, markers, interventions, effects, budget=budget)

# --- marker-by-marker result ---
st.subheader("Markers")


def _zone(val: float, m, opt_lo: float, opt_hi: float,
          lab_range: tuple[float | None, float | None] | None) -> str:
    """One of: 'optimal' (within opt range), 'healthy' (within ref but not opt),
    'critical' (outside ref). Direction-aware. Uses the lab's actual reference
    range (from biomarker_dump.json) when available; falls back to the engine's
    canonical ref_lo/ref_hi otherwise."""
    if lab_range is not None:
        ref_lo, ref_hi = lab_range
        ref_lo_eff = ref_lo if ref_lo is not None else float("-inf")
        ref_hi_eff = ref_hi if ref_hi is not None else float("inf")
        # Critical zone matches Function Health's [min, max) convention:
        # value exactly at rangeMin is in-range, but value exactly at rangeMax
        # is "above" (verified empirically: LDL Small 142/max 142 → above,
        # DPA 0.8/min 0.8 → in_range, MCH 27.0/min 27.0 → in_range).
        if m.direction == "lower_is_better":
            if val >= ref_hi_eff:
                return "critical"
        elif m.direction == "higher_is_better":
            if val < ref_lo_eff:
                return "critical"
        else:
            if val < ref_lo_eff or val >= ref_hi_eff:
                return "critical"
        # Inside lab range. Detect unit-scale mismatch with canonical opt range
        # (e.g. HDL Large lab=nmol/L, canonical=μmol/L → opt range meaningless).
        units_match = True
        if ref_hi is not None and opt_hi > 0:
            ratio = opt_hi / ref_hi
            if ratio < 0.1 or ratio > 10:
                units_match = False
        if ref_lo is not None and opt_lo > 0 and ref_lo > 0:
            ratio = opt_lo / ref_lo
            if ratio < 0.1 or ratio > 10:
                units_match = False
        if not units_match:
            return "healthy"  # can't trust opt at this scale
        if m.direction == "lower_is_better":
            return "optimal" if val <= opt_hi else "healthy"
        if m.direction == "higher_is_better":
            return "optimal" if val >= opt_lo else "healthy"
        return "optimal" if opt_lo <= val <= opt_hi else "healthy"

    # No lab range — pure canonical
    ref_lo, ref_hi = m.ref_lo, m.ref_hi
    if m.direction == "lower_is_better":
        if val <= opt_hi:
            return "optimal"
        if val <= ref_hi:
            return "healthy"
        return "critical"
    if m.direction == "higher_is_better":
        if val >= opt_lo:
            return "optimal"
        if val >= ref_lo:
            return "healthy"
        return "critical"
    if opt_lo <= val <= opt_hi:
        return "optimal"
    if ref_lo <= val <= ref_hi:
        return "healthy"
    return "critical"


def _bucket(cur_z: str, proj_z: str, imp_pct: float) -> str:
    """7-bucket status that distinguishes Healthy (in reference range) from
    Optimal (in the tighter optimal subrange)."""
    if cur_z == "optimal":
        return "🟢 Already optimal"
    if proj_z == "optimal":
        if cur_z == "critical":
            return "🔴→🟢 Critical → optimal"
        return "🟡→🟢 Healthy → optimal"
    if cur_z == "critical":
        if proj_z == "healthy":
            return "🔴→🟡 Critical → healthy (not yet optimal)"
        return "🔴 Still outside healthy range"
    # cur_z == healthy and proj_z == healthy (still not optimal)
    if imp_pct > 0.5:
        return "🟡 Improved, still healthy-not-optimal"
    return "🟡 Healthy but not optimal (no plan movement)"


# Build a row list, then sort + group.
records = []
for mid, current in entered_values.items():
    m = markers[mid]
    projected = plan.projected_marker_values.get(mid, current)
    opt_lo, opt_hi = m.opt_lo, m.opt_hi
    if south_asian:
        for d in m.demographic_modifiers:
            if d.trait == "south_asian":
                if d.opt_lo is not None: opt_lo = d.opt_lo
                if d.opt_hi is not None: opt_hi = d.opt_hi
    imp_pct = plan.improvements_pct.get(mid, 0)
    lab_range = PERSONAL_RANGES.get(mid) if use_personal else None
    cur_zone = _zone(current, m, opt_lo, opt_hi, lab_range)
    proj_zone = _zone(projected, m, opt_lo, opt_hi, lab_range)
    if lab_range is not None:
        lo, hi = lab_range
        healthy_str = f"{lo:g}–{hi:g}" if lo is not None and hi is not None else (
            f"≤{hi:g}" if hi is not None else f"≥{lo:g}"
        )
    else:
        healthy_str = f"{m.ref_lo:g}–{m.ref_hi:g}"
    records.append({
        "marker_id": mid,
        "Marker": m.name,
        "Direction": m.direction,
        "Current": current,
        "Projected": projected,
        "Healthy range": healthy_str,
        "Optimal range": f"{opt_lo:g}–{opt_hi:g}",
        "Units": m.units,
        "Current zone": cur_zone,
        "Projected zone": proj_zone,
        "Improvement %": imp_pct,
        "Status": _bucket(cur_zone, proj_zone, imp_pct),
    })

# --- Top-line zone counts: before vs after ---
def _count(zone_key: str, value: str) -> int:
    return sum(1 for r in records if r[zone_key] == value)

cur_crit, cur_health, cur_opt = _count("Current zone", "critical"), _count("Current zone", "healthy"), _count("Current zone", "optimal")
proj_crit, proj_health, proj_opt = _count("Projected zone", "critical"), _count("Projected zone", "healthy"), _count("Projected zone", "optimal")
cols = st.columns(3)
cols[0].metric("🟢 Optimal", f"{cur_opt} → {proj_opt}", delta=proj_opt - cur_opt)
cols[1].metric("🟡 Healthy (not optimal)", f"{cur_health} → {proj_health}", delta=proj_health - cur_health,
               delta_color="off")
cols[2].metric("🔴 Outside healthy range", f"{cur_crit} → {proj_crit}", delta=proj_crit - cur_crit,
               delta_color="inverse")

# Plain-language summary. Derived from the same (Current zone, Projected zone)
# classification that powers the tiles above, so the numbers always reconcile.
# This is intentionally NOT sourced from the solver's crossing binaries — those
# use canonical thresholds and can disagree with lab-specific reference ranges,
# which would show the user two contradicting stories. Single source of truth.
def _transition(cur: str, proj: str) -> int:
    return sum(1 for r in records if r["Current zone"] == cur and r["Projected zone"] == proj)

crit_to_opt = _transition("critical", "optimal")
crit_to_healthy = _transition("critical", "healthy")
healthy_to_opt = _transition("healthy", "optimal")
crit_stuck = _transition("critical", "critical")
healthy_stuck = _transition("healthy", "healthy")
addressable = cur_crit + cur_health
moved_category = crit_to_opt + crit_to_healthy + healthy_to_opt
# Markers improved meaningfully but didn't cross a category boundary.
improved_within = sum(
    1 for r in records
    if r["Improvement %"] >= 5.0 and r["Current zone"] == r["Projected zone"]
)

# Build a few bullet sentences that only appear when they have content.
lines: list[str] = []
if moved_category:
    parts = []
    if crit_to_opt:
        parts.append(f"**{crit_to_opt}** jump from outside-healthy straight into optimal")
    if crit_to_healthy:
        parts.append(f"**{crit_to_healthy}** escape outside-healthy into the normal range")
    if healthy_to_opt:
        parts.append(f"**{healthy_to_opt}** push from healthy-not-optimal into optimal")
    lines.append("Categorical wins: " + "; ".join(parts) + ".")
if improved_within:
    lines.append(
        f"**{improved_within}** more markers improve ≥5% but stay in the same category "
        "(see the bar chart and table for per-marker detail)."
    )
still_stuck = crit_stuck + healthy_stuck
if still_stuck:
    bits = []
    if crit_stuck:
        bits.append(f"{crit_stuck} still outside-healthy")
    if healthy_stuck:
        bits.append(f"{healthy_stuck} still healthy-but-not-optimal")
    lines.append(
        "Unmoved: " + ", ".join(bits) + ". "
        "Either no eligible intervention closes the gap, the effect is too small "
        "to cross the threshold at your starting value, or the marker is "
        "non-modifiable by lifestyle (see *Uncovered* below)."
    )

if addressable == 0:
    st.success(
        f"All {cur_opt} entered markers are already in the optimal range — "
        "no stack needed."
    )
else:
    st.markdown(
        f"**What this stack does for you:** of your {len(records)} entered "
        f"markers, **{addressable} have room to improve** "
        f"({cur_crit} outside-healthy + {cur_health} healthy-not-optimal). "
        "The solver projects:"
    )
    for line in lines:
        st.markdown(f"- {line}")
    st.caption(
        "Categories use your lab's reference range where available (for the "
        "outside-healthy boundary) and the canonical optimal subrange. A "
        "marker can improve a lot without crossing a category, and a small "
        "nudge can cross a category if it starts near the boundary — the "
        "bar chart shows raw % gain, the tiles show category transitions."
    )

# --- Top-improvements chart (the actionable wins) ---
movers = sorted(
    [r for r in records if r["Improvement %"] > 0.5],
    key=lambda r: -r["Improvement %"],
)[:12]
if movers:
    st.markdown("**Top projected improvements (sorted by % gain)**")
    chart_df = pd.DataFrame({
        "Marker": [r["Marker"] for r in movers],
        "Improvement %": [r["Improvement %"] for r in movers],
    }).set_index("Marker")
    st.bar_chart(chart_df, horizontal=True, height=min(60 + 35 * len(movers), 500))

# --- Full table, sorted by improvement % descending ---
table_df = pd.DataFrame(records).sort_values("Improvement %", ascending=False)
display = pd.DataFrame({
    "Marker": table_df["Marker"],
    "Current": [f"{c:g} {u}" for c, u in zip(table_df["Current"], table_df["Units"])],
    "Healthy": table_df["Healthy range"],
    "Optimal": table_df["Optimal range"],
    "Projected": [f"{p:.2f} {u}" for p, u in zip(table_df["Projected"], table_df["Units"])],
    "Improvement": [f"{p:+.1f}%" for p in table_df["Improvement %"]],
    "Status": table_df["Status"],
})
st.dataframe(display, use_container_width=True, hide_index=True)
st.caption(
    "**Healthy** = within standard clinical reference range. "
    "**Optimal** = tighter aspirational subrange (e.g., HbA1c 4.5–5.2% rather than just <5.6%). "
    "🔴 outside healthy · 🟡 healthy-not-optimal · 🟢 optimal."
)

# --- recommended stack ---
st.subheader(f"Recommended stack ({len(plan.interventions)} of ≤{budget})")
if not plan.interventions:
    st.warning(
        "No interventions selected — likely all entered markers are already in "
        "the optimal range, or every applicable intervention is excluded."
    )
else:
    # Strongest evidence tag per intervention (across contributing effects).
    evidence_for_iv: dict[str, str] = {}
    for iv_id in plan.interventions:
        best_weight = -1.0
        best_tag = "—"
        for mid in entered_values:
            for e in effects_by_intervention_marker.get((iv_id, mid), []):
                w = EVIDENCE_WEIGHTS.get(e.evidence_tag, 0)
                if w > best_weight:
                    best_weight = w
                    best_tag = e.evidence_tag
        evidence_for_iv[iv_id] = best_tag


    def _remove_intervention(iv_id: str) -> None:
        """Callback: add iv_id to the persistent exclusion list, triggering re-solve."""
        excluded_set = set(st.session_state.get("excluded", []))
        excluded_set.add(iv_id)
        st.session_state["excluded"] = sorted(excluded_set)


    # Manual table layout so we can put a Remove button per row.
    header = st.columns([3, 1, 2, 4, 1, 1])
    header[0].markdown("**Intervention**")
    header[1].markdown("**Type**")
    header[2].markdown("**Dose**")
    header[3].markdown("**Mechanisms**")
    header[4].markdown("**Evidence**")
    header[5].markdown("**Remove**")
    for iv_id in plan.interventions:
        iv = interventions.get(iv_id)
        c = st.columns([3, 1, 2, 4, 1, 1])
        if iv is None:
            c[0].write(iv_id)
            c[1].write("?"); c[2].write("?"); c[3].write("—"); c[4].write("—")
        else:
            c[0].write(iv.canonical_name)
            c[1].write(iv.type)
            c[2].write(f"{iv.dose_amount:g} {iv.dose_unit}")
            c[3].write(", ".join(iv.mechanisms) if iv.mechanisms else "—")
            c[4].write(evidence_for_iv[iv_id].upper())
        c[5].button(
            "✕",
            key=f"remove_{iv_id}",
            help=f"Exclude {iv_id} and re-solve. The solver will find the next-best "
                 f"alternative within budget.",
            on_click=_remove_intervention,
            args=(iv_id,),
        )
    st.caption(
        "Evidence: META > RCT > MR > COHORT > ONE_TRIAL > MECHANISM. "
        "Click ✕ to drop an intervention and let the solver re-pick — your exclusion "
        "is remembered in the sidebar list."
    )

# --- coverage matrix: how each intervention covers each marker ---
if plan.interventions and entered_values:
    st.subheader("Coverage matrix")
    st.caption(
        "Effect midpoint per (intervention, marker), in the marker's native units. "
        "Positive = intervention moves the marker toward optimal."
    )
    grid = []
    iv_names = []
    for iv_id in plan.interventions:
        iv = interventions.get(iv_id)
        iv_names.append(iv.canonical_name if iv else iv_id)
        row = {}
        for mid in entered_values:
            m = markers[mid]
            best = None
            for e in effects_by_intervention_marker.get((iv_id, mid), []):
                mid_val = (e.effect_lo + e.effect_hi) / 2
                # sign-correct: "good direction" magnitude
                if m.direction == "lower_is_better":
                    delta = -mid_val
                elif m.direction == "higher_is_better":
                    delta = mid_val
                else:
                    delta = abs(mid_val)
                if best is None or abs(delta) > abs(best):
                    best = delta
            row[m.name] = best if best is not None else None
        grid.append(row)
    cov_df = pd.DataFrame(grid, index=iv_names)
    # Format: hide NaN, show 1 decimal
    st.dataframe(
        cov_df.style.format("{:+.1f}", na_rep="—").background_gradient(
            cmap="Greens", axis=None, vmin=0
        ),
        use_container_width=True,
    )

# --- uncovered ---
if plan.uncovered_markers:
    st.subheader("Uncovered")
    uncovered_rows = []
    for mid in plan.uncovered_markers:
        m = markers.get(mid)
        if not m:
            continue
        reason = (
            "marked immutable in dataset (largely genetic)"
            if m.immutable
            else "no eligible intervention effects"
        )
        uncovered_rows.append({
            "Marker": m.name,
            "Current": f"{entered_values.get(mid, '—')} {m.units}",
            "Reason": reason,
        })
    if uncovered_rows:
        st.dataframe(pd.DataFrame(uncovered_rows), use_container_width=True, hide_index=True)
        st.caption(
            "These either need pharmacotherapy, are out of scope for the lifestyle engine, "
            "or have no effect data extracted yet."
        )

st.divider()
st.caption(
    f"Solver objective: {plan.objective_value:.4f}. "
    "Higher = better total normalized gap closure."
)
