#!/usr/bin/env python3
"""Validate that the AI Company repository contract is present and internally coherent."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "ai-company.yaml",
    "company/workflows/bootstrap-interview.md",
    "company/workflows/idea-to-release.md",
    "company/state/project-state.yaml",
    "company/schemas/task.schema.json",
    "company/schemas/decision.schema.json",
    "company/schemas/escalation.schema.json",
]


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).exists():
            errors.append(f"missing: {relative}")
    for schema in (ROOT / "company/schemas").glob("*.json"):
        try:
            json.loads(schema.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {schema.relative_to(ROOT)}: {exc}")
    if errors:
        print("AI Company doctor: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("AI Company doctor: PASS")
    print("Next: python scripts/session_start.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
