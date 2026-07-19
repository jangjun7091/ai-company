# Contributing

This template is intentionally small, dependency-free, and agent-neutral. Contributions that preserve those properties are welcome.

## Ground rules

- `AGENTS.md` is the canonical operating contract. Vendor adapters stay thin and must not duplicate or weaken it.
- `scripts/` must remain Python standard library only.
- Shipped documents stay generic — company-specific content belongs in repositories created *from* the template.

## Before opening a pull request

```bash
python scripts/doctor.py
python -m unittest discover -s tests -p "test_*.py"
```

Both must pass. If you change contract files (manifest, schemas, agent contracts, state layout), update `scripts/doctor.py` and the tests with them.

## Proposing changes

Open an issue using the feature or bug form, or send a pull request using the PR template. Keep changes small and explain the failure or friction that motivated them.
