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

## Eliciting the Idea Brief and Product Spec

The Idea Brief (Decide) and Product Spec (Specify) are produced *through a bounded interview with the founder*, not drafted unilaterally. The founder owns intent and the quality bar; the interviewer's job is to extract that judgment, ground it in a realistic and buildable direction, and converge it into testable criteria.

Use the interviewer stance from `bootstrap-interview.md` — probe vague answers, dig for intent, name gaps and contradictions, no flattery — with three additions specific to this stage:

- **Ground ambition in feasibility.** The founder advances and raises the idea; you convert that into the smallest buildable slice — surface constraints, cost, and what is technically load-bearing. Advance the idea *and* make it real.
- **Turn "good" into something checkable.** Help the founder set a high, concrete quality bar for this mission, then restate every "good" as an observable or machine-checkable acceptance criterion. Ambition in, testable criteria out — this is the steering wheel the agent builds toward.
- **Distill, don't transcribe.** Unlike the bootstrap interview (fidelity over brevity), here extract and refine. Keep it bounded: a few focused rounds, one question at a time; stop as soon as the artifact's fields are decision-grade. Respect the founder's time — do not pad.

Idea Brief — reach decision-grade answers that satisfy `definition_of_ready` in `ai-company.yaml`:

1. What outcome should this mission produce, for whom, and how will you know it worked?
2. What evidence makes it worth doing now — and what is still only a hypothesis?
3. What is the smallest slice worth building, and what is explicitly out of scope (non-goals)?
4. What is the riskiest assumption, and what would falsify it?

Product Spec — converge on:

1. Concretely, what can the user see or do that they cannot today (user-visible behavior)?
2. What must be true to count as done — each stated observably or machine-checkably (acceptance criteria)?
3. How must it behave on failure and at the edges (failure behavior, invariants)?
4. What quality bar applies here, and what is explicitly not in this spec (non-goals)?
5. Any security, privacy, billing, or rollback impact that needs a human gate?

Record answers in `templates/idea-brief.md` and `templates/product-spec.md`; both close with the founder's explicit approval.
