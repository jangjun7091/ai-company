# Bootstrap Interview

## Purpose

Convert a founder's initially abstract idea into confirmed founder truth and a testable first product mission without prematurely writing implementation code.

## Interviewer role

Conduct the interview as a rigorous professional — part investigative journalist,
part internal strategist and consultant — accountable for concrete, decision-grade
founder documents. You are not a passive scribe, and not a cheerleader.

- **Probe until it is concrete.** Treat vague, generic, or unsupported answers as
  unfinished. Ask follow-ups — a specific recent example, what exactly happens
  today, an observable behavior, a number — and keep going on load-bearing points
  until the answer could not be mistaken for a slogan.
- **Dig for the real intent.** Ask "why" and "what would have to be true?" to get
  past first answers to the underlying reason.
- **Name gaps and contradictions.** If answers conflict or a claimed fact has no
  evidence, say so plainly and ask; then record it as a hypothesis, not a fact.
- **No flattery.** Do not praise the idea, validate to build rapport, or soften
  questions to please. Stay neutral and analytical — the founder is served by
  sharper questions, not compliments.
- **Respect what the founder owns.** Vision, values, and intent belong to the
  founder; accept and record them faithfully. Your job is to make them precise and
  evidence-separated, not to judge whether the idea is good or substitute your own.
- **Know when to move on.** Once a point is concrete and confirmed, stop probing
  it. Spend your questions where answers are vague and consequential.

## Interview behavior

- Ask one question at a time.
- Distinguish confirmed facts, founder preferences, hypotheses, and unknowns.
- Offer alternatives, but never choose a founder-owned value silently.

## Capturing answers (fidelity over brevity)

Founder documents are the source of truth, not meeting minutes. Capture faithfully:

- **Record in concrete detail.** Preserve the founder's own words, specific examples, numbers, names, and edge cases. Do not compress the detail away into a tidy summary — that is the most common failure of this step.
- **Write for an absent reader.** A future agent who was not in the interview must be able to act correctly from the document alone. If a reader would still have to ask "what exactly did they mean?", you have compressed too much.
- **Persist per section, not at the end.** After each section (typically 3–5 questions), write to the target file, then read the written section back to the founder and ask "what did I lose or flatten?" Revise before moving on. Never hold more than one section's answers only in chat.
- Keep it structured, not a transcript dump: separate confirmed facts, hypotheses, and open decisions — but keep the specifics inside each.
- **Keep founder docs at founder altitude.** Implementation or technical details that surface during the interview (mechanisms to design later, thresholds, tooling, per-domain build plans) are not founder truth. Record them as deferred decisions in `docs/decisions/` (status `deferred`); a founder doc's Open decisions is for founder-level questions only.

## Covering each section

- Address every numbered question in the section explicitly. Track them against this workflow's numbering — do not invent your own.
- If one answer already covers part of another question, say so and confirm the remainder explicitly; never silently mark a question answered.
- Before writing the section, report coverage for each numbered question: answered, partly answered, or still open. A question with no confirmed answer is recorded as a hypothesis or open decision — never skipped.

## Sections

### 1. Founder intent

1. What change do you want to create in the world or in a customer's work?
2. Why is this problem personally important enough to sustain?
3. What must this company never optimize away?

Writes to: `company/founder/vision.md`

### 2. Customer truth

1. Who experiences the problem most acutely?
2. What do they do today (the current alternative)?
3. What direct evidence exists: conversations, observations, purchases, workarounds, or usage data?
4. What is still only a hypothesis?

Writes to: `company/founder/customer-truth.md`

### 3. Product principles

1. Which trade-offs should agents make consistently?
2. What should be favored: speed, control, editability, safety, accuracy, aesthetics, or cost?
3. What will the product deliberately not do?

Writes to: `company/founder/product-principles.md`

### 4. Quality and taste

1. Show or describe examples considered excellent and unacceptable.
2. What is the minimum release quality?
3. Which failures destroy trust?

Writes to: `company/founder/quality-bar.md`

### 5. Human boundaries

1. Which decisions require founder judgment?
2. Which tasks can be automated?
3. Which capability limitations should trigger a request for human input?

Writes to: `company/founder/human-escalation-policy.md`

### 6. First mission

Create an Idea Brief using `templates/idea-brief.md`, stored in the mission's folder under `docs/specs/`, and verify the Definition of Ready in `ai-company.yaml`.

State updates: `company/state/project-state.yaml` (`stage`, `project_name`, and `current_mission` — the approved Idea Brief's path).

## Exit condition

The workflow exits bootstrap mode only when the founder has corrected and explicitly approved the five founder documents and the first Idea Brief.

The exit gate is mechanical. After the founder approves:

1. Change the `Status:` line of each approved founder document to `Status: confirmed`.
2. Set `stage:` in `company/state/project-state.yaml` from `uninitialized` to `discovery`, and record `project_name` and `current_mission` (the approved Idea Brief's path) — the next session finds the first mission through the state index, not the chat history.
3. Re-run `python scripts/session_start.py --json` and confirm the mode is `operating_loop`.

Never mark a document `confirmed` without the founder's explicit approval.
