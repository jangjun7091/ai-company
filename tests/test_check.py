"""Tests for scripts/check.py.

These use throwaway subprocess checks (a Python one-liner that passes or
exits non-zero), never the real doctor/unittest run, so they stay fast and
cannot recurse into themselves.
"""
from __future__ import annotations

from pathlib import Path
import contextlib
import importlib.util
import io
import sys
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check.py"
spec = importlib.util.spec_from_file_location("check_module", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

PASS = [sys.executable, "-c", "pass"]
FAIL = [sys.executable, "-c", "import sys; sys.exit(3)"]


def run_quiet(checks: list[tuple[str, list[str]]]) -> int:
    """run_checks with its progress output swallowed, so passing tests do not
    print 'FAIL: boom' into the suite's log."""
    with contextlib.redirect_stdout(io.StringIO()):
        return module.run_checks(checks, Path.cwd())


class RunChecksTest(unittest.TestCase):
    def test_all_pass_returns_zero(self) -> None:
        self.assertEqual(run_quiet([("noop", PASS)]), 0)

    def test_a_failing_check_returns_one(self) -> None:
        self.assertEqual(run_quiet([("boom", FAIL)]), 1)

    def test_one_failure_among_passes_still_fails(self) -> None:
        self.assertEqual(run_quiet([("ok", PASS), ("boom", FAIL)]), 1)

    def test_ships_the_two_guardrails(self) -> None:
        names = [name for name, _ in module.CHECKS]
        self.assertEqual(names, ["doctor", "tests"])


if __name__ == "__main__":
    unittest.main()
