"""Tests for the ghostwire package version."""

import re

from ghostwire import __version__


def test_version_is_valid_semver() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+", __version__) is not None