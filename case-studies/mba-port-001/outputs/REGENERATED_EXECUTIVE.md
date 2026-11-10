# Restaurante Horizonte — informe ejecutivo reproducible

## Problema
La facturación no muestra por sí sola la calidad de la rentabilidad. Se analizaron 12 meses, 14 SKU por mes y los costos operativos conciliados.

## Diagnóstico
- Ventas netas anuales: **32.473.404,18 UM**.
- Resultado operativo simplificado: **8.211.449,91 UM**.
- Margen anual: **25,29 %**.
- El margen pasa de **28,35 %** en enero a **22,17 %** en diciembre.

## Alternativas y decisiones
| Opción | Supuesto | Delta vs. H0 (UM) | Estado |
|---|---|---:|---|
| H0 | Sin cambios | 0,00 | HOLD |
| H1 | Precio SKU-001 +5 %; unidades −3 % | +95.150,38 | RESEARCH |
| H2 | Descuentos −15 %; unidades sin caída | +114.563,18 | RESEARCH |
| A | Lotes y merma | No cuantificado | DESIGN_PILOT |
| B | Cobertura por franja sin bajar horas pagadas | No cuantificado | DESIGN_PILOT |

## Pruebas que cambian la decisión
- H1 con caída de unidades del 8 %: **-10.419,55 UM** respecto de H0: se detiene.
- H2 con caída del 1 %: **-82.452,97 UM** respecto de H0: se detiene.

## Regla económica
Se conserva la merma, los cargos de delivery y el resto de gastos en el nivel base; solo varían ingresos y costo de receta según unidades. No se suman efectos de modelos alternativos, ni se atribuyen ahorros a A/B.

## Decisión ejecutiva
Mantener H0 como comparador, investigar H1 y H2 separadamente, y diseñar A o B para una única ventana de piloto reversible. Los escenarios de precio requieren medir respuesta de demanda y costos de implementación antes de su adopción.

## Cómo comprobar
`python -m src.restaurant_case --check-anchors` y `python -m unittest discover -s tests -v`.
