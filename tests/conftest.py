"""Shared pytest fixtures and config."""

from __future__ import annotations

from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    """Path to tests/fixtures (generic data only — no project-specific values)."""
    return FIXTURES_DIR
