# Weekly Operating Review

Review only decision-relevant information:

- Customer value delivered and evidence.
- Product usage, activation, retention, conversion, and revenue signals.
- Reliability, security, cost, and unresolved incidents.
- Founder decisions waiting for input.
- Repeated agent failures and capability gaps.
- Experiments completed, invalidated hypotheses, and next priorities.
- Whether new evidence should revise any founder document (see `company/workflows/founder-doc-revision.md`).
- Work that should be stopped, simplified, automated, or escalated to a human specialist.

Outputs:

- Updated company priorities.
- Explicit decisions and dissent.
- A small set of approved missions.
- Changes to quality gates, skills, evaluations, or permissions.

State updates:

- `company/state/company-state.yaml`: `company_priorities`, `founder_review_queue`, `capability_gaps`; review and prune `repeated_failures`; update `active_products` and `portfolio_stage` when a product has launched or retired or the portfolio's shape has changed.
- `company/state/project-state.yaml`: `next_review`.
