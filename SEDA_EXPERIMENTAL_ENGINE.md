# SEDA — Experimental Decision Engine (Archived)

**CIEC LAB | Engineering case study | Status: ARCHIVED / REUSABLE / NOT PRODUCTION-READY | October 2026**

## Research question

Can a small, event-driven decision engine enforce explicit policy contracts, abstain from action, record decisions and fail closed under specified error conditions? Can the same core be adapted to a second, non-financial use case without rewriting it?

SEDA-QX began as an experimental trading-oriented decision engine. This entry documents a **bounded engineering result** centered on event processing, policy contracts and fault containment.

## Work completed

- Built an offline Python prototype that receives structured events, evaluates programmed policies and records outcomes.
- Added input/decision validation, duplicate-event handling, retry boundaries and a configurable strict failure mode.
- Iteratively repaired defects uncovered by independent adversarial review, including invalid risk limits, malformed policy outputs, event-state mutation after failed evaluation, and strict-mode bypass cases.
- Reported final validation: **65/65 implementation tests and 19/19 independent review tests** passing within their stated scope.
- Demonstrated a **limited non-financial adaptation** for synthetic operational incident classification by using an external adapter without rewriting the original engine.

## Scope of validation

The test results cover a bounded offline Python prototype, defined failure scenarios and a synthetic non-financial adaptation. The system has not undergone production integration or deployment qualification. These results should not be interpreted as broader operational certification.

## Decision and rationale

**Development paused in October 2026.** Technical feasibility and narrow portability were demonstrated, and the work was preserved as a reusable experimental asset rather than expanded into a standalone product. CIEC LAB preserved the code, test suites, review reports and decision trail privately for potential reuse.

**Reactivation rule:** only revisit the engine for a concrete operational need with a defensible benefit against simpler alternatives, appropriate technical validation and a defined use case.

## What this case demonstrates about CIEC LAB

The laboratory can construct executable software, subject it to independent adversarial tests, repair reproducible defects, define the limits of its claims and **preserve reusable engineering results with explicit evidence boundaries**.

**Public evidence. Private machinery.** Source code, internal laboratory architecture, orchestration, agent prompts, handoff packs and institutional-memory archives are not published here.

---

[CIEC LAB portfolio](README.md) · [Executive portfolio](EXECUTIVE_PORTFOLIO.md)
