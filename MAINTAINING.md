# Maintaining this template

> Scope: this file governs the **ai-company template itself**. If you created a
> repository *from* the template, delete `MAINTAINING.md` and `ROADMAP.md` — they
> are not part of your company.

The point of this file: any future session — a new chat, a different agent, a
different model — can open this repository and continue improving it without the
previous conversation. The state lives in Git, issues, and the roadmap, never in
chat history.

## Prime directive

Keep this a template people want to fork and star: small, honest, dependency-free,
and genuinely useful on the first try. Every change should make the *first hour*
with the template better.

## Design invariants (do not break these)

1. **Scripts stay Python standard library only.** Zero install steps is a feature.
2. **`AGENTS.md` is the canonical contract.** Vendor adapters (`CLAUDE.md`,
   `.claude/`, `.cursor/`, `.github/copilot-instructions.md`) stay thin and never
   duplicate or weaken it. Model-neutrality binds the operating contract
   (`AGENTS.md`, `company/`, `templates/`, `docs/`); the README's adapter list
   and historical provenance notes in `ROADMAP.md`/`CHANGELOG.md` may name
   vendors.
3. **Template body documents are English.** Korean lives only in `README.ko.md`.
4. **Every commit keeps the guardrails green:** `python scripts/doctor.py` and the
   unittest suite pass. CI enforces this on every push and PR.
5. **The template ships generic.** Company-specific content belongs in repositories
   created *from* the template, never here.
6. **`ai-company.yaml` `version` is the single source of truth** for the template
   version. Follow [SemVer](https://semver.org/).

## Resume in a new session

Run these to reconstruct context, then work one issue at a time:

```bash
# 1. Where the template stands
git log --oneline -15
cat ROADMAP.md

# 2. What is planned next — the current milestone is ROADMAP.md's "Next:" heading
gh issue list --repo jangjun7091/ai-company --milestone "<current milestone, e.g. the ROADMAP Next version>"

# 3. Pick the top unblocked issue, then:
git switch -c feat/<short-slug>          # one issue per branch, one behavior per change
#    ... make the change ...
python scripts/doctor.py                  # must pass
python -m unittest discover -s tests -p "test_*.py"   # must pass
#    ... update CHANGELOG.md under [Unreleased] ...
git commit -am "..." && git push -u origin HEAD
gh pr create --fill                       # link the issue with "Closes #N"
```

Merge when CI is green. When a milestone's issues are all merged, cut a release
(below). That is the whole loop — repeatable forever, session-independent.

## Cutting a release

1. Move the `[Unreleased]` section of `CHANGELOG.md` under a new
   `[x.y.z] - YYYY-MM-DD` heading.
2. Bump `version` in `ai-company.yaml` to the full SemVer `x.y.z` — `0.4.0`,
   not `0.4` — (and agent contract versions if their contracts changed).
   Releases before 0.4.0 wrote `X.Y`; normalize when you touch the field.
3. Commit: `Release vX.Y.Z`.
4. Tag and publish:
   ```bash
   gh release create vX.Y.Z --title "vX.Y.Z" --notes-from-tag
   # or paste the CHANGELOG section as --notes
   ```
5. Update `ROADMAP.md`: mark the shipped version done, open the next milestone.

## Growing an audience (stars and contributors)

- Keep an inviting set of `good first issue` items open at all times.
- Reply to issues and PRs quickly; a responsive repo attracts contributors.
- Announce each release (README badge updates automatically) and link the roadmap
  so people see momentum.
- The best marketing is a template that works on the first `python scripts/session_start.py`.
