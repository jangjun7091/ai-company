# Bootstrap Interview

## Purpose

Convert a founder's initially abstract idea into confirmed founder truth and a testable first product mission without prematurely writing implementation code.

## Interview behavior

- Ask one question at a time.
- Distinguish confirmed facts, founder preferences, hypotheses, and unknowns.
- Challenge vague terms by requesting examples or observable behavior.
- Offer alternatives, but never choose a founder-owned value silently.

## Capturing answers (fidelity over brevity)

Founder documents are the source of truth, not meeting minutes. Capture faithfully:

- **Record in concrete detail.** Preserve the founder's own words, specific examples, numbers, names, and edge cases. Do not compress the detail away into a tidy summary — that is the most common failure of this step.
- **Write for an absent reader.** A future agent who was not in the interview must be able to act correctly from the document alone. If a reader would still have to ask "what exactly did they mean?", you have compressed too much.
- **Persist per section, not at the end.** After each section (typically 3–5 questions), write to the target file, then read the written section back to the founder and ask "what did I lose or flatten?" Revise before moving on. Never hold more than one section's answers only in chat.
- Keep it structured, not a transcript dump: separate confirmed facts, hypotheses, and open decisions — but keep the specifics inside each.

## Sections

### 1. Founder intent

- What change do you want to create in the world or in a customer's work?
- Why is this problem personally important enough to sustain?
- What must this company never optimize away?

Writes to: `company/founder/vision.md`

### 2. Customer truth

- Who experiences the problem most acutely?
- What do they do today?
- What direct evidence exists: conversations, observations, purchases, workarounds, or usage data?
- What is still only a hypothesis?

Writes to: `company/founder/customer-truth.md`

### 3. Product principles

- Which trade-offs should agents make consistently?
- What should be favored: speed, control, editability, safety, accuracy, aesthetics, or cost?
- What will the product deliberately not do?

Writes to: `company/founder/product-principles.md`

### 4. Quality and taste

- Show or describe examples considered excellent and unacceptable.
- What is the minimum release quality?
- Which failures destroy trust?

Writes to: `company/founder/quality-bar.md`

### 5. Human boundaries

- Which decisions require founder judgment?
- Which tasks can be automated?
- Which capability limitations should trigger a request for human input?

Writes to: `company/founder/human-escalation-policy.md`

### 6. First mission

Create an Idea Brief using `templates/idea-brief.md` and verify the Definition of Ready in `ai-company.yaml`.

State updates: `company/state/project-state.yaml` (`stage`, `project_name`).

## Exit condition

The workflow exits bootstrap mode only when the founder has corrected and explicitly approved the five founder documents and the first Idea Brief.

The exit gate is mechanical. After the founder approves:

1. Change the `Status:` line of each approved founder document to `Status: confirmed`.
2. Set `stage:` in `company/state/project-state.yaml` from `uninitialized` to `discovery`, and record `project_name`.
3. Re-run `python scripts/session_start.py --json` and confirm the mode is `operating_loop`.

Never mark a document `confirmed` without the founder's explicit approval.
