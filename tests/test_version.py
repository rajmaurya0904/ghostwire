"""Tests for the ghostwire package version module."""

from ghostwire import __version__
from ghostwire.version import __version__ as version_module_version


def test_version_is_non_empty_string() -> None:
    assert isinstance(__version__, str)
    assert __version__.strip()


def test_version_matches_module_attribute() -> None:
    assert __version__ == version_module_version


def test_version_follows_semver_pattern() -> None:
    parts = __version__.split(".")
    assert len(parts) == 3
    for part in parts:
        assert part.isdigit()
