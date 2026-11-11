"""Tests for the public Patio del Molino financial reconstruction."""
from pathlib import Path
import runpy
import unittest

ROOT = Path(__file__).resolve().parents[1]
compute = runpy.run_path(str(ROOT / "src" / "reproduce.py"))
build = compute["build"]


class ExecutiveCase(unittest.TestCase):
    def setUp(self):
        self.r = build()

    def test_sales_anchor(self):
        self.assertEqual(self.r["net_sales_um"], "4444400")

    def test_gross_proxy(self):
        self.assertEqual(self.r["gross_margin_proxy_um"], "2533308")

    def test_result(self):
        self.assertEqual(self.r["simplified_operating_result_um"], "151998")

    def test_margin(self):
        self.assertEqual(self.r["simplified_operating_margin_pct"], "3.42")

    def test_cost_shock(self):
        self.assertEqual(self.r["result_after_cost_shock_um"], "-889.36")

    def test_refund_metric_measures_value_not_count(self):
        self.assertEqual(self.r["refund_amount_change_pct"], "70.00")
        self.assertFalse(self.r["refundable_event_count_inferred"])

    def test_missing_ticket_measure_not_zero(self):
        self.assertFalse(self.r["ticket_average_evaluable"])

    def test_all_indicators_present(self):
        self.assertEqual(self.r["kri_count"], 16)


if __name__ == "__main__":
    unittest.main()
