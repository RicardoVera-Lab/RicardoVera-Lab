# Metodología y reglas de lectura

**Datos sintéticos generados para un caso empresarial**.

## Grano y fuentes

Una fila por mes y SKU en `ventas_sku_mes.csv` (12 × 14 = 168 filas); 12 filas por archivo de `operacion_mes.csv`, `gastos_mes.csv` e `inventario_mes.csv`. Período 2025-01 a 2025-12. No se mezclan monedas ni se extrapolan efectos fuera del período. Cada archivo está fijado por SHA-256.

## Conciliaciones no negociables

1. Por SKU: `cantidad × precio_unitario = venta_bruta`; `venta_bruta − descuento = venta_neta`; `cantidad × costo_receta_unitario = costo_receta`.
2. Por mes: suma de costo receta por SKU = consumo de inventario; merma contable = merma operativa.
3. Inventario: `apertura + compras − consumo − merma + ajuste = cierre`; el cierre de un mes debe ser igual a la apertura del siguiente.
4. Cuenta de resultados mensual: `venta_neta − receta − merma − delivery − (personal + alquiler + servicios + marketing + otros)`.
5. Margen: `resultado_operativo / venta_neta × 100`. Las conciliaciones se realizan en Decimal, con redondeo half-up a centavos **solo al presentar** el resultado.

## Sensibilidad comercial bajo un único régimen

La sensibilidad económica mantiene **merma, delivery y gastos operativos constantes** respecto de H0 y hace variar solo receta e ingreso en función de unidades. El volumen disminuye en los SKU afectados por cada alternativa:

- **H1:** aplica a `SKU-001`. Nuevo ingreso en filas afectadas: `(venta_bruta − descuento) × 1,05 × (1 − caída_unidades)`; receta: `costo_receta × (1 − caída_unidades)`. Las otras 13 SKU no se alteran.
- **H2:** aplica a las 14 SKU. Nuevo ingreso: `(venta_bruta − 0,85 × descuento) × (1 − caída_unidades)`; receta: `costo_receta × (1 − caída_unidades)`.
- **H0:** sin variación. Se comparan deltas de resultado operativo, no solo cambios de facturación.

No se suman estimaciones de escenarios económicos basados en supuestos distintos. La sensibilidad no incorpora gastos nuevos de ejecución de precio ni estima elasticidad. Un posible aumento de ventas que reduzca margen no se considera éxito.

## Reglas operativas explicativas

`src/operational_controls.py` presenta una máquina de estados acotada a **un único slot**. `FREE → RESERVED → EXECUTED`; cancelar desde `RESERVED` libera el slot. Cancelar desde `EXECUTED` produce `REVERSAL_REQUIRED_AFTER_EXECUTION` y retiene la reserva. Una reversión requiere identificadores sintácticamente válidos y una referencia exacta a la ejecución; solo después vuelve a `FREE`. Una reserva de A bloquea B y viceversa.

Los identificadores `SYN-...`, `EXE-...` y `REV-...` son referencias de ejemplo, no autenticación, autorizaciones ni comprobantes de reversión física. Este módulo no contiene lógica propietaria, firmas, controles regulatorios o lógica para producción.

## Decisión operativa

H0 `HOLD`. H1/H2 `RESEARCH` y revisión de elasticidad. A/B `DESIGN_PILOT`, mutuamente excluyentes en el slot demostrativo. No existe delta monetario atribuible a A/B; `null` es intencional. Una decisión de implementación corresponde al propietario del negocio.
