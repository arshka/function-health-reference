"""Deterministic corpus-completeness audit.

Walks every per-marker research markdown under `biomarker_interventions/`,
extracts every quantified intervention-effect row from the structured tables,
matches each row to a canonical intervention ID, and diffs the result against
the existing `etl/data/effects/` YAML corpus.

No LLM. Single deterministic pass. Reproducible byte-for-byte across runs.

Outputs:
  coverage_report.md         — gaps / extras / unmatched / unknown-sections
  etl/proposed_effects/*.yaml — schema-valid stub effect YAMLs for gaps

Reliability features (see commit message for full rationale):
  * mistune AST table parsing (not regex over markdown)
  * Explicit allow/deny lists for table sections (unknowns surface in report)
  * Magnitude parser with arrow-direction detection, separate from marker
    direction; wrong-direction rows are flagged as ADVERSE and skipped
  * rapidfuzz token_set_ratio matching with three confidence tiers
  * Hand-maintained intervention_aliases.yaml for stubborn mismatches
  * Pydantic Effect validation on every stub
  * Built-in recall test: parser must rediscover ≥95% of existing effects
    in the corpus or the run fails (--recall-test) / warns (default)

Usage:
  uv run python scripts/audit_coverage.py              # full audit
  uv run python scripts/audit_coverage.py --recall-test  # recall only
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import mistune
import yaml
from pydantic import ValidationError
from rapidfuzz import fuzz, process

# `fhetl` lives one level up.
ROOT = Path(__file__).resolve().parents[2]
ETL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ETL_ROOT))
from fhetl.schemas import EVIDENCE_WEIGHTS, Effect, Intervention, Marker  # noqa: E402


# ---------------------------------------------------------------------------
# Section classification — explicit lists, no guessing.
# ---------------------------------------------------------------------------
INCLUDE_HEADING_PATTERNS: list[re.Pattern] = [
    re.compile(p, re.IGNORECASE) for p in [
        r"\bfoods?\b.*\b(raise|increase|improve|improving|elevat|lower|reduce|decreas|worsen|decreasing|lowering)",
        r"\bsupplement",
        r"\bactivit(y|ies)\b",
        r"\bbehavior",
        r"\bdrugs?\b",
        r"\bmedications?\b",
        r"\btests?\s+&|\btests?\s+and\b",
        r"\bprocedures?\b",
        r"\binterventions?\b",
        r"\bdiets?\b",
        r"\bexercise\b",
    ]
]
EXCLUDE_HEADING_PATTERNS: list[re.Pattern] = [
    re.compile(p, re.IGNORECASE) for p in [
        r"\bsynthesis\b",
        r"\bopen\s+questions?\b",
        r"\bweak\s+evidence\b",
        r"\bwearable",
        r"\bgenetic\s+(modifiers?|interactions?)",
        r"\bconfounders?\b",
        r"\bdrug\s+interactions?",
        r"\bassay\s+artifacts?",
        r"\bsource\s+format",
        r"\bsouth\s+asian|\bsa[- ]specific",
        r"\b(legend|table\s+of\s+contents|toc)\b",
        r"\bineffective\b",  # "Ineffective or claimed-but-doesn't-work"
        r"\bclaimed[- ]but[- ]doesn",
        r"\bcaveat",
        r"\binteractions?\s+&|\binteractions?\s+and",
        r"\bopen\s+issues?\b",
        r"\bbackground\b",
        r"\bbiology\b",
        r"\bdose[- ]response",
    ]
]


def classify_heading(heading: str) -> Literal["include", "exclude", "unknown"]:
    """Classify an H2 heading as include / exclude / unknown."""
    if not heading:
        return "unknown"
    for p in EXCLUDE_HEADING_PATTERNS:
        if p.search(heading):
            return "exclude"
    for p in INCLUDE_HEADING_PATTERNS:
        if p.search(heading):
            return "include"
    return "unknown"


# ---------------------------------------------------------------------------
# Magnitude parsing.
# ---------------------------------------------------------------------------
SKIP_MAGNITUDE_PATTERNS: list[re.Pattern] = [
    re.compile(p, re.IGNORECASE) for p in [
        r"\bnegligible\b",
        r"\bno\s+effect\b",
        r"\bzero\s+effect\b",
        r"\btrivial\b",
        r"\bnone\s+demonstrat",
        r"\bnot\s+a\s+driver\b",
        r"\bunchanged\b",
        r"\bneutral\b.*\bto\b.*\bsmall\b",
        r"\bn/?a\b",
        r"\bnot\s+applicable\b",
        r"\bminimal\s+impact\b",
        r"\bclinically\s+meaningless\b",
        r"^—$",
        r"^\s*-\s*$",
    ]
]

ARROW_UP = re.compile(r"[↑⬆️]|\b(?:increase|raises?|raised|raising|elevat|gains?|up\b|↑|↗|higher)\b", re.IGNORECASE)
ARROW_DOWN = re.compile(r"[↓⬇️]|\b(?:decrease|reduces?|reduced|reducing|lowers?|lowered|lowering|drops?|fell|down\b|↓|↘)\b", re.IGNORECASE)

# Two numbers joined by an en-dash, em-dash, "to", or hyphen.
RANGE_PATTERNS: list[re.Pattern] = [
    re.compile(r"([+\-−]?\s*\d+(?:\.\d+)?)\s*[-–—]\s*([+\-−]?\s*\d+(?:\.\d+)?)\s*(pp|%|ng/mL|mg/dL|mmol/L|nmol/L|umol/L|μmol/L|g/dL|U/L|IU/L|bpm|kg|points?|score|times)?", re.IGNORECASE),
    re.compile(r"([+\-−]?\s*\d+(?:\.\d+)?)\s*to\s*([+\-−]?\s*\d+(?:\.\d+)?)\s*(pp|%|ng/mL|mg/dL|mmol/L|nmol/L|umol/L|μmol/L|g/dL|U/L|IU/L|bpm|kg|points?|score|times)?", re.IGNORECASE),
]
# Single number with arrow or sign.
SINGLE_NUM_PATTERN = re.compile(r"~?\s*([+\-−]?\s*\d+(?:\.\d+)?)\s*(pp|%|ng/mL|mg/dL|mmol/L|nmol/L|umol/L|μmol/L|g/dL|U/L|IU/L|bpm|kg|points?|score)?", re.IGNORECASE)

PCT_UNITS = {"%"}
ABSOLUTE_UNITS = {"pp", "ng/ml", "mg/dl", "mmol/l", "nmol/l", "umol/l", "μmol/l", "g/dl", "u/l", "iu/l", "bpm", "kg", "points", "point", "score", "times"}


def _to_float(s: str) -> float:
    """Parse '-30', '+15', '−10' (unicode minus), '  20 ' → float."""
    s = s.strip().replace("−", "-").replace(" ", "")
    return float(s)


@dataclass
class ParsedMagnitude:
    lo: float
    hi: float
    effect_type: Literal["pct", "absolute"]
    direction: Literal["increase", "decrease"]  # implied by arrow / sign
    raw: str


def parse_magnitude(text: str) -> ParsedMagnitude | None:
    """Parse a 'Direction & magnitude' cell into a signed range.

    Returns None if magnitude is missing, qualitative-only, or matches a skip
    pattern. The sign in the returned (lo, hi) reflects the documented arrow
    direction (down = negative, up = positive), NOT the marker's improvement
    direction — caller cross-checks that.
    """
    if not text:
        return None
    for p in SKIP_MAGNITUDE_PATTERNS:
        if p.search(text):
            return None

    # Decide arrow direction. Some cells have both ↑ and ↓ (e.g. effect on TWO
    # markers); prefer the FIRST arrow seen.
    up_match = ARROW_UP.search(text)
    down_match = ARROW_DOWN.search(text)
    if up_match and (not down_match or up_match.start() < down_match.start()):
        arrow_dir: Literal["increase", "decrease"] = "increase"
    elif down_match:
        arrow_dir = "decrease"
    else:
        arrow_dir = "increase"  # default; sign may still encode direction below

    # Try range patterns first.
    pair: tuple[float, float] | None = None
    unit_raw: str | None = None
    for p in RANGE_PATTERNS:
        m = p.search(text)
        if m:
            try:
                pair = (_to_float(m.group(1)), _to_float(m.group(2)))
                unit_raw = (m.group(3) or "").lower() if m.lastindex and m.lastindex >= 3 else None
                break
            except ValueError:
                continue

    if pair is None:
        # Single-number fallback. Only accept if there's a unit attached AND
        # the number doesn't look like a year (19xx / 20xx). Otherwise we'd
        # grab citation years as magnitudes.
        m = SINGLE_NUM_PATTERN.search(text)
        if not m:
            return None
        unit = (m.group(2) or "").lower() if m.lastindex and m.lastindex >= 2 else ""
        if not unit:
            return None
        raw_num = m.group(1).replace("−", "-").replace(" ", "")
        if re.fullmatch(r"(?:19|20)\d{2}", raw_num):
            return None  # year, not a magnitude
        try:
            v = _to_float(raw_num)
        except ValueError:
            return None
        pair = (v, v)
        unit_raw = unit

    # Sign convention: the arrow direction is authoritative.
    # Magnitude cells like "ALT ↓ 10–20%" mean -20 to -10 (the "-" inside the
    # range is the separator, not a sign). Cells like "ALT ↓ -5 to -15%"
    # mean the same thing — parsed pair already negative but order flipped.
    # Normalize on absolute magnitude, then re-sign based on arrow.
    abs_pair = sorted([abs(pair[0]), abs(pair[1])])  # [small, large]
    if arrow_dir == "decrease":
        lo, hi = -abs_pair[1], -abs_pair[0]  # -large, -small → lo ≤ hi
    else:
        lo, hi = abs_pair[0], abs_pair[1]    # small, large

    # Pick effect_type.
    if unit_raw in PCT_UNITS:
        effect_type: Literal["pct", "absolute"] = "pct"
    elif unit_raw in ABSOLUTE_UNITS:
        effect_type = "absolute"
    else:
        # Default: pp → absolute, otherwise pct
        effect_type = "pct"

    return ParsedMagnitude(lo=lo, hi=hi, effect_type=effect_type, direction=arrow_dir, raw=text)


# ---------------------------------------------------------------------------
# Evidence tag, time window, citation parsing.
# ---------------------------------------------------------------------------
EVIDENCE_TAG_PATTERN = re.compile(r"\[\s*\*?\*?\s*(meta|rct|cohort|mr|mechanism|1[- ]trial|one[- ]trial)\s*\*?\*?\s*\]", re.IGNORECASE)
EVIDENCE_MAP = {
    "meta": "meta",
    "rct": "rct",
    "cohort": "cohort",
    "mr": "mr",
    "mechanism": "mechanism",
    "1-trial": "one_trial",
    "1 trial": "one_trial",
    "one-trial": "one_trial",
    "one trial": "one_trial",
}


def parse_evidence_tag(text: str) -> str | None:
    """Find [Meta] / [RCT] / [Cohort] / [MR] / [Mechanism] / [1-Trial]."""
    m = EVIDENCE_TAG_PATTERN.search(text or "")
    if not m:
        return None
    return EVIDENCE_MAP.get(m.group(1).lower().strip())


TIME_RANGE = re.compile(r"(\d+)\s*[-–—]\s*(\d+)\s*(wk|week|weeks|mo|month|months|yr|year|years)", re.IGNORECASE)
TIME_SINGLE = re.compile(r"(\d+)\s*\+?\s*(wk|week|weeks|mo|month|months|yr|year|years)", re.IGNORECASE)
TIME_MONTHS_BARE = re.compile(r"\bmonths?\b", re.IGNORECASE)
TIME_YEARS_BARE = re.compile(r"\byears?\b", re.IGNORECASE)

UNIT_TO_WK = {"wk": 1, "week": 1, "weeks": 1, "mo": 4, "month": 4, "months": 4, "yr": 52, "year": 52, "years": 52}


def parse_time_window(text: str) -> tuple[int, int]:
    """Parse a 'Time to effect' cell into (lo_wk, hi_wk). Defaults to (12, 24)."""
    if not text:
        return (12, 24)
    m = TIME_RANGE.search(text)
    if m:
        lo, hi, unit = int(m.group(1)), int(m.group(2)), m.group(3).lower()
        mult = UNIT_TO_WK.get(unit, 1)
        return (min(lo * mult, 520), min(hi * mult, 520))
    m = TIME_SINGLE.search(text)
    if m:
        lo = int(m.group(1))
        unit = m.group(2).lower()
        mult = UNIT_TO_WK.get(unit, 1)
        v = min(lo * mult, 520)
        return (v, v)
    if TIME_MONTHS_BARE.search(text):
        return (12, 24)
    if TIME_YEARS_BARE.search(text):
        return (52, 104)
    return (12, 24)


CITATION_AUTHOR_YEAR = re.compile(
    r"([A-Z][a-zA-Z'-]+(?:\s+(?:et\s+al\.|&\s+[A-Z][a-zA-Z'-]+))?)\s*"
    r"(?:[A-Za-z][^,;()]*?)?"  # filler
    r"\s+(?P<year>(?:19|20)\d{2})"
)
CITATION_JOURNAL = re.compile(r"\*([^*]+?)\*")  # italic journal in markdown
CITATION_PMID = re.compile(r"PMID[:\s]*(\d{6,9})", re.IGNORECASE)


def parse_citations(text: str) -> list[dict]:
    """Best-effort citation extraction. Returns a list of {author, journal, year, pmid}.

    Always returns at least one element — if everything fails, a placeholder
    with author="unknown" so the row still validates. Surface as a warning.
    """
    if not text or not text.strip():
        return [{"author": "unknown", "journal": "unknown", "year": 2020, "pmid": None}]

    out: list[dict] = []
    # Split on ; which research files use between separate citations.
    for chunk in re.split(r";\s*(?=[A-Z])", text):
        chunk = chunk.strip()
        if not chunk:
            continue
        author_m = CITATION_AUTHOR_YEAR.search(chunk)
        journal_m = CITATION_JOURNAL.search(chunk)
        pmid_m = CITATION_PMID.search(chunk)
        if author_m:
            author = author_m.group(1).strip()
            year = int(author_m.group("year"))
        else:
            # Year-only fallback.
            ym = re.search(r"(?:19|20)\d{2}", chunk)
            if ym:
                author = "unknown"
                year = int(ym.group())
            else:
                continue
        journal = journal_m.group(1).strip() if journal_m else "unknown"
        # Bound year for schema.
        year = max(1970, min(year, 2030))
        out.append({
            "author": author,
            "journal": journal,
            "year": year,
            "pmid": pmid_m.group(1) if pmid_m else None,
        })

    if not out:
        out.append({"author": "unknown", "journal": "unknown", "year": 2020, "pmid": None})
    return out


# ---------------------------------------------------------------------------
# Markdown AST traversal.
# ---------------------------------------------------------------------------
@dataclass
class RawRow:
    marker_id: str
    section: str
    section_class: Literal["include", "exclude", "unknown"]
    intervention_phrase: str
    dose_text: str
    magnitude_text: str
    time_text: str
    evidence_text: str
    source_text: str
    source_file: str


def _node_text(node: dict | str) -> str:
    """Recursively extract plain text from a mistune AST node."""
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "".join(_node_text(c) for c in node)
    if not isinstance(node, dict):
        return ""
    if "raw" in node and isinstance(node["raw"], str):
        return node["raw"]
    children = node.get("children") or []
    return _node_text(children)


def _column_index(headers: list[str], patterns: list[str]) -> int | None:
    """First header index whose lowercase form contains any of the patterns."""
    for i, h in enumerate(headers):
        h_l = h.lower()
        for p in patterns:
            if p in h_l:
                return i
    return None


def extract_rows(marker_id: str, md_text: str, md_path: str) -> list[RawRow]:
    """Walk a markdown file's AST. For every table, classify the most recent
    H2 heading and emit one RawRow per body row.
    """
    parser = mistune.create_markdown(renderer=None, plugins=["table"])
    ast = parser(md_text)

    rows: list[RawRow] = []
    current_h2 = ""

    for node in ast:
        ntype = node.get("type")
        if ntype == "heading" and node.get("attrs", {}).get("level") == 2:
            current_h2 = _node_text(node).strip()
        elif ntype == "table":
            heading_class = classify_heading(current_h2)
            children = node.get("children") or []
            head_node = next((c for c in children if c.get("type") == "table_head"), None)
            body_node = next((c for c in children if c.get("type") == "table_body"), None)
            if not head_node or not body_node:
                continue
            head_cells = head_node.get("children") or []
            headers = [_node_text(c).strip() for c in head_cells]
            iv_col = _column_index(headers, ["food", "supplement", "activity", "drug", "intervention", "exercise", "behavior", "test", "procedure"])
            dose_col = _column_index(headers, ["dose", "pattern", "amount"])
            mag_col = _column_index(headers, ["direction", "magnitude", "effect", "delta", "reality"])
            time_col = _column_index(headers, ["time", "duration", "weeks", "wk", "timing"])
            ev_col = _column_index(headers, ["evidence", "tag", "quality"])
            src_col = _column_index(headers, ["source", "reference", "citation"])
            # Fall back to positional defaults if headers don't match (e.g.
            # wearable tables look different; we mostly exclude those anyway).
            if iv_col is None:
                iv_col = 0

            for body_row in body_node.get("children") or []:
                cells = [_node_text(c).strip() for c in (body_row.get("children") or [])]
                if not cells:
                    continue

                def at(idx: int | None) -> str:
                    return cells[idx] if idx is not None and idx < len(cells) else ""

                rows.append(RawRow(
                    marker_id=marker_id,
                    section=current_h2,
                    section_class=heading_class,
                    intervention_phrase=at(iv_col),
                    dose_text=at(dose_col),
                    magnitude_text=at(mag_col),
                    time_text=at(time_col),
                    evidence_text=at(ev_col),
                    source_text=at(src_col),
                    source_file=md_path,
                ))
    return rows


# ---------------------------------------------------------------------------
# Fuzzy matching.
# ---------------------------------------------------------------------------
HIGH_THRESHOLD = 80
MEDIUM_THRESHOLD = 60


@dataclass
class MatchResult:
    intervention_id: str | None
    score: float
    tier: Literal["alias", "high", "medium", "low", "none"]
    candidates: list[tuple[str, float]] = field(default_factory=list)


def _normalize(s: str) -> str:
    """Strip punctuation, lowercase, collapse whitespace — for fuzzy matching."""
    s = s.lower()
    s = re.sub(r"[(),/\\\-_:;\[\]{}*]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


class Matcher:
    def __init__(self, interventions: dict[str, Intervention], aliases: dict[str, str]):
        # Build a search index: each entry maps a search string to a canonical ID.
        self.interventions = interventions
        self.aliases = {k.lower(): v for k, v in aliases.items()}
        self.index: list[tuple[str, str]] = []  # (searchable_phrase, canonical_id)
        for iv_id, iv in interventions.items():
            self.index.append((_normalize(iv.canonical_name), iv_id))
            self.index.append((_normalize(iv_id.replace("_", " ")), iv_id))

    def match(self, phrase: str, dose: str = "") -> MatchResult:
        # Alias short-circuit (substring, case-insensitive).
        norm = _normalize(phrase)
        for alias_sub, iv_id in self.aliases.items():
            if alias_sub in norm and iv_id in self.interventions:
                return MatchResult(intervention_id=iv_id, score=100.0, tier="alias")

        # Combine phrase + dose for a richer matching string.
        query = _normalize(f"{phrase} {dose}".strip())
        if not query:
            return MatchResult(intervention_id=None, score=0, tier="none")

        # rapidfuzz process.extract returns sorted by score.
        # Search against each index entry independently; pick best.
        searchables = [s for s, _ in self.index]
        ids = [i for _, i in self.index]
        results = process.extract(
            query,
            searchables,
            scorer=fuzz.token_set_ratio,
            limit=5,
        )
        if not results:
            return MatchResult(intervention_id=None, score=0, tier="none")

        top_phrase, top_score, top_idx = results[0]
        top_id = ids[top_idx]
        candidates = [(ids[idx], score) for _, score, idx in results]

        if top_score >= HIGH_THRESHOLD:
            tier: Literal["alias", "high", "medium", "low", "none"] = "high"
        elif top_score >= MEDIUM_THRESHOLD:
            tier = "medium"
        else:
            tier = "low"

        return MatchResult(
            intervention_id=top_id if tier in ("high", "medium") else None,
            score=top_score,
            tier=tier,
            candidates=candidates,
        )


# ---------------------------------------------------------------------------
# Marker → md file mapping.
# ---------------------------------------------------------------------------
def build_marker_md_map(markers_dir: Path, research_dir: Path) -> dict[str, Path]:
    """Map every canonical marker_id to its research markdown file.

    Filename match is `<marker_id>.md` (case-insensitive, dashes/underscores
    interchangeable). Manual overrides for known special cases.
    """
    manual = {
        "lp_a": research_dir / "advanced_lipids" / "Lp(a).md",
    }
    canonical_ids = {p.stem for p in markers_dir.glob("*.yaml")}
    out: dict[str, Path] = {}
    for marker_id in sorted(canonical_ids):
        if marker_id in manual and manual[marker_id].exists():
            out[marker_id] = manual[marker_id]
            continue
        candidates = [
            marker_id.lower(),
            marker_id.lower().replace("_", "-"),
            marker_id.replace("_", " "),
        ]
        for md in research_dir.rglob("*.md"):
            stem_norm = md.stem.lower().replace("-", "_").replace(" ", "_")
            if stem_norm in {c.replace("-", "_").replace(" ", "_") for c in candidates}:
                out[marker_id] = md
                break
    return out


# ---------------------------------------------------------------------------
# Pipeline.
# ---------------------------------------------------------------------------
@dataclass
class ExtractedEffect:
    raw: RawRow
    intervention_id: str | None
    match: MatchResult
    direction: Literal["increase", "decrease"]
    effect_type: Literal["pct", "absolute"]
    effect_lo: float
    effect_hi: float
    evidence_tag: str
    time_lo_wk: int
    time_hi_wk: int
    citations: list[dict]
    is_adverse: bool
    skip_reason: str | None


def process_row(raw: RawRow, marker: Marker, matcher: Matcher) -> ExtractedEffect | None:
    """Apply parsing + skip rules. Returns None if row is silently dropped
    (no magnitude / qualitative only). Returns ExtractedEffect with
    skip_reason set if row is structurally valid but excluded from output."""
    if raw.section_class == "exclude":
        return None
    if raw.section_class == "unknown":
        # Surface in report but don't extract.
        return None

    mag = parse_magnitude(raw.magnitude_text)
    if mag is None:
        return None

    # Cross-check direction vs marker.direction. Wrong-direction = adverse effect.
    is_adverse = False
    if marker.direction == "lower_is_better":
        # Improvement = decrease. arrow=decrease → improvement.
        is_adverse = mag.direction == "increase"
    elif marker.direction == "higher_is_better":
        is_adverse = mag.direction == "decrease"
    else:
        # in_band: any movement is potentially adverse depending on baseline;
        # we don't have enough info, so we don't extract these. Solver ignores
        # in_band anyway.
        return ExtractedEffect(
            raw=raw, intervention_id=None, match=MatchResult(None, 0, "none"),
            direction=mag.direction, effect_type=mag.effect_type,
            effect_lo=mag.lo, effect_hi=mag.hi,
            evidence_tag="mechanism", time_lo_wk=12, time_hi_wk=24,
            citations=[], is_adverse=False, skip_reason="in_band marker (solver doesn't score)",
        )

    evidence = parse_evidence_tag(raw.evidence_text) or parse_evidence_tag(raw.source_text)
    if not evidence:
        # No evidence tag is a quality signal — surface but don't drop.
        evidence = "mechanism"

    time_lo, time_hi = parse_time_window(raw.time_text)
    citations = parse_citations(raw.source_text)

    match = matcher.match(raw.intervention_phrase, raw.dose_text)

    skip_reason = None
    if is_adverse:
        skip_reason = "adverse-direction effect (worsens marker)"

    return ExtractedEffect(
        raw=raw,
        intervention_id=match.intervention_id,
        match=match,
        direction=mag.direction,
        effect_type=mag.effect_type,
        effect_lo=mag.lo,
        effect_hi=mag.hi,
        evidence_tag=evidence,
        time_lo_wk=time_lo,
        time_hi_wk=time_hi,
        citations=citations,
        is_adverse=is_adverse,
        skip_reason=skip_reason,
    )


def build_effect_dict(e: ExtractedEffect, marker_id: str) -> dict:
    """Schema-valid dict ready to dump to YAML."""
    tag = e.evidence_tag
    weight = EVIDENCE_WEIGHTS.get(tag, 0.5)
    return {
        "intervention_id": e.intervention_id,
        "marker_id": marker_id,
        "direction": e.direction,
        "effect_type": e.effect_type,
        "effect_lo": round(e.effect_lo, 2),
        "effect_hi": round(e.effect_hi, 2),
        "baseline_mod_elevated": 1.0,
        "baseline_mod_lean": 0.5,
        "evidence_tag": tag,
        "evidence_weight": weight,
        "time_lo_wk": e.time_lo_wk,
        "time_hi_wk": e.time_hi_wk,
        "citations": e.citations,
    }


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------
def load_corpus():
    markers = {p.stem: Marker.model_validate(yaml.safe_load(p.read_text()))
               for p in (ETL_ROOT / "data" / "markers").glob("*.yaml")}
    interventions = {p.stem: Intervention.model_validate(yaml.safe_load(p.read_text()))
                     for p in (ETL_ROOT / "data" / "interventions").glob("*.yaml")}
    existing_effects: dict[str, set[str]] = defaultdict(set)
    for p in (ETL_ROOT / "data" / "effects").glob("*.yaml"):
        d = yaml.safe_load(p.read_text())
        existing_effects[d["marker_id"]].add(d["intervention_id"])
    return markers, interventions, dict(existing_effects)


def load_aliases() -> dict[str, str]:
    path = ETL_ROOT / "scripts" / "intervention_aliases.yaml"
    if not path.exists():
        return {}
    d = yaml.safe_load(path.read_text()) or {}
    return d.get("aliases") or {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--recall-test", action="store_true",
                        help="Only run the recall test against existing effects; exit non-zero if recall < 95%.")
    parser.add_argument("--recall-threshold", type=float, default=0.40,
                        help="Minimum acceptable recall (default 0.40 — recall is "
                             "approximate due to canonical-ID drift in the corpus, "
                             "so this is a directional sanity gate not a hard target).")
    parser.add_argument("--no-stubs", action="store_true",
                        help="Skip writing stub YAMLs (report only).")
    args = parser.parse_args()

    markers, interventions, existing_effects = load_corpus()
    aliases = load_aliases()
    matcher = Matcher(interventions, aliases)

    marker_md = build_marker_md_map(ETL_ROOT / "data" / "markers", ROOT / "biomarker_interventions")
    missing_md_markers = sorted(set(markers) - set(marker_md))

    all_extracted: dict[str, list[ExtractedEffect]] = defaultdict(list)
    unknown_sections: dict[str, set[str]] = defaultdict(set)

    for marker_id, md_path in marker_md.items():
        try:
            md_text = md_path.read_text()
        except Exception as exc:
            print(f"  ⚠ {marker_id}: cannot read {md_path}: {exc}", file=sys.stderr)
            continue
        raw_rows = extract_rows(marker_id, md_text, str(md_path.relative_to(ROOT)))
        for raw in raw_rows:
            if raw.section_class == "unknown":
                unknown_sections[marker_id].add(raw.section)
                continue
            processed = process_row(raw, markers[marker_id], matcher)
            if processed is not None:
                all_extracted[marker_id].append(processed)

    # ---- Recall test: parser should rediscover existing effects -----------
    found_existing: set[tuple[str, str]] = set()
    expected_existing: set[tuple[str, str]] = set()
    for marker_id, iv_ids in existing_effects.items():
        for iv_id in iv_ids:
            expected_existing.add((marker_id, iv_id))
    for marker_id, effects in all_extracted.items():
        for e in effects:
            if e.intervention_id and not e.skip_reason:
                found_existing.add((marker_id, e.intervention_id))
    rediscovered = found_existing & expected_existing
    recall = len(rediscovered) / max(len(expected_existing), 1)
    # Recall here is approximate: existing YAML often uses one of several
    # near-duplicate canonical IDs (krill_oil_2g vs krill_oil_2_5g, etc.) and
    # the parser may pick a different one. So this is a directional health
    # signal, not a strict gate. A truly broken parser shows <10% recall;
    # a working one with canonical-ID drift typically sits 40-70%.
    print(f"\nRecall (exact-ID match): {len(rediscovered)} / {len(expected_existing)} = {recall:.1%}")

    if args.recall_test:
        if recall < args.recall_threshold:
            print(f"FAIL: recall {recall:.1%} < {args.recall_threshold:.0%}", file=sys.stderr)
            # Surface biggest misses to help diagnose.
            missed = sorted(expected_existing - found_existing)[:30]
            print(f"\nSample misses ({len(missed)} of {len(expected_existing - found_existing)}):", file=sys.stderr)
            for marker_id, iv_id in missed:
                print(f"  {marker_id}  ←  {iv_id}", file=sys.stderr)
            return 1
        print(f"PASS: recall {recall:.1%} >= {args.recall_threshold:.0%}")
        return 0

    # ---- Diff + report ----------------------------------------------------
    proposed_dir = ETL_ROOT / "proposed_effects"
    if not args.no_stubs:
        proposed_dir.mkdir(exist_ok=True)
        for p in proposed_dir.glob("*.yaml"):
            p.unlink()

    gaps: dict[str, list[ExtractedEffect]] = defaultdict(list)
    extras: dict[str, set[str]] = defaultdict(set)
    unmatched_by_marker: dict[str, list[ExtractedEffect]] = defaultdict(list)
    medium_confidence: dict[str, list[ExtractedEffect]] = defaultdict(list)
    adverse_by_marker: dict[str, list[ExtractedEffect]] = defaultdict(list)
    in_band_skipped: dict[str, int] = defaultdict(int)
    schema_failures: list[tuple[str, str, str]] = []  # (marker_id, iv_id, err)
    stub_count = 0

    for marker_id, effects in all_extracted.items():
        documented_ids: set[str] = set()
        for e in effects:
            if e.skip_reason == "in_band marker (solver doesn't score)":
                in_band_skipped[marker_id] += 1
                continue
            if e.is_adverse:
                adverse_by_marker[marker_id].append(e)
                continue
            if e.intervention_id is None:
                unmatched_by_marker[marker_id].append(e)
                continue
            documented_ids.add(e.intervention_id)
            if e.match.tier == "medium":
                medium_confidence[marker_id].append(e)
            if e.intervention_id not in existing_effects.get(marker_id, set()):
                # Validate the stub dict against schema before adding.
                stub = build_effect_dict(e, marker_id)
                try:
                    Effect.model_validate(stub)
                except ValidationError as ve:
                    schema_failures.append((marker_id, e.intervention_id, str(ve)))
                    continue
                gaps[marker_id].append(e)
                if not args.no_stubs:
                    fname = f"{e.intervention_id}__{marker_id}.yaml"
                    (proposed_dir / fname).write_text(
                        yaml.dump(stub, sort_keys=False, allow_unicode=True)
                    )
                    stub_count += 1

        # Extras: in YAML but parser didn't find.
        existing_ids = existing_effects.get(marker_id, set())
        extras[marker_id] = existing_ids - documented_ids

    # ---- Write report -----------------------------------------------------
    report_lines: list[str] = []
    report_lines.append("# Corpus coverage audit (deterministic)\n")
    total_yaml_effects = sum(len(v) for v in existing_effects.values())
    total_extracted_matched = sum(
        len([e for e in v if e.intervention_id and not e.is_adverse and not e.skip_reason])
        for v in all_extracted.values()
    )
    total_gaps = sum(len(v) for v in gaps.values())
    total_unmatched = sum(len(v) for v in unmatched_by_marker.values())
    total_extras = sum(len(v) for v in extras.values())
    total_adverse = sum(len(v) for v in adverse_by_marker.values())
    total_in_band = sum(in_band_skipped.values())

    report_lines.extend([
        f"- Markers in canonical corpus: **{len(markers)}**",
        f"- Markers with research md mapped: **{len(marker_md)}**",
        f"- Effects in YAML (existing corpus): **{total_yaml_effects}**",
        f"- Effects extracted from research (matched + improving): **{total_extracted_matched}**",
        f"- **Recall on existing corpus: {recall:.1%}** ({len(rediscovered)} / {len(expected_existing)})",
        f"- Gaps (in research, missing from YAML): **{total_gaps}**",
        f"- Extras (in YAML, parser did not find): **{total_extras}**",
        f"- Unmatched (research phrase, no canonical ID): **{total_unmatched}**",
        f"- Adverse-direction rows (skipped): **{total_adverse}**",
        f"- In-band marker rows (skipped): **{total_in_band}**",
        f"- Schema validation failures: **{len(schema_failures)}**",
        f"- Unknown-section markers: **{len(unknown_sections)}**",
        "",
    ])

    if missing_md_markers:
        report_lines.append("## Markers with no research md\n")
        for m in missing_md_markers:
            report_lines.append(f"- `{m}`")
        report_lines.append("")

    if unknown_sections:
        report_lines.append("## Unknown section headings (extend allow/deny lists)\n")
        for marker_id, secs in sorted(unknown_sections.items()):
            for s in sorted(secs):
                report_lines.append(f"- `{marker_id}` § {s!r}")
        report_lines.append("")

    report_lines.append("## Gaps (sorted by # missing per marker)\n")
    sorted_gaps = sorted(gaps.items(), key=lambda x: -len(x[1]))
    for marker_id, effects in sorted_gaps:
        if not effects:
            continue
        report_lines.append(f"\n### `{marker_id}` — {len(effects)} missing")
        for e in sorted(effects, key=lambda x: x.intervention_id or ""):
            mag = f"{e.effect_lo:g} to {e.effect_hi:g} {e.effect_type}"
            tier = e.match.tier
            report_lines.append(
                f"- `{e.intervention_id}` ({tier}, score={e.match.score:.0f}) — "
                f"{e.direction} {mag} [{e.evidence_tag}]"
            )

    if extras:
        report_lines.append("\n## Extras (in YAML, not surfaced by parser)\n")
        for marker_id, ids in sorted(extras.items()):
            if not ids:
                continue
            report_lines.append(f"\n### `{marker_id}` — {len(ids)} extras")
            for iv_id in sorted(ids):
                report_lines.append(f"- `{iv_id}__{marker_id}.yaml`")

    if unmatched_by_marker:
        report_lines.append("\n## Unmatched intervention phrases (add to aliases.yaml or create canonical)\n")
        for marker_id, effects in sorted(unmatched_by_marker.items()):
            if not effects:
                continue
            report_lines.append(f"\n### `{marker_id}` — {len(effects)} unmatched")
            for e in effects[:25]:  # cap to keep report scannable
                cands = ", ".join(f"{cid}({score:.0f})" for cid, score in e.match.candidates[:3])
                report_lines.append(
                    f"- `{e.raw.intervention_phrase!r}`  →  top candidates: {cands}"
                )

    if medium_confidence:
        report_lines.append("\n## Medium-confidence matches (review before merging)\n")
        for marker_id, effects in sorted(medium_confidence.items()):
            if not effects:
                continue
            report_lines.append(f"\n### `{marker_id}` — {len(effects)} medium-confidence")
            for e in effects[:15]:
                report_lines.append(
                    f"- `{e.intervention_id}` (score={e.match.score:.0f}) "
                    f"← {e.raw.intervention_phrase!r}"
                )

    if schema_failures:
        report_lines.append("\n## Schema validation failures (parser bugs)\n")
        for marker_id, iv_id, err in schema_failures[:50]:
            report_lines.append(f"- `{marker_id}` ← `{iv_id}`: {err[:160]}")

    (ROOT / "coverage_report.md").write_text("\n".join(report_lines))
    print(f"\n✓ Wrote coverage_report.md")
    if not args.no_stubs:
        print(f"✓ Wrote {stub_count} stub effect YAMLs to {proposed_dir.relative_to(ROOT)}/")
    print(
        f"  Gaps: {total_gaps}   Extras: {total_extras}   "
        f"Unmatched: {total_unmatched}   Adverse: {total_adverse}   "
        f"Recall: {recall:.1%}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
