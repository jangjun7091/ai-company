# Environment Adapters

The canonical company logic lives in `AGENTS.md`, `ai-company.yaml`, `company/workflows/`, and schemas.

Adapters should only:

- Tell a specific environment where canonical files are.
- Expose neutral workflows as that environment's commands or skills.
- Configure safe deterministic hooks.
- Map environment-specific tool names to neutral capabilities.

Adapters must not duplicate or weaken founder authority, permissions, escalation triggers, or verification gates.

Adapter files live at each tool's native location (`AGENTS.md`, `CLAUDE.md`, `.claude/`, `.github/copilot-instructions.md`, `.cursor/`); this folder only documents the pattern.

Included examples:

- Codex: reads `AGENTS.md` directly.
- Claude Code: `CLAUDE.md` plus thin skills.
- GitHub Copilot: `.github/copilot-instructions.md`.
- Cursor: `.cursor/rules/ai-company.mdc`.
