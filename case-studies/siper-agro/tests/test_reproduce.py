"""Reproduction and negative controls; standard Python library only."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from reproduce import DATA, compute  # noqa: E402

EXPECTED = {
    ("inventory", "INV-1"): ("-2", "TN"),
    ("settlements", "LIQ-1"): ("-500", "ARS"),
    ("settlements", "LIQ-2"): ("0", "ARS"),
    ("logistics", "COST-1"): ("200", "ARS"),
    ("logistics", "COST-2"): ("0", "ARS"),
    ("prices", "PRECIO-1"): ("-10", "ARS/TN"),
    ("prices", "PRECIO-2"): ("5", "ARS/TN"),
}


class SyntheticReconciliationTest(unittest.TestCase):
    def test_all_seven_documentary_comparisons(self):
        actual = {(r["family"], r["relation_id"]): (r["difference"], r["unit"]) for r in compute()}
        self.assertEqual(actual, EXPECTED)

    def test_four_distinct_families(self):
        self.assertEqual(len({r["family"] for r in compute()}), 4)

    def test_unresolved_not_equivalent_to_loss(self):
        self.assertEqual(sum(r["status"] == "REVIEW" for r in compute()), 5)
        self.assertEqual(sum(r["status"] == "MATCH" for r in compute()), 2)

    def change_and_check(self, change, expected_error=True):
        with DATA.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            rows = list(reader)
            cols = reader.fieldnames
        change(rows)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "synthetic.csv"
            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=cols)
                writer.writeheader()
                writer.writerows(rows)
            if expected_error:
                with self.assertRaises(ValueError):
                    compute(path)
            else:
                return compute(path)

    def test_missing_explicit_relation_is_rejected(self):
        self.change_and_check(lambda rows: rows[0].update(relation_id=""))

    def test_unit_mismatch_is_rejected(self):
        self.change_and_check(lambda rows: rows[0].update(unit="KG"))

    def test_duplicate_record_is_rejected(self):
        self.change_and_check(lambda rows: rows.append(rows[0].copy()))

    def test_invalid_role_is_rejected(self):
        self.change_and_check(lambda rows: rows[0].update(role="fabricated"))

    def test_missing_closing_record_is_rejected(self):
        self.change_and_check(lambda rows: rows.__setitem__(slice(None), [r for r in rows if r["role"] != "closing"]))

    def test_mutated_source_changes_arithmetic(self):
        altered = self.change_and_check(lambda rows: rows[0].update(value="101"), expected_error=False)
        inventory = next(r for r in altered if r["family"] == "inventory")
        self.assertEqual(inventory["difference"], "-3")


if __name__ == "__main__":
    unittest.main()
