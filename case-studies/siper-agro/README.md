# SIPER-AGRO | Operational Intelligence for Agribusiness

### From disconnected records to an actionable management review

**CIEC LAB · Ricardo Vera · Business Analysis / Operational Intelligence**

An acopio can have purchase records, invoices, inventory balances and freight settlements in separate systems—and still lack a reliable answer to a basic question: **which differences deserve management attention before the next closing cycle?**

SIPER-AGRO approaches that problem through structured document intake, explicit cross-source reconciliation and traceable management findings. The objective is not another dashboard: it is a clear list of what differs, what evidence is needed and who should verify it.

**[Resumen ejecutivo en español](README_ES.md)** · **[Executive portfolio](../../EXECUTIVE_PORTFOLIO.md)** · **[Contact](mailto:richardvera084@gmail.com?subject=CIEC%20LAB%20%7C%20SIPER-AGRO%20business%20inquiry)**

---

## The operational problem

A mismatch between recorded stock and its theoretical closing balance may come from an unposted movement, a cut-off issue, a measurement error or something else. Acting on the figure without reconstructing the record trail can produce the wrong correction.

The same challenge appears when settlements and payments, freight records and cost ledgers, or purchase and sale prices cannot be reconciled under a common reference.

**The approach:** organize the source records, calculate defensible differences, identify their documentary links, and translate each exception into a verification priority.

## Results of the controlled case

<small>Demonstration based on synthetic operational records, not a client engagement.</small>

| Area | Reconciled figures | Result | Management action |
|---|---|---:|---|
| **Inventory** | Opening 100 TN + purchases 60 TN − sales 40 TN vs recorded closing 118 TN | **−2 TN** | Verify physical count, dispatch notes and period cut-off |
| **Settlements** | ARS 10,000 settled vs ARS 9,500 recorded as paid | **−500 ARS** | Reconcile payment allocation, receipts and payment dates |
| **Freight** | ARS 1,600 on a trip vs ARS 1,400 in the cost ledger | **+200 ARS** | Compare invoice scope, rate and accounting classification |
| **Price comparison** | Two purchase/sale pairs with consistent ARS/TN units | **−10 / +5 ARS/TN** | Validate comparability of product, contract and pricing basis |

Two additional linked comparisons reconcile to zero: one settlement and one freight cost.

**Reconciliation coverage:** **4 areas · 7 linked comparisons · 5 differences requiring review · 2 matches.** The case demonstrates a method to prioritize investigation; a documentary discrepancy is not, on its own, a confirmed financial loss.

## What the management team receives

1. **A structured evidence register.** Each finding retains its relation ID, source category, unit and corresponding comparison.
2. **A prioritized investigation list.** Inventory, treasury, logistics and commercial responsibilities are separated instead of mixing different operational problems.
3. **A practical closing standard.** For each exception, the reviewer knows which documents to check and what would count as a reconciled outcome.
4. **A reproducible numerical basis.** The public example includes independent Python verification and automated controls, so a reviewer can reproduce every published figure.

[**Read the executive decision brief (Spanish)**](docs/DECISION_BRIEF_ES.md)

## From operational records to an engagement

The consulting workflow is designed to be straightforward:

**1 — Scope.** Define the period, operation, systems and management decision to support.

**2 — Reconcile.** Receive the six operational data categories, check their structure and reconcile explicit relationships.

**3 — Prioritize.** Rank the discrepancies by business relevance and identify missing documentary evidence.

**4 — Review with management.** Present a concise findings register, validation responsibilities and recommended next steps.

**5 — Follow up.** Re-check the evidence and update the status of each exception in the agreed review cycle.

This is a proposed consulting process, not a claim that it has already been delivered to a commercial acopio.

## Technical proof you can inspect

The proprietary SIPER-AGRO application runs locally; the **public repository contains a separate, intentionally small reproduction of the documented arithmetic**, not the private engine.

| Public artifact | What it demonstrates |
|---|---|
| [Source transactions](data/synthetic_transactions.csv) | Explicit relation identifiers, roles and units |
| [Reconciliation script](src/reproduce.py) | Deterministic calculations using `decimal.Decimal` |
| [Automated tests](tests/test_reproduce.py) | Nine unit and negative-control tests |
| [Expected output](results/expected.json) | Machine-readable reconciliation results |
| [Verification scope](docs/EVIDENCE_AND_LIMITATIONS.md) | Input provenance, coverage and technical boundaries |

**Run locally** with Python 3.10+; no external dependencies:

```bash
cd case-studies/siper-agro
python src/reproduce.py
python -m unittest discover -s tests -v
```

The public tests also run in GitHub Actions on Python **3.10, 3.12 and 3.13**. This independently verifies the published arithmetic; it is not a certification of every proprietary module.

## Why this matters

**For an acopio or grain trading company:** a stronger closing review begins with reconciled records, clearly assigned questions and evidence that can support the next decision.

**For employers:** this case demonstrates requirements framing, data-quality rules, quantitative reconciliation, Python verification, technical documentation and executive communication.

### Discuss an operational diagnostic

**Ricardo Vera | CIEC LAB · Argentina · Remote collaboration**

[**Contact me about an agribusiness diagnostic**](mailto:richardvera084@gmail.com?subject=SIPER-AGRO%20%7C%20Operational%20Diagnostic) · [**Discuss a Business / Operations Analyst role**](mailto:richardvera084@gmail.com?subject=Ricardo%20Vera%20%7C%20Analyst%20Opportunity)

**Related work:** [Restaurant profitability](../mba-port-001/README.md) · [Restaurant operational intelligence](../patio-del-molino/README.md)
