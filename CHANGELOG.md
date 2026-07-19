# Changelog

All notable changes to this template are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- `AGENTS.md` **Context discipline** section: an affordance-style guide to loading context — state files as the index, `current_mission` / `active_spec` pointers for the current step, load-on-demand as the default, prefer fetching over guessing, and escalate rather than read everything to infer a missing decision. Framed explicitly as affordances and defaults, not a fixed read-list, so it orients a strong orchestrator instead of caging it while giving a smaller sub-agent a floor. (#18)
- `company/workflows/founder-doc-revision.md`: how to revise confirmed founder documents — everyday evolution by moving items between sections, substantive changes recorded as ADRs, with the weekly operating review as the cadence and a no-silent-change rule. Referenced from `AGENTS.md` and `weekly-operating-review.md`. (#16)

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
