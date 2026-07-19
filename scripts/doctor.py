#!/usr/bin/env python3
"""Validate the repository operating contract.

Checks: required contract files exist, schema files parse as JSON, state
values use the vocabularies defined in ai-company.yaml, and agent contracts
use the escalation trigger enum from the escalation schema.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "README.md",
    "CLAUDE.md",
    "ai-company.yaml",
    ".github/copilot-instructions.md",
    ".cursor/rules/ai-company.mdc",
    "company/founder/vision.md",
    "company/founder/customer-truth.md",
    "company/founder/product-principles.md",
    "company/founder/quality-bar.md",
    "company/founder/human-escalation-policy.md",
    "company/workflows/bootstrap-interview.md",
    "company/workflows/idea-to-release.md",
    "company/workflows/incident-to-learning.md",
    "company/workflows/weekly-operating-review.md",
    "company/state/project-state.yaml",
    "company/state/company-state.yaml",
    "company/schemas/task.schema.json",
    "company/schemas/decision.schema.json",
    "company/schemas/escalation.schema.json",
    "company/schemas/evidence.schema.json",
    "templates/task.md",
    "templates/human-assistance-request.md",
    "templates/evidence.md",
    "templates/learning-entry.md",
]


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def yaml_scalar(lines: list[str], key: str) -> str | None:
    """Value of the first `key: value` line, tolerating quotes and comments.

    Deliberately naive: the state files this repo machine-reads are flat
    `key: value` documents, which keeps the scripts dependency-free.
    """
    prefix = key + ":"
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(prefix):
            value = stripped[len(prefix):].split("#", 1)[0].strip().strip("'\"")
            return value or None
    return None


def yaml_block_list(lines: list[str], header: str) -> list[str]:
    """Items of the `- item` list directly under a `header:` line.

    The header must match the stripped line exactly (so `stages:` never
    matches `portfolio_stages:`). Comment lines inside the list are
    skipped; a blank line or any other content ends the list.
    """
    items: list[str] = []
    collecting = False
    for line in lines:
        stripped = line.strip()
        if collecting:
            if stripped.startswith("- "):
                items.append(stripped[2:].split("#", 1)[0].strip().strip("'\""))
                continue
            if stripped.startswith("#"):
                continue
            break
        if stripped == header:
            collecting = True
    return items


def collect_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (root / relative).exists():
            errors.append(f"missing: {relative}")

    schema_dir = root / "company" / "schemas"
    if schema_dir.exists():
        for schema in sorted(schema_dir.glob("*.json")):
            try:
                json.loads(schema.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(
                    f"invalid JSON {schema.relative_to(root).as_posix()}: {exc}"
                )

    stages: list[str] = []
    portfolio_stages: list[str] = []
    manifest = root / "ai-company.yaml"
    if manifest.exists():
        lines = read_lines(manifest)
        stages = yaml_block_list(lines, "stages:")
        portfolio_stages = yaml_block_list(lines, "portfolio_stages:")
        if not stages:
            errors.append("ai-company.yaml: lifecycle stages list not found")

    project_state = root / "company" / "state" / "project-state.yaml"
    if project_state.exists() and stages:
        stage = yaml_scalar(read_lines(project_state), "stage")
        if stage is None:
            errors.append("company/state/project-state.yaml: no stage value")
        elif stage not in stages:
            errors.append(
                "company/state/project-state.yaml: "
                f"stage '{stage}' is not one of {stages}"
            )

    company_state = root / "company" / "state" / "company-state.yaml"
    if company_state.exists() and portfolio_stages:
        portfolio = yaml_scalar(read_lines(company_state), "portfolio_stage")
        if portfolio is not None and portfolio not in portfolio_stages:
            errors.append(
                "company/state/company-state.yaml: "
                f"portfolio_stage '{portfolio}' is not one of {portfolio_stages}"
            )

    escalation_schema = root / "company" / "schemas" / "escalation.schema.json"
    agents_dir = root / "company" / "agents"
    if escalation_schema.exists() and agents_dir.exists():
        try:
            allowed = set(
                json.loads(escalation_schema.read_text(encoding="utf-8"))
                ["properties"]["trigger"]["enum"]
            )
        except (json.JSONDecodeError, KeyError, TypeError):
            allowed = set()
            errors.append(
                "company/schemas/escalation.schema.json: trigger enum not readable"
            )
        for contract in sorted(agents_dir.glob("*.yaml")):
            if not allowed:
                break
            rel = contract.relative_to(root).as_posix()
            triggers = yaml_block_list(read_lines(contract), "mandatory_escalation:")
            if not triggers:
                errors.append(f"{rel}: mandatory_escalation list missing or empty")
                continue
            unknown = [t for t in triggers if t not in allowed]
            if unknown:
                errors.append(
                    f"{rel}: mandatory_escalation values not in the escalation "
                    f"schema trigger enum: {unknown}"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()
    errors = collect_errors()
    if args.json:
        payload = {"status": "fail" if errors else "pass", "errors": errors}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    elif errors:
        print("AI Company doctor: FAIL")
        for error in errors:
            print(f"- {error}")
    else:
        print("AI Company doctor: PASS")
        print("Next: python scripts/session_start.py --json")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
