"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import ghostwire


def test_version_is_set() -> None:
    assert ghostwire.__version__
