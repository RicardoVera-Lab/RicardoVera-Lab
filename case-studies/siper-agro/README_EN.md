# SIPER-AGRO | Executive & Hiring Brief

**Operational intelligence · Agribusiness data reconciliation · CIEC LAB**

**Business problem:** Grain storage and trading operations frequently depend on disconnected inventory, purchasing, sales, cash, settlement and freight records. When totals disagree, management needs a traceable explanation and a concrete review plan.

**Documented case:** Four reconciliation areas, seven explicitly linked comparisons, five differences and two matches.

| Operational signal | Difference | Next management question |
|---|---:|---|
| Inventory closure | **−2 TN** | Which movement, count or cut-off explains the balance? |
| Settlements vs payments | **−500 ARS** | Which payment allocation or receipt is outstanding? |
| Freight vs cost ledger | **+200 ARS** | Are these cost records measuring the same service? |
| Two price pairs | **−10 / +5 ARS/TN** | Are product, terms and pricing bases comparable? |

**What the work demonstrates:** business problem framing, source linking, structured verification, decimal-precision reconciliation, nine automated tests and management-oriented recommendations.

**Technical evidence:** [Source data](data/synthetic_transactions.csv) · [Public reproduction](src/reproduce.py) · [Tests](tests/test_reproduce.py) · [Executive decisions](docs/DECISION_BRIEF_ES.md)

**Reproduce:** From this folder, run `python src/reproduce.py` and `python -m unittest discover -s tests -v` (Python 3.10+, no external packages).

**Engagement fit:** Business Analyst · Operations Analyst · Data Quality · Operational Risk · Agribusiness Consulting.

[**Discuss a role or operational diagnostic**](mailto:richardvera084@gmail.com?subject=Ricardo%20Vera%20%7C%20Business%20Analysis)

*Portfolio demonstration using synthetic operational records; not a client engagement. Technical scope and product limits are documented [here](docs/EVIDENCE_AND_LIMITATIONS.md).*

[Full case study](README.md) · [Versión en español](README_ES.md)
