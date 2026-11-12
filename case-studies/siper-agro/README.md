# SIPER-AGRO | Agribusiness Document Reconciliation & Decision Intelligence

**Case study 03 · CIEC LAB · November 2026 · Synthetic data only**

**Business question:** When purchase, sale, inventory, settlement, cash and freight records disagree, what can an operations manager *actually verify* before taking action?

SIPER-AGRO is a private local application for structured operational diagnosis in agricultural storage/trading (acopio). This public case documents a **controlled synthetic reconciliation**, an executive reading layer and an independent arithmetic reconstruction. It is **not** a release of the private application or its internal algorithms.

> **Result:** 4/4 documentary families calculated, 7 explicit comparisons, **5 discrepancies requiring review** and **2 matching comparisons**. Discrepancies are **not** established losses, fraud, causal findings or financial benefit.

## Evidence at a glance

| Reconciliation | Synthetic inputs | Difference | Management interpretation |
|---|---|---:|---|
| Inventory closure | Opening 100 TN + purchased 60 TN - sold 40 TN; recorded closing 118 TN | **-2 TN** | Recount and reconcile cut-off / dispatch documents. |
| Settlement LIQ-1 | Settlement ARS 10,000; recorded payments ARS 9,500 | **-500 ARS** | Check payment allocation and supporting receipts. |
| Settlement LIQ-2 | Settlement ARS 5,000; payments ARS 5,000 | **0 ARS** | Matches only for this linked relation. |
| Freight COST-1 | Freight record ARS 1,600; independent cost ledger ARS 1,400 | **+200 ARS** | Reconcile trip invoices and cost classifications. |
| Freight COST-2 | Freight record ARS 700; cost ledger ARS 700 | **0 ARS** | Matches only for this linked relation. |
| Price pair 1 | Purchase 100 vs sale 90 ARS/TN | **-10 ARS/TN** | Check contract, product quality and pricing basis; not profit. |
| Price pair 2 | Purchase 120 vs sale 125 ARS/TN | **+5 ARS/TN** | Check contract and cost basis; not profit. |

**What changed in the management decision:** rather than concluding that the inventory difference equals a financial loss, the review prioritizes a physical recount, document cut-off checks and a named owner. The same evidence-first discipline applies to settlements, freight and price pairs. See [management decision brief](docs/DECISION_BRIEF_ES.md).

## Reproduce the figures in under a minute

Requires **Python 3.10+**, using only the standard library.

```bash
cd case-studies/siper-agro
python src/reproduce.py
python -m unittest discover -s tests -v
```

- [Synthetic public transactions](data/synthetic_transactions.csv) — 20 intentionally artificial records grouped by explicit relation ID; no client data.
- [Independent reconstruction](src/reproduce.py) — decimal arithmetic, explicit joins only, unit checks and refusal of malformed inputs.
- [Nine automated tests](tests/test_reproduce.py) — seven comparisons, completeness and negative controls.
- [Expected machine-readable output](results/expected.json) — sample output of the public reconstruction.
- [Evidence, scope and limitations](docs/EVIDENCE_AND_LIMITATIONS.md) — provenance and claims policy.

**Important distinction:** this public Python script reproduces the *shown arithmetic*; it does **not** reproduce the private app, its ingestion protocol, security, PDF generation, G7 risk model, VIPER, KRI, IRO, MCC or PFO-Lite engines.

## What was actually validated

The underlying synthetic G10F case reported **0 intake issues**, **6/6 inventory rows linked**, **5/5 settlements**, **5/5 logistics** and **4/4 price rows**. The private case carried a restricted ZIP with source cells and hashes, and a separate anonymized PDF. That private case is **not uploaded here**.

The owner subsequently ran the W7 update and reported `WINDOWS_PASS_CANDIDATE` for app and package integrity plus the native Windows gate. **Full W7 evidence logs were not supplied with this public release**, so this repository makes no independent claim of complete Windows certification or commercial readiness.

**Current limits:** 41 sector-domain decisions remain open. No validated crosswalk from G10F documentary inputs to the legacy 12 KRIs, IRO, MCC and PFO-Lite. No financial-loss estimate, no real customer case, no proof of production deployment, and no automated commercial approval. Those limits are intentional, not hidden.

## Value demonstrated

1. **Business analysis:** decompose an ambiguous operational concern into testable comparisons and evidence requests.
2. **Data quality and traceability:** maintain explicit relation identifiers, units and a route to source documents.
3. **Quantitative reproducibility:** reconstruct seven comparisons using decimal arithmetic and independent tests.
4. **Decision discipline:** distinguish reconciliation signals from validated economics, priorities and causal claims.
5. **Communication:** translate technical findings into owner/actions, instead of handing managers raw errors.

**Related portfolio:** [Executive portfolio](../../EXECUTIVE_PORTFOLIO.md) · [Restaurant profitability](../mba-port-001/README.md) · [Restaurant operational diagnosis](../patio-del-molino/README.md)

**Ricardo Vera · CIEC LAB · Argentina** — Business Analysis · Operational Intelligence · Research & Decision Systems.

*No proprietary source, private case ZIPs, company identities, secrets or real business records are included.*
