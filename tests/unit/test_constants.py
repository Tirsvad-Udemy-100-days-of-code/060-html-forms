"""!
@file test_constants.py
@brief Smoke test: the package imports and its constants are consistent.
"""

import tomllib
from pathlib import Path

from html_forms import constants


def test_version_matches_pyproject() -> None:
    """!@brief The version constant equals the version in pyproject.toml."""
    pyproject = Path(__file__).parents[2] / "pyproject.toml"
    data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    assert constants.APP_VERSION == data["project"]["version"]


def test_ports_are_different() -> None:
    """!@brief The demo and the blog can run side by side."""
    assert constants.DEMO_PORT != constants.BLOG_PORT
