# Idea to Release

The canonical operating loop is the eight-step loop in `ai-company.yaml`
(`discover → decide → specify → build → verify → release → observe → learn`).
**Plan** and **Task** below are sub-phases between Specify and Build.

1. **Discover** — gather customer evidence and define the problem.
2. **Decide** — founder approves priority, desired outcome, non-goals, and risk boundary.
3. **Specify** — produce a Product Spec with testable acceptance criteria.
4. **Plan** — identify architecture impact, alternatives, dependencies, and rollback.
5. **Task** — split into minimal vertical slices with explicit allowed scope.
6. **Build** — work on isolated branches or worktrees; preserve traceable artifacts.
7. **Verify** — independent checks against acceptance criteria and regression suite.
8. **Release** — use feature flags, staged rollout, or another containment mechanism when relevant.
9. **Observe** — collect product, reliability, cost, and customer signals.
10. **Learn** — convert evidence into decisions, tests, skills, runbooks, or rejected hypotheses.

State updates in `company/state/project-state.yaml`:

| Step | Update |
| --- | --- |
| Discover | `stage: discovery` |
| Decide | `stage: definition`, `current_mission` (approved Idea Brief) |
| Specify | `active_spec` (Product Spec path) |
| Build | `stage: build` |
| Verify | `stage: verification`, `last_verified_commit` |
| Release | `stage: release_candidate` then `production`, `last_production_release` |
| Learn | `stage: learning`, plus an entry in `docs/learning/` using `templates/learning-entry.md` |

No phase may declare itself complete solely through an agent's prose assertion.
