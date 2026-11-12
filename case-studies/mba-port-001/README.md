# Vendía más. Pero cada mes se quedaba con menos margen.

### MBA-PORT-001 | Inteligencia de rentabilidad y decisiones comerciales para restaurantes

**Ricardo Vera · CIEC LAB | Análisis empresarial e inteligencia operativa**

## ¿De qué sirve facturar más si cada venta deja menos?

En gastronomía, el peligro no siempre es que falten clientes. A veces es más difícil de detectar: **el local trabaja más, vende más y convierte cada vez menos facturación en resultado**.

Este caso pone los números sobre la mesa, identifica dónde se comprime la rentabilidad y demuestra por qué algunas decisiones comerciales aparentemente razonables pueden empeorar la situación.

[**Ver dictamen ejecutivo**](reports/EXECUTIVE_DECISION.md) · [**Examinar resultados**](outputs/RESULTS.json) · [**Solicitar diagnóstico**](mailto:richardvera084@gmail.com?subject=Diagn%C3%B3stico%20de%20rentabilidad%20%7C%20Ricardo%20Vera)

---

## El dato que debería preocupar al dueño

| Indicador del modelo | Resultado |
|---|---:|
| Ventas netas anuales | **32.473.404,18 UM** |
| Resultado operativo simplificado | **8.211.449,91 UM** |
| Margen operativo anual | **25,29 %** |
| Margen de enero | **28,35 %** |
| Margen de diciembre | **22,17 %** |
| Deterioro del margen | **−6,18 puntos porcentuales** |
| Cobertura del análisis | **14 productos · 12 meses** |

**La facturación creció. La calidad económica de esa facturación se deterioró.** La caída del margen no se explica mirando únicamente la caja.

### Dónde aparece la presión

| Costo como porcentaje de venta neta | Enero | Diciembre | Variación |
|---|---:|---:|---:|
| Costo de recetas | 36,23 % | 44,29 % | **+8,06 p. p.** |
| Merma | 0,43 % | 0,97 % | **+0,54 p. p.** |
| Delivery | 2,27 % | 3,28 % | **+1,01 p. p.** |

La dirección tiene una pregunta más útil que “¿vendemos más?”: **“¿qué está absorbiendo el margen y cuánto más podemos tolerar?”**

## La decisión comercial que parecía funcionar

Supongamos que se reducen los descuentos un **15 %**.

- Con las unidades vendidas constantes, el modelo proyecta **+114.563,18 UM** respecto de la referencia.
- Si las unidades caen apenas **1 %**, la misma medida pasa a **−82.452,97 UM** respecto de la referencia.

El cambio de resultado entre ambos escenarios es decisivo. **Una medida que luce rentable en la planilla puede destruir valor si nadie prueba su sensibilidad frente al cliente.**

También se contrastó un incremento de precio del 5 % en un producto:

| Escenario | Cambio de resultado frente a referencia |
|---|---:|
| Precio SKU-001 +5 %, unidades −3 % | **+95.150,38 UM** |
| Precio SKU-001 +5 %, unidades −8 % | **−10.419,55 UM** |
| Descuentos −15 %, unidades estables | **+114.563,18 UM** |
| Descuentos −15 %, unidades −1 % | **−82.452,97 UM** |

**Mi criterio de intervención:** ninguna política de precios debería aprobarse solo porque el escenario optimista ofrece una mejora.

## Lo que estructuré

**01 · Rentabilidad reconstruida.** Ventas, descuentos, costos por receta, inventario, merma, delivery y gastos operativos.

**02 · Ingeniería comercial.** Alternativas de precio y descuento comparadas contra la misma línea base.

**03 · Sensibilidad y condiciones de detención.** Qué pasa cuando cae la demanda y en qué escenarios conviene frenar.

**04 · Diseño de intervención.** Dos pilotos alternativos: control de lotes/merma y cobertura horaria.

**05 · Gobierno de ejecución.** Reservas, cancelaciones y reversión referenciada en un modelo demostrativo de control.

**06 · Comprobación técnica.** Fuentes CSV, cálculos deterministas en Python, pruebas automatizadas y archivos de resultados.

## Resolución de gerencia

| Alternativa | Decisión |
|---|---|
| **H0 · Mantener referencia** | Continuar midiendo |
| **H1 · Modificar precio** | Investigar respuesta de demanda |
| **H2 · Reducir descuentos** | Validar elasticidad antes de intervenir |
| **A · Reducir merma** | Diseñar piloto medible |
| **B · Ajustar cobertura horaria** | Diseñar piloto alternativo |

No asigné ahorros a los pilotos A y B sin medición. La prioridad es **probar la intervención correcta**, no sumar promesas que el dato todavía no respalda.

## Reproducí el análisis

Fuentes: [ventas por producto](data/ventas_sku_mes.csv), [operación](data/operacion_mes.csv), [gastos](data/gastos_mes.csv) e [inventario](data/inventario_mes.csv).

Resultados: [cifras y escenarios](outputs/RESULTS.json) · [indicadores mensuales](outputs/MONTHLY_METRICS.csv) · [matriz de decisión](outputs/OPTION_MATRIX.csv) · [pruebas](tests/test_restaurant_case.py) · [metodología](docs/METHODOLOGY.md).

Desde la raíz del repositorio, con Python 3.10+:

```bash
cd case-studies/mba-port-001
python -m src.restaurant_case --check-anchors
python -m src.operational_controls
python -m unittest discover -s tests -v
python tools/verify_manifest.py
```

**Ficha técnica:** modelo empresarial reproducible con datos estructurados de prueba correspondientes a 2025; los importes están expresados en unidades monetarias (UM), no en una moneda nacional.

---

## ¿Cuánto margen está perdiendo tu restaurante sin darse cuenta?

Puedo ayudarte a reconstruir el problema, identificar qué variable lo está provocando y comparar decisiones comerciales y operativas **antes de apostar la rentabilidad a una intuición**.

**Ricardo Vera | CIEC LAB** · Especialista en análisis empresarial, inteligencia operativa y decisiones de rentabilidad

[**Solicitar un diagnóstico ejecutivo de rentabilidad**](mailto:richardvera084@gmail.com?subject=Quiero%20analizar%20la%20rentabilidad%20de%20mi%20negocio) · [**English summary**](README_EN.md) · [Portafolio](../../EXECUTIVE_PORTFOLIO.md)
