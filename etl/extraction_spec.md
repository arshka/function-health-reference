# Extraction pipeline — spec for the 3-agent ensemble

Per-marker markdown tables (e.g. `biomarker_interventions/cardiovascular/ApoB.md`) → validated YAML effect files (`etl/data/effects/{intervention}__{marker}.yaml`).

The orchestrator is not yet built. This document is the spec it implements.

---

## Pipeline overview

```
   markdown source file (e.g. ApoB.md)
                │
        ┌───────┼───────┐
        │       │       │
     Agent A  Agent B  Agent C       ← different prompts/personas/models
        │       │       │
        └───┬───┴───┬───┘
            ▼       ▼
        Schema validator (per-agent)  ← discards malformed outputs cell-by-cell
            │
            ▼
        Canonicalization              ← normalize intervention/marker IDs
            │
            ▼
        Voting + reconciliation       ← per-cell agreement → confidence tag
            │
            ▼
        Merged YAML output            ← {intervention}__{marker}.yaml + confidence
            │
            ▼
        Human review queue            ← disagreements + missed-row candidates
```

Critical invariant: **schema validation runs per-agent before any voting.** A malformed extraction is dropped for that cell, not voted on.

---

## The three agent personas

Each agent gets the same source markdown and the same YAML output contract, but a different traversal strategy. The goal is uncorrelated error patterns.

### Persona A — row-by-row faithful

> "You are a careful research-data extractor. Read the source markdown table row by row, top to bottom. For each row, emit exactly one effect file per (intervention, marker) pair the row describes. Do not skip rows. Do not invent rows. If a row mentions multiple markers (e.g. 'ApoB −5%; LDL-C −7 mg/dL'), emit one effect file per marker. Preserve the row's exact numbers; do not round."

### Persona B — by canonical intervention

> "You are organizing research by intervention. For each named food/supplement/activity mentioned anywhere in the source, emit all effect files describing its effects on the document's marker. Group by intervention; list every effect found. After emitting, return a list of `rows_seen` containing the source's row index for every row you extracted from, so the orchestrator can detect missed rows."

### Persona C — by marker column

> "You are a marker-effect cataloguer. The source document is about ONE marker. For every effect-bearing claim in the document (foods, supplements, supplements that don't work, activities, wearables, behaviors — all sections), emit one effect file. Include negative effects (interventions that *raise* the marker) — these are equally important. Use direction=increase for raising effects."

The personas overlap deliberately. Disagreement at the cell level signals real ambiguity in the source; agreement signals confidence.

---

## YAML output contract (what every agent must return)

For each `(intervention_id, marker_id)` pair, a YAML file matching `fhetl.schemas.Effect`:

```yaml
intervention_id: psyllium_husk_10g     # snake_case, includes dose for disambiguation
marker_id: apob                         # from canonical/markers.yaml
direction: decrease                     # decrease | increase
effect_type: pct                        # pct | absolute
effect_lo: -10                          # signed; matches direction
effect_hi: -7
baseline_mod_elevated: 1.0              # cited effect assumes this
baseline_mod_lean: 0.5                  # 30–60% of cited for lean baseline (default 0.5)
evidence_tag: meta                      # meta | rct | cohort | mr | mechanism | one_trial
evidence_weight: 1.0                    # canonical per tag — solver tiebreak
time_lo_wk: 4
time_hi_wk: 8
citations:
  - author: Jovanovski
    journal: AJCN
    year: 2018
    vol: 108
    page: 922
    pmid: "30101536"                    # digits only, 7–9 chars; null if unavailable
```

Plus, alongside the effects, each agent returns a single sidecar `_meta.yaml`:

```yaml
agent: persona_a
source_file: biomarker_interventions/cardiovascular/ApoB.md
rows_seen_per_section:
  section_1_foods_that_lower: 24
  section_2_foods_that_raise: 14
  section_3_supplements_improving: 13
  section_3_supplements_raising_or_ineffective: 9
  section_4_activities: 18
  section_5_wearables: 9
extraction_notes: ""                    # any ambiguity the agent wants to flag
```

