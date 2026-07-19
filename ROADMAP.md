# Roadmap

> Scope: the roadmap for the **ai-company template itself**. Delete this file in
> repositories created *from* the template.

This is the durable "what's next." Granular, actionable work lives in
[GitHub issues](https://github.com/jangjun7091/ai-company/issues) under milestones;
this file holds the versioned themes so any session can see the direction at a glance.

## Versioning

The template follows [SemVer](https://semver.org/), starting at `0.x` while the
shape can still change, then `1.0.0` once the operating contract is stable. The
current version is the `version` field in `ai-company.yaml`.

## Shipped

- **0.1.0** — initial template (generated with GPT-5.6).
- **0.2.0** — reliable bootstrap exit gate, fixture-based tests, unified escalation
  vocabulary, real contract validation in `doctor.py`, schema-wired templates,
  state wiring, public-repo docs, Korean README.
- **0.3.0** — dogfooding hardening of the bootstrap interview (faithful detailed
  capture, a rigorous non-sycophantic interviewer, numbered questions with
  per-section coverage, founder-altitude discipline) and a home for research
  (`docs/research/`, `templates/research-note.md`). See `CHANGELOG.md`.
- **0.4.0** — the coherence release: the Product Spec became agent-drafted and
  founder-ratified, the Idea Brief interview gained altitude-and-resolution
  discipline, `AGENTS.md` gained an affordance-style context discipline,
  confirmed founder docs gained a revision workflow, and build tasks gained
  worker-delegation defaults — plus a full contract audit (19 fixes: state
  wiring, artifact destinations, DoR/DoD gate wiring, doctor coverage,
  defaults-not-mandates cleanups). See `CHANGELOG.md`.

## Next: 0.5.0 — "prove it works end to end"

Theme: lower the distance between cloning the template and seeing a complete company.

- A worked example under `examples/` (filled founder docs + one feature run through
  idea-to-release) so newcomers see the finished state, not just blanks.
- Validate real artifact instances against the JSON schemas (stdlib-only).
- A maintainer/session orientation helper, mirroring `session_start.py`.
- A Windows check script (no GNU Make required).
- A 60-second quickstart recording in the README.

## Later

- **0.6.0 — richer operating loop and trustworthy evidence:** scaffolding helpers
  for specs/ADRs/tasks, more worked workflows (feedback and experiment loops —
  wiring the already-shipped `templates/experiment.md`), eval-harness stubs, and
  a learning ledger that visibly reduces repeated-failure counts.
- **1.0.0 — stable contract:** the operating contract, schemas, and gates are
  committed to and versioned for backward compatibility.

## A note on version numbers

If you prefer product-style numbers (v2.1, v3.0, …), map them onto this SemVer
track — but a project honestly at `0.3` should grow through `0.4 → 1.0` rather than
jump to `2.x`. Big themes become minor/major bumps; small fixes become patch bumps.
