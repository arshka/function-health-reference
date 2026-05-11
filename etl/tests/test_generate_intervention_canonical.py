"""Tests for scripts/generate_intervention_canonical.py."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from generate_intervention_canonical import generate  # noqa: E402


def _write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_generates_sorted_id_name_type_entries(tmp_path: Path) -> None:
    interventions = tmp_path / "interventions"
    _write(interventions / "psyllium_husk_10g.yaml",
           {"id": "psyllium_husk_10g", "canonical_name": "Psyllium husk",
            "type": "supplement", "dose_amount": 10, "dose_unit": "g_per_day"})
    _write(interventions / "evoo_30ml.yaml",
           {"id": "evoo_30ml", "canonical_name": "Extra virgin olive oil",
            "type": "food", "dose_amount": 30, "dose_unit": "ml_per_day"})

    out = tmp_path / "canonical" / "interventions.yaml"
    generate(interventions_dir=interventions, output_path=out)

    parsed = yaml.safe_load(out.read_text())
    ids = [e["id"] for e in parsed["interventions"]]
    assert ids == ["evoo_30ml", "psyllium_husk_10g"]  # sorted
    psyllium = next(e for e in parsed["interventions"] if e["id"] == "psyllium_husk_10g")
    assert psyllium["canonical_name"] == "Psyllium husk"
    assert psyllium["type"] == "supplement"
    # Should not include dose_amount, dose_unit, mechanisms, etc.
    assert set(psyllium.keys()) == {"id", "canonical_name", "type"}


def test_skips_files_without_id(tmp_path: Path) -> None:
    interventions = tmp_path / "interventions"
    _write(interventions / "good.yaml",
           {"id": "good", "canonical_name": "Good", "type": "food"})
    _write(interventions / "broken.yaml", {})  # no id

    out = tmp_path / "canonical" / "interventions.yaml"
    generate(interventions_dir=interventions, output_path=out)

    parsed = yaml.safe_load(out.read_text())
    assert [e["id"] for e in parsed["interventions"]] == ["good"]


def test_creates_output_directory(tmp_path: Path) -> None:
    interventions = tmp_path / "interventions"
    _write(interventions / "x.yaml",
           {"id": "x", "canonical_name": "X", "type": "food"})

    out = tmp_path / "deep" / "nested" / "interventions.yaml"
    generate(interventions_dir=interventions, output_path=out)
    assert out.exists()
