#!/usr/bin/env python3
"""Return the deterministic session mode for any LLM/coding environment."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FOUNDER_DOC_NAMES = [
    "vision.md",
    "customer-truth.md",
    "product-principles.md",
    "quality-bar.md",
    "human-escalation-policy.md",
]
# Accepts "Status: confirmed", "Status: `confirmed`", any casing.
STATUS_RE = re.compile(r"^status\s*:\s*`?([a-z_]+)`?\s*$", re.IGNORECASE)
NEXT_STAGE_AFTER_BOOTSTRAP = "discovery"

BOOTSTRAP_INSTRUCTION = (
    "Follow company/workflows/bootstrap-interview.md. Ask one focused question "
    "at a time. Do not implement product code."
)
OPERATING_INSTRUCTION = (
    "Read current specs, decisions, review queues, and evidence. Propose the "
    "smallest valid next action under AGENTS.md."
)


def founder_docs(root: Path = ROOT) -> list[Path]:
    return [root / "company" / "founder" / name for name in FOUNDER_DOC_NAMES]


def document_status(path: Path) -> str:
    """Status declared by the document's `Status:` line.

    Returns the lowercased status value, "missing" when the file does not
    exist, or "unknown" when no parseable `Status:` line is present.
    """
    if not path.exists():
        return "missing"
    for line in path.read_text(encoding="utf-8").splitlines():
        match = STATUS_RE.match(line.strip())
        if match:
            return match.group(1).lower()
    return "unknown"


def document_confirmed(path: Path) -> bool:
    return document_status(path) == "confirmed"


def read_stage(root: Path = ROOT) -> str:
    path = root / "company" / "state" / "project-state.yaml"
    if not path.exists():
        return "uninitialized"
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("stage:"):
            value = stripped.split(":", 1)[1].split("#", 1)[0].strip().strip("'\"")
            return value or "uninitialized"
    return "uninitialized"


def build_result(root: Path = ROOT) -> dict:
    stage = read_stage(root)
    statuses = {
        path.relative_to(root).as_posix(): document_status(path)
        for path in founder_docs(root)
    }
    missing = [doc for doc, status in statuses.items() if status != "confirmed"]
    bootstrap = stage == "uninitialized" or bool(missing)
    exit_steps: list[str] = []
    if bootstrap:
        exit_steps = [
            "Complete each unconfirmed founder document with the founder, then "
            "change its 'Status:' line to 'Status: confirmed'.",
            "Set 'stage:' in company/state/project-state.yaml from "
            f"'uninitialized' to '{NEXT_STAGE_AFTER_BOOTSTRAP}' (the next "
            "lifecycle stage in ai-company.yaml).",
            "Re-run 'python scripts/session_start.py --json' and confirm the "
            "mode is operating_loop.",
        ]
    return {
        "mode": "bootstrap_interview" if bootstrap else "operating_loop",
        "stage": stage,
        "founder_docs": statuses,
        "missing_or_unconfirmed_founder_docs": missing,
        "instruction": BOOTSTRAP_INSTRUCTION if bootstrap else OPERATING_INSTRUCTION,
        "exit_steps": exit_steps,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()
    result = build_result()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Mode: {result['mode']}")
        print(f"Stage: {result['stage']}")
        print("Founder documents:")
        for doc, status in result["founder_docs"].items():
            print(f"- {doc}: {status}")
        if result["exit_steps"]:
            print("To leave bootstrap mode:")
            for index, step in enumerate(result["exit_steps"], start=1):
                print(f"{index}. {step}")
        print(result["instruction"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
