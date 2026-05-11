"""Tests for scripts/consolidate.py — intervention ID merge tool."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

# Make scripts/ importable
SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from consolidate import consolidate  # noqa: E402


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


@pytest.fixture
def fake_data_dir(tmp_path: Path) -> Path:
    """A minimal data/ tree with two interventions and a few effects."""
    data = tmp_path / "data"
    (data / "effects").mkdir(parents=True)
    (data / "interventions").mkdir(parents=True)
    (data / "markers").mkdir(parents=True)

    # Intervention to be removed
    _write_yaml(
        data / "interventions" / "old_id.yaml",
        {"id": "old_id", "canonical_name": "Old", "type": "supplement",
         "dose_amount": 1, "dose_unit": "g_per_day"},
    )
    # Intervention to keep
    _write_yaml(
        data / "interventions" / "new_id.yaml",
        {"id": "new_id", "canonical_name": "New", "type": "supplement",
         "dose_amount": 1000, "dose_unit": "mg_per_day"},
    )

    # Effect referencing old_id (will be renamed + rewritten)
    _write_yaml(
        data / "effects" / "old_id__apob.yaml",
        {"intervention_id": "old_id", "marker_id": "apob",
         "direction": "decrease", "effect_type": "pct",
         "effect_lo": -10, "effect_hi": -5},
    )
    # Effect referencing old_id on a second marker
    _write_yaml(
        data / "effects" / "old_id__ldl_c.yaml",
        {"intervention_id": "old_id", "marker_id": "ldl_c",
         "direction": "decrease", "effect_type": "pct",
         "effect_lo": -8, "effect_hi": -3},
    )
    # Unrelated effect — should not change
    _write_yaml(
        data / "effects" / "other_iv__apob.yaml",
        {"intervention_id": "other_iv", "marker_id": "apob",
         "direction": "decrease", "effect_type": "pct",
         "effect_lo": -5, "effect_hi": -2},
    )

    return data


def test_rewrites_intervention_id_in_effect_files(fake_data_dir: Path) -> None:
    consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")

    # The renamed effect should have intervention_id == new_id
    new_effect = yaml.safe_load(
        (fake_data_dir / "effects" / "new_id__apob.yaml").read_text()
    )
    assert new_effect["intervention_id"] == "new_id"


def test_renames_effect_files(fake_data_dir: Path) -> None:
    consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")

    # New filenames exist
    assert (fake_data_dir / "effects" / "new_id__apob.yaml").exists()
    assert (fake_data_dir / "effects" / "new_id__ldl_c.yaml").exists()
    # Old filenames gone
    assert not (fake_data_dir / "effects" / "old_id__apob.yaml").exists()
    assert not (fake_data_dir / "effects" / "old_id__ldl_c.yaml").exists()


def test_deletes_old_intervention_yaml(fake_data_dir: Path) -> None:
    consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")
    assert not (fake_data_dir / "interventions" / "old_id.yaml").exists()


def test_keeps_new_intervention_yaml(fake_data_dir: Path) -> None:
    consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")
    assert (fake_data_dir / "interventions" / "new_id.yaml").exists()


def test_unrelated_effects_untouched(fake_data_dir: Path) -> None:
    consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")
    untouched = yaml.safe_load(
        (fake_data_dir / "effects" / "other_iv__apob.yaml").read_text()
    )
    assert untouched["intervention_id"] == "other_iv"


def test_errors_when_target_filename_conflict(fake_data_dir: Path) -> None:
    """If new_id__marker.yaml already exists, rename would clobber — must error."""
    _write_yaml(
        fake_data_dir / "effects" / "new_id__apob.yaml",
        {"intervention_id": "new_id", "marker_id": "apob",
         "direction": "decrease", "effect_type": "pct",
         "effect_lo": -8, "effect_hi": -4},
    )
    with pytest.raises(FileExistsError):
        consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")


def test_errors_when_new_intervention_missing(fake_data_dir: Path) -> None:
    (fake_data_dir / "interventions" / "new_id.yaml").unlink()
    with pytest.raises(FileNotFoundError):
        consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")


def test_errors_when_old_intervention_missing(fake_data_dir: Path) -> None:
    (fake_data_dir / "interventions" / "old_id.yaml").unlink()
    with pytest.raises(FileNotFoundError):
        consolidate(data_dir=fake_data_dir, old_id="old_id", new_id="new_id")
