# SIPER-AGRO | Evidence, reproducibility and scope

## Documentary contract

The published case reproduces seven explicitly linked comparisons in four families: inventory, settlements, logistics and prices. Every record has a relation identifier and declared unit. The arithmetic uses Python `decimal.Decimal`, explicit links and deterministic input validation.

**Results in scope:** three documentary discrepancies (**−2 TN**, **−500 ARS**, **+200 ARS**), two commercial price spreads (**−10 / +5 ARS/TN**) and two numerical matches. Price spreads are classified `PRICE_CONTEXT`, not `REVIEW`, because comparing a selling price with a purchase price does not by itself establish an exception.

## Source records and reference

- **Record type:** structured synthetic operational test case; not a customer engagement.
- **Reference package:** private G10F example with six XLSX input categories, explicit relation schema and a restricted report.
- **Case date:** 2026-11-12.
- **Period modelled:** 2026-02-01 inclusive to 2026-03-01 exclusive.
- **Preflight:** CALCULATED; no reported intake issues. Linked coverage: inventory 6/6, settlements 5/5, logistics 5/5, prices 4/4.

The public [transaction sample](../data/synthetic_transactions.csv), [reproduction module](../src/reproduce.py), [expected output](../results/expected.json) and [nine tests](../tests/test_reproduce.py) allow independent confirmation of the seven figures and classification rules.

## Application and validation scope

The operational application runs locally and is separate from the published numerical reproduction. Windows W7 integration previously returned `WINDOWS_PASS_CANDIDATE` with manifest and gate checks marked PASS in the owner's reported console run. A complete public Windows validation bundle is not attached to this case.

The public reproduction validates the documented arithmetic and input checks; it does not evaluate the private application, its full risk model, ingestion controls, reporting renderer or production deployment.

Legacy IRO, 12 KRIs, MCC and PFO-Lite models are not validated against G10F inputs in this public release. The wider sector workflow has 41 outstanding decisions to resolve before full business-domain approval.

## Interpretation rules

- A documentary discrepancy requires source reconciliation; it is not a confirmed financial loss.
- A commercial price spread requires comparable product, quality, volume, contractual and tax bases.
- A numerical match is limited to the specified record pair.
- Units cannot be mixed or converted implicitly.
- A management adjustment requires supporting documents and authorized review.

[**Management brief**](DECISION_BRIEF_ES.md) · [**Case overview**](../README.md)
