# More sales. Less margin. A decision problem worth investigating.

### Executive case MBA-PORT-001 · Restaurant profitability and operational decision intelligence

**Ricardo Vera | Business Analysis · Operational Intelligence · CIEC LAB**

> **Revenue growth is not a profitability strategy.** The relevant question is where margin is being absorbed—and which intervention remains sound when customers, costs and operations react.

## The business problem

A 12-month restaurant case recorded **32,473,404.18 UM** in annual net sales and **8,211,449.91 UM** in simplified operating profit. Monthly operating margin fell from **28.35% in January to 22.17% in December**: **6.18 percentage points of erosion**.

The analysis traced ingredient costs from **36.23% to 44.29% of net sales**, waste from **0.43% to 0.97%**, and delivery from **2.27% to 3.28%** over those months.

## The finding that changes management action

A 15% reduction in discounts produces **+114,563.18 UM** in modeled annual operating profit *if units do not fall*. A **1% unit decline** reverses it to **−82,452.97 UM versus baseline**. Likewise, a 5% increase in one product's price produces **+95,150.38 UM** with 3% fewer units but **−10,419.55 UM** with 8% fewer units.

**Decision:** test demand behavior before changing prices or discounts. Design a controlled waste-management pilot or staffing-coverage pilot without booking hypothetical savings. Keep an auditable baseline.

## What this case delivers

- Financial reconciliation across sales, recipe cost, waste, delivery, operating expenses and inventory.
- Product-level price and discount scenarios with explicit demand sensitivities.
- Five-option executive decision matrix with stop conditions.
- Operational intervention states, cancellation and reversal controls.
- Four CSV input sources, independently regenerable outputs, and an automated Python test suite.

**Case data:** synthetic 2025 data, 14 products over 12 months, denominated in monetary units (UM). [Methodology and calculations](docs/METHODOLOGY.md).

| Document | Purpose |
|:--|:--|
| [Executive decision](reports/EXECUTIVE_DECISION.md) | Management findings and next actions |
| [Financial results](outputs/RESULTS.json) | Exact baseline and scenario values |
| [Option matrix](outputs/OPTION_MATRIX.csv) | Decision categories |
| [Testing](docs/TESTING.md) | Reproducibility |

## Reproduce

Python 3.10+, standard library only:

```bash
python -m src.restaurant_case --check-anchors
python -m src.operational_controls
python -m unittest discover -s tests -v
python tools/verify_manifest.py
```

## For decision-makers

**Know which revenue converts into margin—and which proposed fix might destroy it.**

Ricardo Vera works on business analysis, operational intelligence, profitability diagnostics and defensible management decisions.

**Executive contact:** [richardvera084@gmail.com](mailto:richardvera084@gmail.com?subject=Business%20profitability%20diagnostic%20%7C%20CIEC%20LAB). Include your industry, the problem and the decision at stake.

[Full Spanish case](README.md) · [CIEC LAB portfolio](https://github.com/RicardoVera-Lab)
