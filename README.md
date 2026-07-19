# AI Company Starter

A model- and tool-neutral operating template for a founder working with AI teammates from problem discovery through production learning.

## Core idea

The repository is the source of truth. Codex, Claude Code, Copilot, Cursor, Goose, OpenHands, or future agents are replaceable execution environments.

The operating loop is:

`Discover → Decide → Specify → Build → Verify → Release → Observe → Learn`

## Start a new project

```bash
git clone <your-template-repository> my-product
cd my-product
python scripts/session_start.py
```

Then open the repository in your preferred coding agent and say:

> Start the company workflow. Follow AGENTS.md and the session-start output. Do not write product code until the bootstrap interview and Definition of Ready are complete.

## Rules

1. Founder truth, product decisions, specifications, tests, evidence, and learnings live in Git.
2. Vendor-specific files are adapters, never the canonical source.
3. Agents propose and execute; the founder owns vision, customer truth, quality, risk, and irreversible decisions.
4. Production incidents and user feedback must become reproducible evidence, evaluations, or updated operating rules.
5. Stronger models do not bypass scope, evidence, approval, or quality gates.

## Repository map

- `AGENTS.md` — canonical instructions for all agents.
- `ai-company.yaml` — operating manifest and gates.
- `company/founder/` — founder-owned source of truth.
- `company/agents/` — role contracts independent of LLM model.
- `company/workflows/` — repeatable company workflows.
- `company/schemas/` — typed handoff contracts.
- `company/state/` — current lifecycle state.
- `templates/` — reusable artifacts.
- `docs/` — specs, decisions, runbooks, and learnings.
- `adapters/` and tool-specific folders — thin compatibility layers.
- `scripts/` — deterministic checks that do not depend on an LLM.

## Recommended adoption order

1. Bootstrap interview and founder documents.
2. One feature through Idea Brief → Spec → Task → PR → Verification.
3. Production telemetry and feedback ingestion.
4. Incident-to-learning loop.
5. Multiple agent roles and an orchestration/control-center runtime.

## License

No license is included by default. Choose one before publishing the repository publicly.
