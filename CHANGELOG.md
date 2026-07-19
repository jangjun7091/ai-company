# Changelog

All notable changes to this template are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- The Product Spec is now **agent-drafted then founder-ratified**, not produced by a full interview. `idea-to-release.md` distinguishes the two artifacts: the Idea Brief is *elicited* (its intent lives only in the founder's head), while the Product Spec is *derived* — the agent drafts it from the approved Idea Brief and the founder documents (especially `quality-bar.md`), then the founder ratifies the load-bearing few (acceptance-criteria thresholds, non-goals, human-gate impacts) and the agent asks only where "good" is genuinely underdetermined, never burying a guessed threshold. `AGENTS.md` Feature work and the `product-spec.md` pointer comment updated to match. (#24)

### Added

- "Executing build tasks" discipline in `company/workflows/idea-to-release.md` for delegating build work to workers (a subagent or any external CLI that reads `AGENTS.md`): one task with tight scope, isolate per branch/worktree, least privilege (read-only for review, write only for implementation, no sandbox bypass outside a disposable runner), verify-before-merge (a worker's self-report is not evidence), and keep the human gates for irreversible or outward-facing actions. Model-neutral by design — no vendor named. (#27)
- Altitude-and-resolution guard for the Idea Brief / Product Spec interview in `company/workflows/idea-to-release.md`: the interviewer holds each artifact at its altitude (the founder owns intent; the agent owns mechanism), defers implementation detail the founder volunteers to the Spec and Build phases instead of deepening to match, and states the decision-grade resolution it needs so the founder neither over-specifies (anchoring the agent) nor under-specifies (confident-wrong output). Found by running the #20 interview on a real product. (#22)
- Founder-interview discipline for the Idea Brief in `company/workflows/idea-to-release.md`: the brief is elicited through a bounded founder interview, not drafted unilaterally, reusing the `bootstrap-interview.md` interviewer stance with stage-specific additions (ground ambition in feasibility, make the quality bar checkable, distill rather than transcribe). Wired from `AGENTS.md` Feature work and pointer comments in both templates. #20 originally produced the Product Spec through the same interview; the drafted-then-ratified model described under Changed (#24) supersedes that part. (#20)
- `AGENTS.md` **Context discipline** section: an affordance-style guide to loading context — state files as the index, `current_mission` / `active_spec` pointers for the current step, load-on-demand as the default, prefer fetching over guessing, and escalate rather than read everything to infer a missing decision. Framed explicitly as affordances and defaults, not a fixed read-list, so it orients a strong orchestrator instead of caging it while giving a smaller sub-agent a floor. (#18)
- `company/workflows/founder-doc-revision.md`: how to revise confirmed founder documents — everyday evolution by moving items between sections, substantive changes recorded as ADRs, with the weekly operating review as the cadence and a no-silent-change rule. Referenced from `AGENTS.md` and `weekly-operating-review.md`. (#16)

### Fixed

- The release checklist specifies that the `version` bump in `ai-company.yaml` produces full SemVer (`x.y.z`) — releases so far wrote `X.Y` (`0.3`), leaving the field MAINTAINING calls the SemVer single source of truth in a non-SemVer format. The field itself normalizes at the next release, per the founder's decision; no mid-cycle edit. (#58)
- The Definition of Ready is satisfiable where it is checked: the Idea Brief covers the brief-level items, `acceptance_criteria_testable` is satisfied by the derived Product Spec, and the full gate passes before Build. Previously both workflow references told the agent the brief alone satisfies a gate whose criteria item is — post-#24 — a Spec artifact. Gate vocabulary unchanged. (#55)
- The repository map in `README.md` and `README.ko.md` matches the tree: all five workflows (`founder-doc-revision` was missing) and the full `docs/` set (research and incidents were missing). (#53)
- The resume protocol in `MAINTAINING.md` no longer hardcodes a milestone that goes stale after every release: the issue-list step takes the current milestone from `ROADMAP.md`'s "Next:" heading (it pointed at the already-released v0.3.0, so a resuming session saw zero planned issues). (#51)
- `session_start.py`'s operating-mode instruction matches the #18 Context discipline — start from the state-file index and load what the current step needs — instead of the fixed read-list ("Read current specs, decisions, review queues, and evidence") that predates it. (#49)
- The worker-delegation topology in `idea-to-release.md` reads as defaults, not mandates: a single task file per worker and per-worker branch/worktree isolation are the stated defaults with their override criteria, matching the contract's affordances-and-defaults posture. The safety bullets — least privilege and no sandbox bypass, verify-before-merge, human gates — stay firm. (#47)
- The operating loop in `idea-to-release.md` is fully wired: Verify names `definition_of_done` in `ai-company.yaml` as the completion bar (previously the manifest's done-gate was invoked by no workflow), Observe routes failures into `incident-to-learning.md`, and Learn hands the next mission back to Discover (`stage: discovery`) — previously the loop dead-ended at `learning`. (#45)
- Every state field has a named writer: escalations record the blocked task's id in `blocked_by_human` and clear it on resolution (`AGENTS.md`); open ADR ids are tracked in `active_decisions` (`docs/decisions/README.md`); the weekly operating review keeps `active_products` and `portfolio_stage` current. Previously all four fields were written by nothing — `company-state.yaml`'s header even named writers that never wrote it — and `blocked_by_human`'s comment promised "human-assistance-request ids" although escalations only carry a `task_id`. Comments fixed to match. (#43)
- `doctor.py` requires the templates the workflows build artifacts from — `idea-brief`, `product-spec`, `adr`, `incident`, `research-note` — so deleting one fails the contract check instead of leaving a workflow step silently unexecutable. Locked by a new fixture test. (#41)
- `templates/adr.md` satisfies its governing schema and uses one id scheme: a `## Question` section (`decision.schema.json` requires `question`) and `Id: ADR-NNN` — previously the title said `ADR-NNN` while the Id line said `DEC-NNN`. (#39)
- `templates/product-spec.md` can record the ratification the workflow requires: a `Status: draft <!-- draft | ratified -->` line and a `## Founder ratification` block — one checkbox per explicitly-confirmed item from `idea-to-release.md` (acceptance criteria incl. agent-chosen thresholds, quality bar and non-goals, human-gate impacts) plus a ratified date — mirroring the Idea Brief's founder-decision block. Previously nothing in the artifact distinguished a draft spec from a ratified one. (#37)
- Artifact instructions name their destinations: the Idea Brief and Product Spec are written *using* their templates into the mission's folder under `docs/specs/` — previously `idea-to-release.md` said "recorded in `templates/idea-brief.md`", which reads as writing into the blank template — and incident records get a home, the new `docs/incidents/` (with README), named from `incident-to-learning.md`. (#35)
- The bootstrap exit gate records `current_mission` (the approved first Idea Brief's path) alongside `stage` and `project_name` — in the workflow's section-6 state updates and exit step 2, the `session_start.py` exit-step text, and the `project-state.yaml` field comment. Previously the brief was approved during bootstrap but nothing pointed at it, so the next session's state index (`AGENTS.md` Context discipline) lost the first mission. The mechanical gate itself is unchanged. (#33)
- `idea-to-release.md` no longer describes acceptance criteria as an interview product: the Idea Brief interview elicits the concrete quality bar, and the derived Spec restates it as observable or machine-checkable criteria — matching the drafted-then-ratified model. The interviewer stance is scoped to the brief interview plus the Spec's ratification questions, and founder-volunteered implementation detail is parked in `docs/decisions/` (status `deferred`), the convention `bootstrap-interview.md` already uses. (#31)

## [0.3.0] - 2026-07-19

### Added

- `docs/research/` and `templates/research-note.md`: a home for market, competitive, literature, and domain research, and the location for the Customer & Market Research agent's evidence log — kept separate from founder truth, which holds only the confirmed distillation. (#14)

### Changed

- Bootstrap interview now instructs faithful, detailed capture of founder answers (preserve the founder's own words, examples, numbers, and edge cases) with a per-section read-back check, instead of writing a compressed summary. Founder-doc comments and `AGENTS.md` reinforce that founder docs are the source of truth, not a paraphrase. (#6)
- Defined a rigorous, non-sycophantic interviewer role for the bootstrap interview (probe vague answers, dig for intent, name gaps, no flattery) with an explicit boundary: the founder owns the vision; the interviewer makes it precise and evidence-separated rather than judging it. `AGENTS.md` adds a general no-flattery behavior. (#8)
- Numbered the interview sub-questions and added a per-section coverage rule so the interviewer cannot silently skip or merge questions, or drift into its own numbering. Before writing a section it must report per-question coverage (answered / partly / open). (#10)
- Clarified that founder docs are founder-altitude only: the `Open decisions` section is for founder-level questions, and implementation or technical details that surface during the interview are routed to `docs/decisions/` (status `deferred`) instead of being parked in founder docs. (#12)

## [0.2.0] - 2026-07-19

### Added

- `exit_steps` in the session-start output and a documented mechanical bootstrap exit gate: confirm the five founder documents, advance `stage` to `discovery`, re-run the script.
- `doctor.py` now validates stage values, portfolio-stage values, and each agent contract's escalation vocabulary against the escalation schema enum, and supports `--json`.
- `templates/evidence.md` and `templates/learning-entry.md`; existing templates name their governing schemas and carry the schema-required fields.
- Explicit "State updates" wiring from every workflow to `company/state/*.yaml`, and a `lifecycle.portfolio_stages` vocabulary.
- `LICENSE` (MIT), `CONTRIBUTING.md`, `CHANGELOG.md`, `.gitattributes`, issue-template config, and a CI smoke run of `session_start.py`.
- `MAINTAINING.md` and `ROADMAP.md`: a session-independent process for maintaining the template across versions, plus release and stars badges.

### Changed

- Founder-document confirmation is decided by the `Status:` line alone — accepted with or without backticks, case-insensitively. The undocumented requirement to delete an HTML comment is gone.
- The eight agent contracts use the escalation schema's trigger enum verbatim (contracts bumped to 0.2).
- Tests run against fixture trees instead of the live repository.
- README rewritten: template usage, architecture diagram, honest adapter list, Windows notes, Korean translation.

### Fixed

- Founders could not leave bootstrap mode without reading the session script's source.
- Configuring the template turned CI red, because the test suite asserted the unconfigured state against live files.
- Session output leaked Windows backslash paths.

## [0.1.0] - 2026-07-19

### Added

- Initial template generated with GPT-5.6: `AGENTS.md` contract, founder source-of-truth documents, eight agent role contracts, four workflows, typed schemas, state files, artifact templates, environment adapters, guardrail scripts, and CI.
