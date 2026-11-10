"""Deterministic P&L, reconciliation and scenario study for Restaurante Horizonte.

This file is a new public implementation derived only from the four published CSVs
and from the business rules explained in docs/METHODOLOGY.md. Python stdlib only.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CENT = Decimal('0.01')
ZERO = Decimal('0')
MONTHS = tuple(f'2025-{i:02d}' for i in range(1, 13))
FILES = ('ventas_sku_mes.csv', 'operacion_mes.csv', 'gastos_mes.csv', 'inventario_mes.csv')
EXPENSES = ('labor_um', 'rent_um', 'utilities_um', 'marketing_um', 'other_opex_um')
COST_RULE = 'RECIPE_COGS_VARIABLE_WASTE_DELIVERY_OPEX_FIXED'
TARGET = 'SKU-001'

class DataError(ValueError):
    """Broken CSV contract or financial reconciliation."""


def number(value: str, field: str, *, nonnegative: bool = False) -> Decimal:
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise DataError(f'INVALID_NUMBER:{field}') from exc
    if not result.is_finite() or (nonnegative and result < ZERO):
        raise DataError(f'OUT_OF_RANGE:{field}')
    return result


def money(value: Decimal) -> str:
    return str(value.quantize(CENT, rounding=ROUND_HALF_UP))


def pct(value: Decimal) -> str:
    return str(value.quantize(CENT, rounding=ROUND_HALF_UP))


def read_data(data_dir: Path) -> dict[str, list[dict[str, str]]]:
    source: dict[str, list[dict[str, str]]] = {}
    for fname in FILES:
        path = data_dir / fname
        if not path.is_file():
            raise DataError(f'MISSING_FILE:{fname}')
        with path.open('r', encoding='utf-8-sig', newline='') as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
                raise DataError(f'INVALID_HEADER:{fname}')
            rows = list(reader)
        if any(None in row or any(value is None or value == '' for value in row.values()) for row in rows):
            raise DataError(f'EMPTY_OR_EXTRA_FIELD:{fname}')
        source[fname] = rows
    return source


def _by_month(rows: list[dict[str, str]], label: str) -> dict[str, dict[str, str]]:
    counts = Counter(row['month'] for row in rows)
    if set(counts) != set(MONTHS) or any(c != 1 for c in counts.values()):
        raise DataError(f'MONTH_COVERAGE:{label}')
    return {r['month']: r for r in rows}


def baseline(source: dict[str, list[dict[str, str]]]) -> dict:
    sales = source['ventas_sku_mes.csv']
    if len(sales) != 168 or len({r['sku'] for r in sales}) != 14:
        raise DataError('SALES_COUNT_OR_SKUS')
    keys = [(r['month'], r['sku']) for r in sales]
    if len(set(keys)) != 168 or set(r['month'] for r in sales) != set(MONTHS):
        raise DataError('DUPLICATE_OR_MISSING_SKU_MONTH')
    if any(sum(1 for k in keys if k[0] == month) != 14 for month in MONTHS):
        raise DataError('NOT_14_SKU_PER_MONTH')
    op = _by_month(source['operacion_mes.csv'], 'operations')
    expenses = _by_month(source['gastos_mes.csv'], 'expenses')
    inventory = _by_month(source['inventario_mes.csv'], 'inventory')
    monthly = {month: {'month': month, 'net': ZERO, 'gross': ZERO, 'discount': ZERO,
                       'cogs': ZERO} for month in MONTHS}
    for r in sales:
        month, sku = r['month'], r['sku']
        units = number(r['quantity_sold'], 'units', nonnegative=True)
        if units != units.to_integral_value():
            raise DataError(f'FRACTIONAL_UNITS:{month}:{sku}')
        price = number(r['unit_price_um'], 'unit_price_um', nonnegative=True)
        recipe = number(r['unit_recipe_cost_um'], 'unit_recipe_cost_um', nonnegative=True)
        gross = number(r['gross_sales_um'], 'gross_sales_um', nonnegative=True)
        discount = number(r['discount_um'], 'discount_um', nonnegative=True)
        net = number(r['net_sales_um'], 'net_sales_um', nonnegative=True)
        recipe_total = number(r['estimated_cogs_um'], 'estimated_cogs_um', nonnegative=True)
        if gross != units * price or net != gross - discount or recipe_total != units * recipe:
            raise DataError(f'SKU_RECONCILIATION:{month}:{sku}')
        if discount > gross:
            raise DataError(f'DISCOUNT_EXCEEDS_GROSS:{month}:{sku}')
        entry = monthly[month]
        for key, val in (('net', net), ('gross', gross), ('discount', discount), ('cogs', recipe_total)):
            entry[key] += val
    previous = None
    for month in MONTHS:
        entry = monthly[month]
        operations, expense, stock = op[month], expenses[month], inventory[month]
        entry['waste'] = number(operations['waste_um'], 'operations.waste_um', nonnegative=True)
        entry['delivery'] = number(operations['delivery_fees_um'], 'delivery_fees_um', nonnegative=True)
        entry['opex'] = sum((number(expense[k], k, nonnegative=True) for k in EXPENSES), ZERO)
        opening = number(stock['opening_um'], 'opening_um', nonnegative=True)
        closing = number(stock['closing_um'], 'closing_um', nonnegative=True)
        purchase = number(stock['purchases_um'], 'purchases_um', nonnegative=True)
        adjustment = number(stock['adjustments_um'], 'adjustments_um')
        inv_cogs = number(stock['consumption_um'], 'consumption_um', nonnegative=True)
        inv_waste = number(stock['waste_um'], 'inventory.waste_um', nonnegative=True)
        if inv_cogs != entry['cogs'] or inv_waste != entry['waste']:
            raise DataError(f'INVENTORY_VS_OPERATION:{month}')
        if previous is not None and opening != previous:
            raise DataError(f'INVENTORY_ROLLOVER:{month}')
        if opening + purchase - inv_cogs - inv_waste + adjustment != closing:
            raise DataError(f'INVENTORY_FORMULA:{month}')
        previous = closing
        entry['profit'] = entry['net'] - entry['cogs'] - entry['waste'] - entry['delivery'] - entry['opex']
        entry['margin_pct'] = entry['profit'] / entry['net'] * 100 if entry['net'] else ZERO
    totals = {k: sum((monthly[m][k] for m in MONTHS), ZERO)
              for k in ('net', 'gross', 'discount', 'cogs', 'waste', 'delivery', 'opex', 'profit')}
    totals['margin_pct'] = totals['profit'] / totals['net'] * 100
    return {'totals': totals, 'months': monthly}


def simulate(source: dict[str, list[dict[str, str]]], base: dict,
             option: str, volume_drop_pct: str | int | Decimal) -> dict[str, str]:
    if option not in ('H1', 'H2'):
        raise DataError('UNKNOWN_PRICE_OPTION')
    reduction = number(str(volume_drop_pct), 'volume_drop_pct', nonnegative=True) / 100
    if reduction > 1:
        raise DataError('VOLUME_DROP_ABOVE_100')
    remaining = 1 - reduction
    sales, cost = ZERO, ZERO
    for row in source['ventas_sku_mes.csv']:
        gross = number(row['gross_sales_um'], 'gross', nonnegative=True)
        discount = number(row['discount_um'], 'discount', nonnegative=True)
        original_sales = number(row['net_sales_um'], 'net', nonnegative=True)
        original_cost = number(row['estimated_cogs_um'], 'cogs', nonnegative=True)
        if option == 'H2':
            sales += (gross - discount * Decimal('0.85')) * remaining
            cost += original_cost * remaining
        elif row['sku'] == TARGET:
            sales += original_sales * Decimal('1.05') * remaining
            cost += original_cost * remaining
        else:
            sales += original_sales
            cost += original_cost
    fixed = sum((base['totals'][k] for k in ('waste', 'delivery', 'opex')), ZERO)
    result = sales - cost - fixed
    return {
        'option': option, 'volume_drop_pct': pct(reduction * 100),
        'net_sales_um': money(sales), 'recipe_cogs_um': money(cost),
        'result_um': money(result), 'delta_vs_h0_um': money(result - base['totals']['profit']),
        'cost_rule': COST_RULE,
    }


def decide(source: dict[str, list[dict[str, str]]], base: dict) -> dict:
    scenarios = {
        'H1_0pct': simulate(source, base, 'H1', 0),
        'H1_3pct': simulate(source, base, 'H1', 3),
        'H1_8pct': simulate(source, base, 'H1', 8),
        'H2_0pct': simulate(source, base, 'H2', 0),
        'H2_1pct': simulate(source, base, 'H2', 1),
        'H2_3pct': simulate(source, base, 'H2', 3),
    }
    return {
        'case_id': 'MBA-PORT-001', 'period': '2025-01/2025-12', 'cost_rule': COST_RULE,
        'baseline': {**{k + '_um': money(base['totals'][k]) for k in ('gross', 'discount', 'net', 'cogs', 'waste', 'delivery', 'opex', 'profit')},
                     'margin_pct': pct(base['totals']['margin_pct'])},
        'monthly': [{'month': m, 'net_sales_um': money(base['months'][m]['net']),
                     'profit_um': money(base['months'][m]['profit']),
                     'margin_pct': pct(base['months'][m]['margin_pct'])} for m in MONTHS],
        'scenarios': scenarios,
        'options': [
            {'option': 'H0', 'state': 'HOLD', 'delta_vs_h0_um': '0.00',
             'reason': 'Mantener comparador y medir'},
            {'option': 'H1', 'state': 'RESEARCH', 'delta_vs_h0_um': scenarios['H1_3pct']['delta_vs_h0_um'],
             'assumed_volume_drop_pct': '3.00', 'stop_at_pct': '8.00',
             'reason': 'Revisar respuesta de demanda antes de cambiar precio'},
            {'option': 'H2', 'state': 'RESEARCH', 'delta_vs_h0_um': scenarios['H2_0pct']['delta_vs_h0_um'],
             'assumed_volume_drop_pct': '0.00', 'stop_at_pct': '1.00',
             'reason': 'Investigar elasticidad y efecto de descuento'},
            {'option': 'A', 'state': 'DESIGN_PILOT', 'delta_vs_h0_um': None,
             'reason': 'Diseñar control de lotes y mermas, sin atribuir ahorro'},
            {'option': 'B', 'state': 'DESIGN_PILOT', 'delta_vs_h0_um': None,
             'reason': 'Diseñar cobertura por franja, sin atribuir ahorro'},
        ],
        'constraints': ['A_AND_B_ONE_SHARED_PILOT_SLOT', 'DO_NOT_ADD_SCENARIOS',
                        'DO_NOT_INFER_MONEY_SAVINGS_FOR_A_B', 'REQUIRE_BUSINESS_AUTHORIZATION_FOR_EXECUTION'],
    }


def executive_markdown(result: dict) -> str:
    b = result['baseline']; s = result['scenarios']; months = result['monthly']
    def fmt(v: str) -> str:
        return f"{Decimal(v):,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')
    text = [
        '# Restaurante Horizonte — informe ejecutivo reproducible', '',
        '## Problema',
        'La facturación no muestra por sí sola la calidad de la rentabilidad. Se analizaron 12 meses, 14 SKU por mes y los costos operativos conciliados.', '',
        '## Diagnóstico',
        f"- Ventas netas anuales: **{fmt(b['net_um'])} UM**.",
        f"- Resultado operativo simplificado: **{fmt(b['profit_um'])} UM**.",
        f"- Margen anual: **{str(b['margin_pct']).replace('.', ',')} %**.",
        f"- El margen pasa de **{str(months[0]['margin_pct']).replace('.', ',')} %** en enero a **{str(months[-1]['margin_pct']).replace('.', ',')} %** en diciembre.", '',
        '## Alternativas y decisiones',
        '| Opción | Supuesto | Delta vs. H0 (UM) | Estado |',
        '|---|---|---:|---|',
        '| H0 | Sin cambios | 0,00 | HOLD |',
        f"| H1 | Precio SKU-001 +5 %; unidades −3 % | +{fmt(s['H1_3pct']['delta_vs_h0_um'])} | RESEARCH |",
        f"| H2 | Descuentos −15 %; unidades sin caída | +{fmt(s['H2_0pct']['delta_vs_h0_um'])} | RESEARCH |",
        '| A | Lotes y merma | No cuantificado | DESIGN_PILOT |',
        '| B | Cobertura por franja sin bajar horas pagadas | No cuantificado | DESIGN_PILOT |', '',
        '## Pruebas que cambian la decisión',
        f"- H1 con caída de unidades del 8 %: **{fmt(s['H1_8pct']['delta_vs_h0_um'])} UM** respecto de H0: se detiene.",
        f"- H2 con caída del 1 %: **{fmt(s['H2_1pct']['delta_vs_h0_um'])} UM** respecto de H0: se detiene.", '',
        '## Regla económica',
        'Se conserva la merma, los cargos de delivery y el resto de gastos en el nivel base; solo varían ingresos y costo de receta según unidades. No se suman efectos de modelos alternativos, ni se atribuyen ahorros a A/B.', '',
        '## Decisión ejecutiva',
        'Mantener H0 como comparador, investigar H1 y H2 separadamente, y diseñar A o B para una única ventana de piloto reversible. Los escenarios de precio requieren medir respuesta de demanda y costos de implementación antes de su adopción.', '',
        '## Cómo comprobar',
        '`python -m src.restaurant_case --check-anchors` y `python -m unittest discover -s tests -v`.', '',
    ]
    return '\n'.join(text)


def anchor_check(result: dict) -> None:
    anchors = {
        ('baseline', 'net_um'): '32473404.18',
        ('baseline', 'profit_um'): '8211449.91',
    }
    for (section, key), expected in anchors.items():
        if result[section][key] != expected:
            raise DataError(f'ANCHOR_MISMATCH:{section}.{key}:{result[section][key]}')
    for key, expected in {'H1_3pct':'95150.38', 'H1_8pct':'-10419.55',
                          'H2_0pct':'114563.18', 'H2_1pct':'-82452.97'}.items():
        found = result['scenarios'][key]['delta_vs_h0_um']
        if found != expected:
            raise DataError(f'SCENARIO_MISMATCH:{key}:{found}')
    assert [r['state'] for r in result['options']] == ['HOLD','RESEARCH','RESEARCH','DESIGN_PILOT','DESIGN_PILOT']
    assert all(r['delta_vs_h0_um'] is None for r in result['options'][-2:])


def export(result: dict, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / 'RESULTS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for filename, rows, fields in (
        ('MONTHLY_METRICS.csv', result['monthly'], ('month','net_sales_um','profit_um','margin_pct')),
        ('OPTION_MATRIX.csv', result['options'], ('option','state','delta_vs_h0_um','reason','assumed_volume_drop_pct','stop_at_pct')),
    ):
        with (output_dir / filename).open('w', encoding='utf-8', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(rows)
    (output_dir / 'REGENERATED_EXECUTIVE.md').write_text(executive_markdown(result), encoding='utf-8')
    from .operational_controls import demonstration
    (output_dir / 'OPERATIONAL_CONTROLS.json').write_text(
        json.dumps(demonstration(), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Reproduce Restaurante Horizonte annual results and decisions.')
    parser.add_argument('--data-dir', type=Path, default=ROOT / 'data')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'outputs')
    parser.add_argument('--check-anchors', action='store_true', help='Verify all locked numeric anchors.')
    parser.add_argument('--no-write', action='store_true', help='Only inspect and print results.')
    args = parser.parse_args(argv)
    try:
        source = read_data(args.data_dir)
        result = decide(source, baseline(source))
        if args.check_anchors:
            anchor_check(result)
        if not args.no_write:
            export(result, args.output_dir)
    except DataError as exc:
        parser.exit(2, f'STOP: {exc}\n')
    print('CASE_ID:', result['case_id'])
    print('NET_SALES_UM:', result['baseline']['net_um'])
    print('OPERATING_RESULT_UM:', result['baseline']['profit_um'])
    print('ANNUAL_MARGIN_PCT:', result['baseline']['margin_pct'])
    print('H1_3PCT_DELTA_UM:', result['scenarios']['H1_3pct']['delta_vs_h0_um'])
    print('H2_0PCT_DELTA_UM:', result['scenarios']['H2_0pct']['delta_vs_h0_um'])
    print('H1_8PCT_NEGATIVE_UM:', result['scenarios']['H1_8pct']['delta_vs_h0_um'])
    print('H2_1PCT_NEGATIVE_UM:', result['scenarios']['H2_1pct']['delta_vs_h0_um'])
    print('ANCHORS:', 'PASS' if args.check_anchors else 'NOT_REQUESTED')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
