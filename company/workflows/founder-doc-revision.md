# Founder Document Revision

Founder documents are the source of truth agents act on. `Status: confirmed`
means "the founder has approved this as current truth," not "frozen forever."
They are living documents — revise them as evidence accumulates and thinking
sharpens, but never silently: a change to a principle or boundary changes how
the whole company behaves.

## Two kinds of revision

### Everyday evolution — move items between sections

Most revision is promoting content as evidence comes in, using the sections
each founder document already has:

- A **hypothesis** is validated → move it to **Confirmed** with its evidence.
- An **open decision** is decided → move it to **Confirmed** (record an ADR if
  it is consequential).
- A **confirmed** statement is proven wrong → correct it and note why.

Low ceremony: edit, update `Last reviewed`, commit with a clear message. Git
history preserves what changed and when.

### Substantive change — principle, vision, quality bar, or boundary

Changing a product principle, pivoting the vision, or moving a quality or
escalation boundary changes agent behavior. Higher ceremony:

- Record the reasoning as an ADR in `docs/decisions/` (`templates/adr.md`) — a
  diff shows *what* changed, not *why*.
- The founder approves the change; agents may draft and propose, only the
  founder confirms.
- Commit or open a PR that links the ADR, and update `Last reviewed`.

## Triggers

- New customer evidence contradicts or refines `customer-truth.md`.
- A principle proved wrong or too rigid in practice (from idea-to-release or an
  incident).
- The vision sharpens or pivots.
- An open decision is resolved, or a hypothesis is validated or invalidated.

## Cadence

The natural place to revisit founder truth against accumulated evidence is the
weekly operating review (`weekly-operating-review.md`). Revise deliberately
there rather than ad hoc.

## Rules

- Never change a confirmed founder document silently. Always: founder approval,
  git traceability, and — for substantive changes — an ADR that records why.
- Keep `Status: confirmed` after the founder re-approves; update `Last reviewed`.
