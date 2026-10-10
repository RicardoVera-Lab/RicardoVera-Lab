# SEDA — Experimental Decision Engine (Archived)

**CIEC LAB | Engineering case study | Status: ARCHIVED / REUSABLE / NOT PRODUCTION-READY | October 2026**

## Research question

Can a small, event-driven decision engine enforce explicit policy contracts, abstain from action, record decisions and fail closed under specified error conditions? Can the same core be adapted to a second, non-financial use case without rewriting it?

SEDA-QX began as an experimental trading-oriented decision engine. This entry documents a **bounded engineering result**, not a profitable trading strategy or a commercial software release.

## Work completed

- Built an offline Python prototype that receives structured events, evaluates programmed policies and records outcomes.
- Added input/decision validation, duplicate-event handling, retry boundaries and a configurable strict failure mode.
- Iteratively repaired defects uncovered by independent adversarial review, including invalid risk limits, malformed policy outputs, event-state mutation after failed evaluation, and strict-mode bypass cases.
- Reported final validation: **65/65 implementation tests and 19/19 independent review tests** passing within their stated scope.
- Demonstrated a **limited non-financial adaptation** for synthetic operational incident classification by using an external adapter without rewriting the original engine.

## What the evidence does *not* establish

- No validated trading profitability, superior risk-adjusted returns or market-predictive advantage.
- No safe live broker execution, production recovery guarantees, hostile-code isolation or universal transactional safety.
- No demonstrated autonomous learning or general-purpose reasoning.
- No verified business buyers, customer deployments or revenue attributable to SEDA.
- The non-financial demonstration does not establish superiority over a simpler rules-based program.

Test counts refer to the reviewed prototype and defined test scenarios. They are **not** certifications of production safety.

## Decision and rationale

**Development paused in October 2026.** Technical feasibility and narrow portability were demonstrated, but the available evidence did not justify continued investment in a standalone product. CIEC LAB preserved the code, test suites, review reports and decision trail privately for potential reuse.

**Reactivation rule:** only revisit the engine for a concrete operational need with a defensible benefit against simpler alternatives, appropriate technical validation and evidence of user or buyer demand.

## What this case demonstrates about CIEC LAB

The laboratory can construct executable software, subject it to independent adversarial tests, repair reproducible defects, define the limits of its claims and **stop a technically interesting program when commercial justification is insufficient**.

**Public evidence. Private machinery.** Source code, internal laboratory architecture, orchestration, agent prompts, handoff packs and institutional-memory archives are not published here.

---

[CIEC LAB portfolio](README.md) · [Executive portfolio](EXECUTIVE_PORTFOLIO.md)
