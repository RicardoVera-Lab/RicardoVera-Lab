# Higher sales. Lower margin. The numbers tell you where to look.

### MBA-PORT-001 | Restaurant profitability & commercial decision intelligence

**Ricardo Vera · CIEC LAB | Business Analysis · Operational Intelligence**

## When revenue rises but margin falls, what are you really growing?

An operation can look healthy on its sales report while its ability to convert revenue into operating results is weakening.

This restaurant case reconstructs **12 months across 14 products**, reconciles cost and sales data, and tests commercial interventions against demand sensitivity.

| Decision metric | Reconstructed result |
|---|---:|
| Annual net sales | **32,473,404.18 UM** |
| Simplified annual operating result | **8,211,449.91 UM** |
| Annual margin | **25.29%** |
| January margin | **28.35%** |
| December margin | **22.17%** |
| Margin erosion | **6.18 percentage points** |

### One decision, two very different outcomes

A modeled **15% reduction in discounts** improves operating result by **114,563.18 UM** if unit demand remains unchanged. A mere **1% decrease in units** reverses the result to **−82,452.97 UM versus baseline**.

A **5% price increase on SKU-001** generates **+95,150.38 UM** at a 3% unit decline but **−10,419.55 UM** at an 8% unit decline.

**The management lesson:** a policy should survive a reasonable stress test before it changes the business.

## What I demonstrate

- **Reconciliation:** sales, inventory, recipe costs, waste, delivery and operating expenses.
- **Commercial evaluation:** price and discount sensitivities on a common baseline.
- **Decision discipline:** hold, research or design a controlled pilot — no invented savings.
- **Operational controls:** example pilot-slot reservation, cancellation and referenced reversal.
- **Verification:** repeatable Python calculations, frozen inputs, automated tests and documented methodology.

[**Executive decision**](reports/EXECUTIVE_DECISION.md) · [**Results**](outputs/RESULTS.json) · [**Tests**](docs/TESTING.md) · [**Methodology**](docs/METHODOLOGY.md).

From the repository root:

```bash
cd case-studies/mba-port-001
python -m src.restaurant_case --check-anchors
python -m src.operational_controls
python -m unittest discover -s tests -v
python tools/verify_manifest.py
```

**Case basis:** structured 2025 test data, with financial results in monetary units (UM).

## Know what is consuming margin before you change prices.

**Ricardo Vera | CIEC LAB** · Business Analysis & Operational Intelligence

[**Discuss a profitability diagnostic**](mailto:richardvera084@gmail.com?subject=Restaurant%20profitability%20diagnostic) · [Full case in Spanish](README.md) · [Executive portfolio](../../EXECUTIVE_PORTFOLIO.md)
