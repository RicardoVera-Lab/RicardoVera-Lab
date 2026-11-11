"""Reconstruct public financial checks from the case snapshot; no third-party packages."""
from pathlib import Path
from decimal import Decimal, InvalidOperation
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "financial_snapshot.csv"
KRI = ROOT / "data" / "kri_snapshot.csv"
MONEY = Decimal("0.01")


def load_money():
    values = {}
    with INPUT.open("r", encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            key = row["metric"]
            if key in values:
                raise ValueError("DUPLICATE_METRIC:" + key)
            try:
                number = Decimal(row["amount_um"])
            except InvalidOperation as exc:
                raise ValueError("INVALID_AMOUNT:" + key) from exc
            if not number.is_finite() or number < 0:
                raise ValueError("INVALID_AMOUNT:" + key)
            values[key] = number
    needed = {"net_sales", "declared_purchases", "operating_expenses", "refunds_current", "refunds_previous"}
    if set(values) != needed:
        raise ValueError("MISSING_OR_EXTRA_METRICS")
    return values


def build():
    v = load_money()
    if v["net_sales"] == 0 or v["refunds_previous"] == 0:
        raise ValueError("ZERO_DENOMINATOR")
    gross_proxy = v["net_sales"] - v["declared_purchases"]
    result = gross_proxy - v["operating_expenses"]
    margin_pct = (result * 100 / v["net_sales"]).quantize(MONEY)
    shock_cost = v["declared_purchases"] * Decimal("1.08")
    shocked_result = (v["net_sales"] - shock_cost - v["operating_expenses"]).quantize(MONEY)
    refund_value_change_pct = ((v["refunds_current"] / v["refunds_previous"] - 1) * 100).quantize(MONEY)
    with KRI.open("r", encoding="utf-8", newline="") as stream:
        indicators = list(csv.DictReader(stream))
    if len(indicators) != 16 or len({row["indicator"] for row in indicators}) != 16:
        raise ValueError("INVALID_INDICATOR_SET")
    unavailable = {row["indicator"] for row in indicators if row["admissible"] == "false"}
    if unavailable != {"K11"}:
        raise ValueError("UNEXPECTED_UNAVAILABLE_METRICS")
    return {
        "net_sales_um": str(v["net_sales"]),
        "gross_margin_proxy_um": str(gross_proxy),
        "simplified_operating_result_um": str(result),
        "simplified_operating_margin_pct": str(margin_pct),
        "purchase_cost_shock_pct": "8",
        "result_after_cost_shock_um": str(shocked_result),
        "refund_amount_change_pct": str(refund_value_change_pct),
        "refundable_event_count_inferred": False,
        "kri_count": len(indicators),
        "ticket_average_evaluable": False
    }


if __name__ == "__main__":
    print(json.dumps(build(), indent=2, ensure_ascii=False))
