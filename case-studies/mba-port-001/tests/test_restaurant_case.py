import csv
import hashlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from decimal import Decimal
from pathlib import Path

from src.restaurant_case import (ROOT, DataError, anchor_check, baseline, decide,
                                 executive_markdown, read_data, simulate, money)
from src.operational_controls import PilotSlot, ControlStop, canonical_id, demonstration

FROZEN = {
    'gastos_mes.csv': '9feaaeb1dd51396869a39dd20db0f6dc9e3ab1df2cd27a0c24a03385d9e33ec5',
    'inventario_mes.csv': '4980c09617ee64ee544a3f81209d2dd612d1ba8ba4f892d5da6db0b728995ac9',
    'operacion_mes.csv': '9e04caaa89cb98d111e4eb1a2c127d247037d4ce0aaa47a1fe00c9722dedfea7',
    'ventas_sku_mes.csv': '5affe35a93c6aa3c1036adc70399638d2a7eb0bb4887687cb3818840cbf2cd27',
}

class FinancialReconciliation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = read_data(ROOT / 'data')
        cls.base = baseline(cls.source)
        cls.result = decide(cls.source, cls.base)

    def test_four_data_sources_are_byte_frozen(self):
        for filename, sha in FROZEN.items():
            with self.subTest(filename=filename):
                self.assertEqual(hashlib.sha256((ROOT/'data'/filename).read_bytes()).hexdigest(), sha)

    def test_12_x_14_grain_and_four_sources(self):
        self.assertEqual(len(self.source['ventas_sku_mes.csv']), 168)
        for fname in ('operacion_mes.csv','gastos_mes.csv','inventario_mes.csv'):
            self.assertEqual(len(self.source[fname]), 12)
        self.assertEqual(len(self.base['months']), 12)

    def test_baseline_reconciled_to_cents(self):
        self.assertEqual(self.result['baseline']['net_um'], '32473404.18')
        self.assertEqual(self.result['baseline']['profit_um'], '8211449.91')
        self.assertEqual(self.result['baseline']['margin_pct'], '25.29')
        anchor_check(self.result)

    def test_margin_deterioration(self):
        rows = self.result['monthly']
        self.assertEqual(rows[0]['margin_pct'], '28.35')
        self.assertEqual(rows[-1]['margin_pct'], '22.17')
        self.assertGreater(Decimal(rows[0]['margin_pct']), Decimal(rows[-1]['margin_pct']))

    def test_h1_profit_gain_with_three_percent_volume_loss(self):
        self.assertEqual(self.result['scenarios']['H1_3pct']['delta_vs_h0_um'], '95150.38')
        self.assertEqual(self.result['scenarios']['H1_3pct']['result_um'], '8306600.29')

    def test_h2_profit_gain_only_under_zero_volume_loss(self):
        self.assertEqual(self.result['scenarios']['H2_0pct']['delta_vs_h0_um'], '114563.18')
        self.assertEqual(self.result['scenarios']['H2_0pct']['result_um'], '8326013.09')

    def test_h1_eight_percent_volume_loss_negative(self):
        self.assertEqual(self.result['scenarios']['H1_8pct']['delta_vs_h0_um'], '-10419.55')

    def test_h2_one_percent_volume_loss_negative(self):
        self.assertEqual(self.result['scenarios']['H2_1pct']['delta_vs_h0_um'], '-82452.97')

    def test_h2_three_percent_loss_frozen_costs(self):
        self.assertEqual(self.result['scenarios']['H2_3pct']['delta_vs_h0_um'], '-476485.27')

    def test_five_decisions_and_undefined_a_b_savings(self):
        self.assertEqual([(o['option'],o['state']) for o in self.result['options']],
                         [('H0','HOLD'),('H1','RESEARCH'),('H2','RESEARCH'),
                          ('A','DESIGN_PILOT'),('B','DESIGN_PILOT')])
        self.assertIsNone(self.result['options'][3]['delta_vs_h0_um'])
        self.assertIsNone(self.result['options'][4]['delta_vs_h0_um'])

    def test_h1_uses_only_target_sku(self):
        h1 = simulate(self.source, self.base, 'H1', 0)
        self.assertEqual(h1['delta_vs_h0_um'], '158492.34')

    def test_invalid_scenario_and_pct_stop(self):
        for option, drop in [('H0','0'),('H2','-1'),('H1','101'),('H1','NaN')]:
            with self.subTest(option=option, drop=drop), self.assertRaises(DataError):
                simulate(self.source, self.base, option, drop)

    def test_tamper_units_detected(self):
        altered = deepcopy(self.source)
        altered['ventas_sku_mes.csv'][0]['quantity_sold'] = '132'
        with self.assertRaisesRegex(DataError,'SKU_RECONCILIATION'):
            baseline(altered)

    def test_fractional_units_detected(self):
        altered = deepcopy(self.source)
        altered['ventas_sku_mes.csv'][0]['quantity_sold'] = '131.5'
        with self.assertRaisesRegex(DataError,'FRACTIONAL_UNITS'):
            baseline(altered)

    def test_inventory_bad_monthly_consumption_detected(self):
        altered = deepcopy(self.source)
        altered['inventario_mes.csv'][0]['consumption_um'] = '0.00'
        with self.assertRaisesRegex(DataError,'INVENTORY_VS_OPERATION'):
            baseline(altered)

    def test_inventory_rolling_balance_detected(self):
        altered = deepcopy(self.source)
        altered['inventario_mes.csv'][1]['opening_um'] = '772001.00'
        with self.assertRaisesRegex(DataError,'INVENTORY_ROLLOVER'):
            baseline(altered)

    def test_missing_sku_month_detected(self):
        altered = deepcopy(self.source)
        altered['ventas_sku_mes.csv'].pop()
        with self.assertRaises(DataError):
            baseline(altered)

    def test_missing_file_stops(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(DataError,'MISSING_FILE'):
                read_data(Path(d))

    def test_revenue_not_sufficient_for_decision(self):
        self.assertIn('El margen pasa', executive_markdown(self.result))
        self.assertLess(Decimal(self.result['scenarios']['H2_1pct']['delta_vs_h0_um']), 0)

    def test_entrypoint_run_from_repo(self):
        with tempfile.TemporaryDirectory() as d:
            proc = subprocess.run([sys.executable,'-m','src.restaurant_case',
                                   '--check-anchors','--output-dir',d],cwd=ROOT,
                                  capture_output=True,text=True,check=False)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn('ANCHORS: PASS', proc.stdout)
            self.assertTrue((Path(d)/'RESULTS.json').is_file())
            self.assertTrue((Path(d)/'OPERATIONAL_CONTROLS.json').is_file())

    def test_mutated_disk_csv_fails_entrypoint(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)
            for src in (ROOT/'data').glob('*.csv'):
                shutil.copyfile(src,target/src.name)
            data=(target/'ventas_sku_mes.csv').read_text('utf-8')
            (target/'ventas_sku_mes.csv').write_text(data.replace(',131,1950.00',',132,1950.00',1),'utf-8')
            proc=subprocess.run([sys.executable,'-m','src.restaurant_case','--data-dir',d,
                                 '--no-write'],cwd=ROOT,capture_output=True,text=True,check=False)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn('STOP:', proc.stderr)


class PublicPilotControls(unittest.TestCase):
    def test_precancel_releases_pilot(self):
        slot=PilotSlot()
        self.assertEqual(slot.reserve('SYN-A'), 'RESERVED')
        self.assertEqual(slot.cancel('SYN-A'),'RELEASED_PRE_EXECUTION')
        self.assertEqual(slot.status,'FREE')
        slot.reserve('SYN-B')

    def test_after_execution_cancel_stops_and_keeps_slot(self):
        slot=PilotSlot();slot.reserve('SYN-A');slot.execute('SYN-A','EXE-1')
        with self.assertRaisesRegex(ControlStop,'REVERSAL_REQUIRED'):
            slot.cancel('SYN-A')
        self.assertEqual(slot.status,'EXECUTED')
        with self.assertRaisesRegex(ControlStop,'SLOT_OCCUPIED'):
            slot.reserve('SYN-B')

    def test_matched_rollback_releases_slot(self):
        slot=PilotSlot();slot.reserve('SYN-A');slot.execute('SYN-A','EXE-1')
        self.assertEqual(slot.rollback('SYN-A','EXE-1','REV-1'), 'RELEASED_AFTER_MATCHED_REVERSAL')
        self.assertEqual(slot.status,'FREE')

    def test_wrong_rollback_reference_stops(self):
        slot=PilotSlot();slot.reserve('SYN-A');slot.execute('SYN-A','EXE-1')
        with self.assertRaisesRegex(ControlStop,'INVALID_REVERSAL_REFERENCE'):
            slot.rollback('SYN-A','EXE-2','REV-1')
        self.assertEqual(slot.status,'EXECUTED')

    def test_empty_and_noncanonical_identifiers_fail(self):
        for bad in ('','  ','abc','SYN a','SYN-',' SYN-A','SYN-Á','SYN-a',None,3):
            with self.subTest(bad=bad),self.assertRaises(ControlStop):
                canonical_id(bad)

    def test_duplicate_reservation_blocked(self):
        slot=PilotSlot();slot.reserve('SYN-A')
        with self.assertRaisesRegex(ControlStop,'SLOT_OCCUPIED'):
            slot.reserve('SYN-B')

    def test_foreign_cancel_rejected(self):
        slot=PilotSlot();slot.reserve('SYN-A')
        with self.assertRaisesRegex(ControlStop,'OWNER_MISMATCH'):
            slot.cancel('SYN-B')
        self.assertEqual(slot.status,'RESERVED')

    def test_demonstration_returns_positive_and_negative(self):
        result=demonstration()
        self.assertEqual(result['slot_after_pre_cancel'],'FREE')
        self.assertTrue(result['post_execution_slot_retained'])
        self.assertTrue(result['invalid_id_rejected'])
        self.assertEqual(result['slot_after_valid_reversal'],'FREE')

if __name__ == '__main__':
    unittest.main()
