"""MILP solver for game plan generation.

Models the recommendation problem as a mixed-integer linear program:

    Decision: y_i ∈ {0,1} — include intervention i
    Auxiliary: z_ijk ∈ {0,1} — intervention i is the "primary" for marker j
               in mechanism class k (handles overlap)
    Constraints:
      Σ_i z_ijk ≤ 1 for each (j, k)         — only one primary per mechanism class
      z_ijk ≤ y_i                            — can only be primary if selected
      m_jk = Σ_i z_ijk · improvement_ij      — contribution from class k to marker j
      total_improvement_j = Σ_k m_jk         — sum across mechanism classes
      capped_j ≤ total_improvement_j         — and ≤ gap_j (don't overshoot)
      Σ_i y_i ≤ budget
    Objective:
      max Σ_j capped_j                       — severity-weighted partial progress
        + α · Σ_j gap_pct_j · cross_ref_j    — severity bonus for critical → healthy
        + β · Σ_j gap_pct_j · cross_opt_j    — severity bonus for any → optimal
        + γ · Σ_j cross_ref_j                — FLAT bonus per critical escape

V2: each intervention belongs to its FULL mechanism set (not just the first
mechanism), so overlap with other interventions on any shared mechanism is
modeled. To prevent a multi-mechanism intervention from being "primary" in
several classes simultaneously and claiming its effect N times, we add the
constraint Σ_k z_ijk ≤ 1 per (intervention, marker).

V3: gap-weighted crossing bonuses. The earlier objective `Σ capped/gap_pct`
normalized severity *out* — a 100% closure of a 2% gap counted the same as
100% closure of a 40% gap, biasing the solver toward broad shallow progress.
V3 drops the normalization (severe markers are now naturally weighted higher
because they have more % room to improve) and adds binary crossing indicators
for two thresholds per marker: `cross_ref` fires when a currently-critical
marker reaches the clinical reference boundary, `cross_opt` fires when any
out-of-optimal marker reaches the optimal subrange. Each crossing earns an
extra `gap_pct_j` units of objective, so harder wins pay more.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

import pulp

from fhetl.schemas import Effect, Intervention, Marker


@dataclass
class UserProfile:
    marker_values: dict[str, float]
    phenotype: str = "elevated"  # elevated | lean
    exclusions: set[str] = field(default_factory=set)
    traits: set[str] = field(default_factory=set)  # e.g. {"south_asian"} for tighter targets


@dataclass
class Plan:
    interventions: list[str]                       # ordered by contribution desc
    projected_marker_values: dict[str, float]
    improvements_pct: dict[str, float]             # per marker, % improvement
    uncovered_markers: list[str]                   # markers with gap but no improvement
    objective_value: float
    # V3: which markers the solver projects will cross a clinical threshold.
    # These come from the MILP's crossing binaries (canonical ref/opt boundaries
    # — independent of any per-user lab reference range shown in the UI).
    crossings_to_healthy: list[str] = field(default_factory=list)
    crossings_to_optimal: list[str] = field(default_factory=list)


def _mech_classes(intervention_id: str, interventions: dict[str, Intervention]) -> list[str]:
    """Mechanism classes an intervention belongs to.

    V2: each intervention is in its FULL mechanism set, not just the first.
    Lets the solver model overlap with other interventions on any shared mechanism.
    Singleton class for empty-mechanism interventions.
    """
    iv = interventions.get(intervention_id)
    if iv and iv.mechanisms:
        return list(iv.mechanisms)
    return [f"_singleton__{intervention_id}"]


def _effect_improvement_pct(
    effect: Effect, marker: Marker, phenotype: str
) -> float:
    """Adjusted, sign-corrected improvement contribution in % units.

    Positive = good (moves the marker toward optimal). Negative = bad.
    """
    mid = (effect.effect_lo + effect.effect_hi) / 2
    mod = (
        effect.baseline_mod_elevated if phenotype == "elevated"
        else effect.baseline_mod_lean
    )
    adjusted = mid * mod  # signed pct (decrease=negative)

    if marker.direction == "lower_is_better":
        return -adjusted   # decrease (negative pct) → positive improvement
    if marker.direction == "higher_is_better":
        return adjusted
    return 0.0  # in_band — punt for v1


def solve(
    profile: UserProfile,
    markers: dict[str, Marker],
    interventions: dict[str, Intervention],
    effects: list[Effect],
    budget: int = 5,
    alpha_ref_cross: float = 2.0,
    beta_opt_cross: float = 0.5,
    gamma_ref_flat: float = 10.0,
) -> Plan:
    """Build and solve the game-plan MILP.

    Crossing bonuses (escaping critical or reaching optimal) sit on top of
    severity-weighted continuous progress.

    `alpha_ref_cross` (default 2.0) — per-unit-severity bonus for a
        critical→healthy crossing. Scales with gap_pct.
    `beta_opt_cross` (default 0.5) — per-unit-severity bonus for any→optimal.
    `gamma_ref_flat` (default 10.0) — FLAT bonus per critical→healthy escape,
        independent of gap size. Ensures small-gap critical escapes (e.g.
        Vitamin D 19 → 30 ng/mL) still beat similar-severity healthy→optimal
        moves on clinical-relevance grounds.

    Total reward for a marker that fully escapes critical = capped_imp_j
        + α · gap_pct_j + γ; a critical→optimal jump also adds β · gap_pct_j.
    """
    # --- 1. Compute per-marker gap (absolute units) ---
    # Apply demographic modifiers (e.g., south_asian -> tighter ApoB target).
    # Demographic modifiers only affect the OPTIMAL boundary (per schema), so
    # critical-zone classification uses raw ref_lo/ref_hi for all users.
    def _effective_range(m: Marker) -> tuple[float, float]:
        opt_lo, opt_hi = m.opt_lo, m.opt_hi
        for d in m.demographic_modifiers:
            if d.trait in profile.traits:
                if d.opt_lo is not None: opt_lo = d.opt_lo
                if d.opt_hi is not None: opt_hi = d.opt_hi
        return opt_lo, opt_hi

    gaps: dict[str, float] = {}
    # % improvement required to reach the clinical-reference boundary, for
    # markers currently OUTSIDE that boundary (critical zone). 0 for markers
    # already in the healthy range.
    imp_for_ref_pct: dict[str, float] = {}
    immutable_out_of_range: list[str] = []
    for mid, val in profile.marker_values.items():
        m = markers.get(mid)
        if not m:
            continue
        opt_lo, opt_hi = _effective_range(m)
        if m.direction == "lower_is_better":
            gap = max(0.0, val - opt_hi)
            ref_excess = max(0.0, val - m.ref_hi)
            imp_ref = (ref_excess / val) * 100 if val > 0 and ref_excess > 0 else 0.0
        elif m.direction == "higher_is_better":
            gap = max(0.0, opt_lo - val)
            ref_deficit = max(0.0, m.ref_lo - val)
            imp_ref = (ref_deficit / val) * 100 if val > 0 and ref_deficit > 0 else 0.0
        else:
            gap = 0.0  # in_band — v1 ignores
            imp_ref = 0.0
        if m.immutable and gap > 0:
            # Marker is largely genetic / non-modifiable by lifestyle (e.g., Lp(a)).
            # Surface as uncovered; don't let the solver waste stack capacity on it.
            immutable_out_of_range.append(mid)
            continue
        gaps[mid] = gap
        imp_for_ref_pct[mid] = imp_ref
    needs_fixing = {mid: g for mid, g in gaps.items() if g > 0}

    # --- 2. Filter eligible effects ---
    candidates: list[tuple[Effect, float]] = []
    for e in effects:
        if e.marker_id not in needs_fixing:
            continue
        if e.intervention_id in profile.exclusions:
            continue
        marker = markers.get(e.marker_id)
        if marker is None:
            continue
        imp_pct = _effect_improvement_pct(e, marker, profile.phenotype)
        if imp_pct <= 0:
            continue  # raises the marker, or zero — skip
        candidates.append((e, imp_pct))

    if not candidates or not needs_fixing:
        return Plan(
            interventions=[],
            projected_marker_values=dict(profile.marker_values),
            improvements_pct={mid: 0.0 for mid in profile.marker_values},
            uncovered_markers=sorted(needs_fixing.keys()),
            objective_value=0.0,
        )

    # --- 3. Build MILP ---
    prob = pulp.LpProblem("game_plan", pulp.LpMaximize)
    eligible_ivs = sorted({e.intervention_id for e, _ in candidates})
    y = {i: pulp.LpVariable(f"y__{i}", cat="Binary") for i in eligible_ivs}

    # V2: each (effect) intervention is placed in EVERY one of its mechanism
    # classes, so it can compete with other interventions on any shared mechanism.
    by_class: dict[tuple[str, str], list[tuple[str, float]]] = defaultdict(list)
    for e, imp in candidates:
        for mech in _mech_classes(e.intervention_id, interventions):
            by_class[(e.marker_id, mech)].append((e.intervention_id, imp))

    z: dict[tuple[str, str, str], pulp.LpVariable] = {}
    m_var: dict[tuple[str, str], pulp.LpVariable] = {}
    for (marker_id, mech), entries in by_class.items():
        m_var[(marker_id, mech)] = pulp.LpVariable(
            f"m__{marker_id}__{mech}", lowBound=0
        )
        for iv_id, _ in entries:
            zkey = (marker_id, mech, iv_id)
            z[zkey] = pulp.LpVariable(
                f"z__{marker_id}__{mech}__{iv_id}", cat="Binary"
            )
            prob += z[zkey] <= y[iv_id]
        prob += pulp.lpSum(z[(marker_id, mech, iv)] for iv, _ in entries) <= 1
        prob += m_var[(marker_id, mech)] == pulp.lpSum(
            z[(marker_id, mech, iv)] * imp for iv, imp in entries
        )

    # V2 anti-double-count: an intervention contributes to a marker via at most
    # ONE mechanism class. Without this, a multi-mechanism intervention could be
    # primary in all of its classes simultaneously and claim its effect N times.
    by_iv_marker: dict[tuple[str, str], list[tuple[str, str, str]]] = defaultdict(list)
    for zkey in z:
        marker_id, mech, iv_id = zkey
        by_iv_marker[(iv_id, marker_id)].append(zkey)
    for (iv_id, marker_id), zkeys in by_iv_marker.items():
        if len(zkeys) > 1:
            prob += pulp.lpSum(z[k] for k in zkeys) <= 1

    # Per-marker totals, capped at gap (in % units). gap_pct doubles as both
    # the cap on `capped_imp` AND the threshold for the optimal-crossing binary
    # (reaching opt boundary == capped_imp at its cap).
    total_imp: dict[str, pulp.LpAffineExpression] = {}
    capped_imp: dict[str, pulp.LpVariable] = {}
    gap_pct_by_marker: dict[str, float] = {}
    for mid, gap_abs in needs_fixing.items():
        current = profile.marker_values[mid]
        gap_pct = (gap_abs / current) * 100 if current > 0 else 0.0
        gap_pct_by_marker[mid] = gap_pct
        contribs = [m_var[(j, k)] for (j, k) in m_var if j == mid]
        total_imp[mid] = pulp.lpSum(contribs)
        capped_imp[mid] = pulp.LpVariable(f"capped__{mid}", lowBound=0)
        prob += capped_imp[mid] <= total_imp[mid]
        prob += capped_imp[mid] <= gap_pct

    # V3: crossing binaries.
    #   cross_opt[mid] = 1 ⇒ capped_imp[mid] ≥ gap_pct (i.e. fully closed)
    #   cross_ref[mid] = 1 ⇒ capped_imp[mid] ≥ imp_for_ref_pct[mid]
    # Both are linear because the multipliers are constants per marker.
    # cross_ref only defined for currently-critical markers (imp_for_ref > 0).
    # When imp_for_ref ≥ gap_pct (shouldn't happen by construction since opt is
    # inside ref, but we guard) we skip the ref binary to avoid an unsatisfiable
    # tie with the gap cap.
    cross_opt: dict[str, pulp.LpVariable] = {}
    cross_ref: dict[str, pulp.LpVariable] = {}
    for mid, gap_pct in gap_pct_by_marker.items():
        if gap_pct <= 0:
            continue
        cross_opt[mid] = pulp.LpVariable(f"cross_opt__{mid}", cat="Binary")
        prob += capped_imp[mid] >= gap_pct * cross_opt[mid]

        imp_ref = imp_for_ref_pct.get(mid, 0.0)
        if 0 < imp_ref <= gap_pct:
            cross_ref[mid] = pulp.LpVariable(f"cross_ref__{mid}", cat="Binary")
            prob += capped_imp[mid] >= imp_ref * cross_ref[mid]

    # Budget
    prob += pulp.lpSum(y.values()) <= budget

    # Active-ingredient grouping: at most one selection per group. Stops the
    # solver from recommending two dose / formulation variants of the same
    # compound simultaneously (e.g. vitamin_d3_1000iu AND vitamin_d3_loading).
    # Interventions with active_ingredient=None are ungrouped and don't
    # participate in this constraint. Only applies when ≥2 eligible
    # interventions in the same group exist (otherwise the constraint is
    # trivial: y_i ≤ 1, already implied by y being binary).
    by_active: dict[str, list[str]] = defaultdict(list)
    for iv_id in eligible_ivs:
        iv = interventions.get(iv_id)
        if iv and iv.active_ingredient:
            by_active[iv.active_ingredient].append(iv_id)
    for group_key, group_ids in by_active.items():
        if len(group_ids) >= 2:
            prob += pulp.lpSum(y[i] for i in group_ids) <= 1

    # Objective: severity-weighted partial progress + gap-weighted crossing
    # bonuses + a FLAT escape-critical bonus, minus a tiny parsimony penalty.
    #   continuous:    Σ capped_imp_j                       — partial progress
    #   ref severity:  α · Σ gap_pct_j · cross_ref_j        — critical → healthy
    #   opt severity:  β · Σ gap_pct_j · cross_opt_j        — anything → optimal
    #   ref flat:      γ · Σ cross_ref_j                    — clinical bonus
    # The flat term γ ensures small-gap critical escapes (e.g. Vit D 19→30) are
    # rewarded on clinical-relevance grounds even when severity is modest. A
    # critical→optimal jump fires BOTH binaries — earning (α·gap + β·gap + γ)
    # on top of continuous, the most valuable single-marker move.
    PARSIMONY_PENALTY = 1e-4
    continuous_term = pulp.lpSum(capped_imp.values())
    ref_bonus = pulp.lpSum(
        gap_pct_by_marker[mid] * cross_ref[mid] for mid in cross_ref
    )
    opt_bonus = pulp.lpSum(
        gap_pct_by_marker[mid] * cross_opt[mid] for mid in cross_opt
    )
    ref_flat_bonus = pulp.lpSum(cross_ref.values())
    prob += (
        continuous_term
        + alpha_ref_cross * ref_bonus
        + beta_opt_cross * opt_bonus
        + gamma_ref_flat * ref_flat_bonus
        - PARSIMONY_PENALTY * pulp.lpSum(y.values())
    )

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    # --- 4. Extract solution ---
    contribution: dict[str, float] = defaultdict(float)
    for (mid, mech, iv_id), zvar in z.items():
        val = zvar.value()
        if val and val > 0.5:
            entries = dict(by_class[(mid, mech)])
            contribution[iv_id] += entries.get(iv_id, 0.0)

    # Only include interventions that actually contributed to some marker
    selected = [
        iv for iv in eligible_ivs
        if (y[iv].value() or 0) > 0.5 and contribution.get(iv, 0) > 0
    ]
    selected.sort(key=lambda iv: -contribution[iv])

    projected: dict[str, float] = {}
    improvements: dict[str, float] = {}
    for mid, current in profile.marker_values.items():
        imp_pct = (capped_imp[mid].value() or 0.0) if mid in capped_imp else 0.0
        improvements[mid] = imp_pct
        m = markers.get(mid)
        if m is None:
            projected[mid] = current
            continue
        if m.direction == "lower_is_better":
            projected[mid] = current * (1 - imp_pct / 100)
        elif m.direction == "higher_is_better":
            projected[mid] = current * (1 + imp_pct / 100)
        else:
            projected[mid] = current

    uncovered = sorted(
        [mid for mid in needs_fixing if improvements.get(mid, 0) <= 0.01]
        + immutable_out_of_range
    )

    crossings_to_healthy = sorted(
        mid for mid, var in cross_ref.items() if (var.value() or 0) > 0.5
    )
    crossings_to_optimal = sorted(
        mid for mid, var in cross_opt.items() if (var.value() or 0) > 0.5
    )

    return Plan(
        interventions=selected,
        projected_marker_values=projected,
        improvements_pct=improvements,
        uncovered_markers=uncovered,
        objective_value=prob.objective.value() or 0.0,
        crossings_to_healthy=crossings_to_healthy,
        crossings_to_optimal=crossings_to_optimal,
    )
