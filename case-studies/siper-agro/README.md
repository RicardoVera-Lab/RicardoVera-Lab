# SIPER-AGRO | Close the gaps before they become management decisions

### Operational intelligence for grain storage, trading and agribusiness

**Ricardo Vera · CIEC LAB | Business Analysis & Operational Intelligence**

## Your stock ledger says one thing. Your settlements and freight records may say another.

The problem is not a lack of spreadsheets. It is the absence of a reliable way to **connect operational records, explain differences and know what must be verified before closing**.

SIPER-AGRO translates fragmented records into a traceable management review. It links documents using explicit identifiers, reconstructs differences and defines the evidence each operating area needs to resolve them.

[**Executive brief in Spanish**](README_ES.md) · [**Evidence and calculations**](#inspect-the-evidence) · [**Discuss an agribusiness diagnostic**](mailto:richardvera084@gmail.com?subject=SIPER-AGRO%20%7C%20Agribusiness%20diagnostic)

---

## Seven comparisons. Four areas. One focused decision agenda.

| Management area | What the linked records show | Decision to protect |
|---|---:|---|
| **Inventory** | **−2 TN** against the theoretical closing balance | Reconcile count, movements and reporting cut-off |
| **Settlements** | **−500 ARS** in the payment comparison | Check receipts, allocations and payment dates |
| **Freight** | **+200 ARS** between freight and expense ledger | Validate service scope and recorded cost |
| **Commercial prices** | **−10 / +5 ARS per TN** on two purchase/sale comparisons | Assess product, quality, terms and contract basis |

**What matters:** three documentary discrepancies deserve reconciliation, two price spreads need commercial context and two additional documentary comparisons match numerically. **A price spread is not automatically an accounting error or commercial loss.**

This distinction is central to decision-quality analysis: not every nonzero value is an exception, and not every matching value closes an entire control cycle.

## What I do for an agribusiness

**01 · Reconstruct the operating picture.** Define the review period and link purchases, sales, inventory, settlements and logistics by auditable reference.

**02 · Separate exceptions from normal commercial movement.** Test documentary balances without inventing price thresholds or treating distinct units as equivalent.

**03 · Prioritize management intervention.** Establish which questions belong to inventory, treasury, transport or commercial leadership.

**04 · Close with evidence.** Produce an exception register with required documents, owners and explicit conditions for resolution.

### The output is an executive decision, not another dashboard.

Management receives a focused review: where the numbers differ, why the comparison is relevant, which document is missing and what should happen next.

[**Read the management decision brief**](docs/DECISION_BRIEF_ES.md)

## Inspect the evidence

The published analytical example includes [source transactions](data/synthetic_transactions.csv), a [Python reconciliation module](src/reproduce.py), [nine automated tests](tests/test_reproduce.py), [expected results](results/expected.json) and [technical scope](docs/EVIDENCE_AND_LIMITATIONS.md).

From this folder, with Python 3.10+:

```bash
python src/reproduce.py
python -m unittest discover -s tests -v
```

The project also includes a root-level GitHub Actions workflow covering Python 3.10, 3.12 and 3.13.

**Case scope:** a reproducible operational scenario built from structured test records; the analytical logic and published comparisons can be inspected independently.

---

## Is your company closing periods with unexplained differences?

**A closing balance should be explainable — not just accepted.**

**Ricardo Vera | CIEC LAB** · Argentina · Remote B2B

[**Request an operational intelligence diagnostic**](mailto:richardvera084@gmail.com?subject=SIPER-AGRO%20%7C%20Operational%20Diagnostic) · [Executive portfolio](../../EXECUTIVE_PORTFOLIO.md) · [Restaurant profitability](../mba-port-001/README.md)
