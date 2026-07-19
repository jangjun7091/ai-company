#!/usr/bin/env python3
"""Return the deterministic session mode for any LLM/coding environment."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FOUNDER_DOCS = [
    ROOT / "company/founder/vision.md",
    ROOT / "company/founder/customer-truth.md",
    ROOT / "company/founder/product-principles.md",
    ROOT / "company/founder/quality-bar.md",
    ROOT / "company/founder/human-escalation-policy.md",
]


def document_confirmed(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    return "Status: `confirmed`" in text and "<!-- Statements personally confirmed" not in text


def read_stage() -> str:
    path = ROOT / "company/state/project-state.yaml"
    if not path.exists():
        return "uninitialized"
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("stage:"):
            return line.split(":", 1)[1].strip()
    return "uninitialized"


def build_result() -> dict:
    stage = read_stage()
    missing = [str(p.relative_to(ROOT)) for p in FOUNDER_DOCS if not document_confirmed(p)]
    if stage == "uninitialized" or missing:
        return {
            "mode": "bootstrap_interview",
            "stage": stage,
            "missing_or_unconfirmed_founder_docs": missing,
            "instruction": "Follow company/workflows/bootstrap-interview.md. Ask one focused question at a time. Do not implement product code.",
        }
    return {
        "mode": "operating_loop",
        "stage": stage,
        "instruction": "Read current specs, decisions, review queues, and evidence. Propose the smallest valid next action under AGENTS.md.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()
    result = build_result()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Mode: {result['mode']}")
        print(f"Stage: {result['stage']}")
        if result.get("missing_or_unconfirmed_founder_docs"):
            print("Missing or unconfirmed founder documents:")
            for item in result["missing_or_unconfirmed_founder_docs"]:
                print(f"- {item}")
        print(result["instruction"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
