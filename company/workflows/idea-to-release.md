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

## Producing the Idea Brief and Product Spec

The Idea Brief (Decide) and Product Spec (Specify) are the two artifacts the agent builds toward, so the founder's judgment must be in them — but they are produced differently:

- The **Idea Brief is elicited** through a bounded founder interview: its intent, bet, non-goals, and riskiest assumption exist only in the founder's head, so they must be drawn out.
- The **Product Spec is derived**: the agent drafts it from the approved Idea Brief and the founder documents (especially `quality-bar.md`), then the founder ratifies the load-bearing few. Do not re-interview what the draft can derive.

The founder owns intent and the quality bar; the agent extracts or derives that judgment, grounds it in a realistic and buildable direction, and converges it into testable criteria.

Use the interviewer stance from `bootstrap-interview.md` — probe vague answers, dig for intent, name gaps and contradictions, no flattery — for the Idea Brief interview and for the few ratification questions the Spec draft surfaces, with these additions specific to this stage:

- **Ground ambition in feasibility.** The founder advances and raises the idea; you convert that into the smallest buildable slice — surface constraints, cost, and what is technically load-bearing. Advance the idea *and* make it real.
- **Turn "good" into something checkable.** Help the founder set a high, concrete quality bar for this mission — specific enough that the Spec draft can restate every "good" as an observable or machine-checkable acceptance criterion. Ambition in, testable criteria out: the interview captures the bar; the derived Spec turns it into the steering wheel the agent builds toward.
- **Distill, don't transcribe.** Unlike the bootstrap interview (fidelity over brevity), here extract and refine. Keep it bounded: a few focused rounds, one question at a time; stop as soon as the artifact's fields are decision-grade. Respect the founder's time — do not pad.
- **Hold altitude — the founder owns intent, the agent owns mechanism.** The Idea Brief is what/why, the bet, non-goals, and the riskiest assumption; mechanism and implementation choices (algorithms, internal structure, how a check is met) belong to the Spec and Build phases. If the founder volunteers implementation detail, capture the *intent* behind it and defer the mechanism — park it in `docs/decisions/` (status `deferred`), as in the bootstrap interview — do not deepen the interview to match. Say what resolution you need: a decision-grade answer, often a single line, is complete — so the founder neither over-specifies (which anchors the agent and wastes their time) nor under-specifies (which yields confident-wrong output).

Idea Brief — reach decision-grade answers that satisfy `definition_of_ready` in `ai-company.yaml`:

1. What outcome should this mission produce, for whom, and how will you know it worked?
2. What evidence makes it worth doing now — and what is still only a hypothesis?
3. What is the smallest slice worth building, and what is explicitly out of scope (non-goals)?
4. What is the riskiest assumption, and what would falsify it?

Product Spec — the agent drafts from the Idea Brief and founder documents; the founder ratifies. The draft settles, and the founder confirms:

1. What the user can see or do that they cannot today (user-visible behavior).
2. What must be true to count as done — each stated observably or machine-checkably (acceptance criteria). Surface any threshold the agent had to choose (for example, a hit-rate bar) for the founder to ratify; never bury a guessed "good".
3. How it must behave on failure and at the edges (failure behavior, invariants).
4. The quality bar that applies, and what is explicitly out of this spec (non-goals).
5. Any security, privacy, billing, or rollback impact that needs a human gate.

The founder need not author these — review and correct the draft, and explicitly confirm 2, 4, and 5. Ask only where the Idea Brief left "good" underdetermined; otherwise derive.

The Idea Brief is recorded from the interview using `templates/idea-brief.md`; the Product Spec is drafted using `templates/product-spec.md` and then ratified. Both live in the mission's folder under `docs/specs/` (see `docs/specs/README.md`) and close with the founder's explicit approval.

## Executing build tasks

Build tasks may be delegated to workers — any agent that reads `AGENTS.md`, whether a subagent or an external CLI. One orchestrator owns the plan and the task split; workers execute scoped tasks. Keep delegation safe and verifiable:

- **One task, tight scope.** Hand a worker a single task file with explicit allowed and forbidden scope, not a whole feature. A headless worker cannot be steered mid-run, so the scope is the control.
- **Isolate the work.** Each worker runs on its own branch or worktree, so parallel runs cannot collide and every change is reversible.
- **Least privilege.** Grant the minimum access the task needs — read-only for review or verification, write only for implementation. Do not disable the sandbox except inside a disposable, isolated runner.
- **Verify before merge.** The orchestrator re-runs the repository checks and the acceptance criteria against the worker's diff before merging. A worker's own success report is not evidence.
- **Keep the human gates.** Irreversible or outward-facing actions (production, publishing, external spend at scale, credential or access expansion) stay at the human gate even when workers otherwise run unattended.
