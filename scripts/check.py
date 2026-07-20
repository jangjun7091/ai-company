#!/usr/bin/env python3
"""Run the template's guardrails without GNU Make.

Windows — and any machine without ``make`` — can verify the repository with a
single command: ``python scripts/check.py``. It runs the same two guardrails as
``make doctor`` and ``make test`` (the contract check and the unittest suite)
and exits non-zero if either fails, so it is safe to wire into CI or a pre-push
hook.

Standard library only, to preserve the zero-install invariant.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Mirror the Makefile's `doctor` and `test` targets, invoked through the same
# interpreter that runs this script (correct on Windows, where `python` may not
# be the intended one).
CHECKS = [
    ("doctor", [sys.executable, "scripts/doctor.py"]),
    (
        "tests",
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
    ),
]


def run_checks(checks: list[tuple[str, list[str]]], cwd: Path) -> int:
    """Run each named check in cwd; return 0 if all pass, 1 otherwise."""
    failed: list[str] = []
    for name, cmd in checks:
        print(f"==> {name}: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=cwd)
        if result.returncode != 0:
            failed.append(name)
        print()

    if failed:
        print(f"FAIL: {', '.join(failed)}")
        return 1
    print("OK: all checks passed")
    return 0


def main() -> int:
    return run_checks(CHECKS, REPO_ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
