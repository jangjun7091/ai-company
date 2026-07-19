# Claude Code Adapter

Read and follow `AGENTS.md` as the canonical project operating contract.

At session start, run:

```bash
python scripts/session_start.py --json
```

Project-specific Claude skills are in `.claude/skills/`. They are adapters to the neutral workflows under `company/workflows/`; do not treat them as a separate source of truth.
