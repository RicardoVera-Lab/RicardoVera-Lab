# Methodology and measurement rules

## Case scope

Patio del Molino is a constructed restaurant test case. This publication uses the **October 2026** operational diagnostic produced by the SIPER-X application and the consolidated executive analysis. Figures are in **monetary units (UM)**. Its purpose is to make the financial checks and decision framing inspectable.

## Source alignment

- **4,444,400 UM**: reported POS sales.
- **1,911,092 UM**: declared purchases/inputs. This is **not** independently established consumed ingredient cost by recipe.
- **2,381,310 UM**: declared operating expenses as supplied in the case.
- **40,000 / 68,000 UM**: previous/current refund **amounts**; no event counts inferred.
- **80.04/100**: output of an internal weighted screening index; the public snippet does not recalculate this proprietary indicator.
- **13 hypotheses**: operational screening candidates, prioritized and evaluated separately.
- **35 distinct customer IDs**: confirmed unique IDs; classifications differ by taxonomy, which does not prove longitudinal change.
- **K11 ticket average**: not evaluable with the current transaction-identity contract; it is not a measured zero.

## Reconstructed financial result

1. Gross proxy = sales − declared purchases = **2,533,308 UM**.
2. Simplified operating result = gross proxy − operating expenses = **151,998 UM**.
3. Simplified margin = result / sales × 100 = **3.42%**.
4. With declared purchases × 1.08 and the other amounts fixed, simplified result = **−889.36 UM**.
5. Refund amount change = (68,000 / 40,000 − 1) × 100 = **70% in amount**, not transactions.

We deliberately **do not** add refund amounts, inventory variance and waste percentages as separate losses, because their populations may overlap. We do not calculate a full accounting break-even point without reconciled fixed/variable expense structure.

## Data published

- `data/financial_snapshot.csv` — five aggregate financial measures.
- `data/kri_snapshot.csv` — sixteen screening indicators, including availability status.
- `src/reproduce.py` — deterministic standard-library arithmetic and validity checks.
- `tests/test_case.py` — eight public numeric and interpretation tests.
- `reports/EXECUTIVE_BRIEF.md` — management priorities and four-week plan.

No individual names, transaction records, client contacts or proprietary application components are necessary to replicate the public financial checks.

## To reproduce

    python case-studies/patio-del-molino/src/reproduce.py
    python -m unittest discover -s case-studies/patio-del-molino/tests -v