The `rows_seen_per_section` count is the missed-row tripwire — agents that disagree on row counts have likely skipped rows.

---

## Canonicalization rules

Before voting, both intervention_id and marker_id are normalized:

- **marker_id** — must be in `canonical/markers.yaml`; otherwise the cell is rejected. No fuzzy matching.
- **intervention_id** — follow the `{name}_{dose}{unit}` pattern in snake_case:
  - `psyllium_husk_10g` not `psyllium` or `psyllium-husk` or `Psyllium-10g`
  - `evoo_30ml` not `extra_virgin_olive_oil` (use the common abbreviation in IDs)
  - Activities: `aerobic_zone2_150min_wk`, `hiit_3x_wk`
  - Behaviors with no dose: `smoking_cessation`, `time_restricted_eating_16_8`
- **mechanisms** — must come from `canonical/mechanisms.yaml`; unknown mechanisms are *warned* (not rejected) so research can extend the enum.

Intervention IDs that don't match an existing entry in `data/interventions/` trigger creation of a new intervention YAML in the same extraction pass.

---

## Voting logic

For each canonical `(intervention_id, marker_id)` key after schema validation has filtered out malformed outputs:

| Outcome | Action | confidence tag |
|---|---|---|
| 3/3 agree within tolerance | auto-accept | `high` |
| 2/3 agree | accept majority, log minority to review queue | `medium` |
| 0/3 agree (all different) | quarantine | `needs_review` |
| 2/3 *didn't extract this cell at all* | this is the dangerous case — flag as `possible_missed_row` | `needs_review` |
| 1/3 extracted | accept with caveat | `low_single_source` |

**Numeric tolerance for agreement:**
- pct effects: ±1.0 percentage point on both `effect_lo` and `effect_hi`
- absolute effects: ±5% of the larger absolute bound, with a minimum window of ±1 unit
- time ranges: ±2 weeks
- evidence_tag: exact match required
- baseline_mod_*: ±0.1
- citations: at least one PMID/author+year overlap

If any of (direction, effect_type, marker_id, intervention_id) differ across agents, this is a *categorical* disagreement and goes to quarantine regardless of numeric proximity.

---

## Citation reconciliation (separate stage)

PMIDs and journal/year/page are the highest-error-rate fields. Treat as a separate pipeline stage:

1. Collect all distinct citations across all 3 agents for each cell.
2. For PMIDs: vote on the canonical PMID. If ≥2 agree, use it. Otherwise fetch metadata from PubMed E-utilities and trust whichever extraction matches.
3. For non-PMID citations (older papers, books): use author+year+journal as the dedup key.

This stage runs after the effect-data voting but before final YAML write.

---

## Pilot calibration

Don't run all 118 markers in the first pass. Run the pipeline on **one panel first** (cardiovascular, 8 files), then:

1. Measure per-section row-count agreement
2. Measure per-cell agreement rate (high/medium/low/needs_review distribution)
3. Hand-audit the `needs_review` queue
4. If false-positive disagreements >20% → tighten canonicalization (intervention IDs, mechanism normalization)
5. If row-count mismatches >5% → tighten persona prompts (Persona A in particular)
6. **Diff the pilot output against the manually-extracted ground truth** in `data/effects/*__apob.yaml` (currently 2 files — extend before running pilot)

Calibrate. Then commit.

---

## What the pipeline produces

After a full run:

```
data/
  effects/
    psyllium_husk_10g__apob.yaml
    psyllium_husk_10g__ldl_c.yaml
    evoo_30ml__apob.yaml
    ...
  interventions/
    psyllium_husk_10g.yaml
    evoo_30ml.yaml
    ...
  _review_queue/
    cardiovascular__needs_review.yaml
    cardiovascular__possible_missed_rows.yaml
```

Each accepted effect file gets a `confidence:` field added by the orchestrator (the schema doesn't enforce it because it's metadata, not data — but it's preserved on read).

The review queue is the prioritized work list for a human pass. If the design is sound and the personas behave, it should contain only the rows where the source is genuinely ambiguous — those are the rows worth a human looking at.
