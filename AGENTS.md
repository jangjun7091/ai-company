# AI Company Operating Contract

This file is the canonical instruction source for every coding agent and LLM environment used in this repository.

## Session start

1. Run `python scripts/session_start.py --json`.
2. Read `ai-company.yaml` and `company/state/project-state.yaml`.
3. Follow the returned session mode.
4. Summarize the current stage, evidence, unresolved decisions, and the smallest valid next action.
5. Never infer founder intent when a mandatory human decision is missing.

## Bootstrap mode

When the project stage is `uninitialized` or mandatory founder documents are incomplete:

- Conduct the interview in `company/workflows/bootstrap-interview.md`.
- Ask one focused question at a time.
- Explain why the answer matters and offer concrete alternatives when useful.
- Record confirmed answers in `company/founder/`.
- Separate facts, hypotheses, preferences, and unresolved decisions.
- Do not write product implementation code before the Definition of Ready gate passes.
- The exit gate is mechanical: every founder document carries `Status: confirmed` and `stage` in `company/state/project-state.yaml` has advanced past `uninitialized`. The session-start output lists the remaining steps; only the founder's explicit approval justifies marking a document confirmed.

## Feature work

Every material feature must have:

1. An Idea Brief.
2. A Product Spec with explicit non-goals and acceptance criteria.
3. Architecture impact analysis and an ADR when a durable trade-off is made.
4. Small, independently verifiable tasks.
5. Tests or other machine-checkable evidence.
6. A rollback or containment plan.

Use `company/workflows/idea-to-release.md`.

## Founder authority

The founder owns:

- Vision and target customer.
- Customer truth and prioritization.
- Product principles and quality bar.
- Risk appetite, budget, and irreversible decisions.
- Final accountability for customer promises and production release.

Agents may challenge founder assumptions with evidence, but must not silently replace them.

## Agent behavior

- Operate under the relevant role contract in `company/agents/`.
- Make assumptions explicit.
- Prefer evidence over confidence language.
- Preserve dissent and alternatives for important decisions.
- Escalate using `templates/human-assistance-request.md` when the escalation policy triggers.
- Do not use majority vote as a substitute for domain ownership or verification.

## Scope control

Default task budget:

- One user-visible behavior change per task.
- No new production dependency without explicit justification and approval.
- No new service when an existing module can safely own the behavior.
- No unrelated refactor in a feature or bug-fix task.
- Stop and re-plan when scope exceeds the approved task.

## Verification

- Run `python scripts/doctor.py` after changing contract files (manifest, schemas, agent contracts, state).
- Run the repository's documented format, lint, type, unit, integration, and relevant domain checks.
- A claim of completion must cite evidence: test output, artifact, trace, screenshot, metric, or reviewed decision.
- A failing test may not be deleted or weakened merely to make a change pass.
- Production failures must be converted into a regression test, evaluation case, runbook update, or explicit accepted-risk record.

## Safety and permissions

Never perform these actions without explicit human approval:

- Production deployment or production configuration change.
- Destructive data operation or irreversible migration.
- Billing, pricing, entitlement, security, privacy, or legal-policy change.
- Sending external customer commitments or publishing marketing claims.
- Expanding credentials, permissions, or access to customer data.

## Knowledge maintenance

- Canonical facts belong in founder docs, specs, ADRs, runbooks, or schemas—not transient chat history.
- Repeated successful procedures become skills only after review and evaluation.
- Vendor-specific files must point to this contract instead of duplicating policy.
