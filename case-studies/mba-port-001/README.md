# El restaurante vendía más. Pero cada venta dejaba menos margen.

### Caso ejecutivo MBA-PORT-001 · Rentabilidad, inteligencia comercial y decisiones operativas

**Ricardo Vera | Business Analysis · Operational Intelligence · CIEC LAB**

> **Facturar más no significa ganar más.** Cuando el margen se deteriora, decidir sin reconciliar costos, inventario y respuesta de la demanda puede convertir una solución atractiva en otro problema.

**El resultado:** se reconstruyeron 12 meses de actividad, se identificaron los principales componentes de la presión sobre el margen y se compararon cinco caminos de decisión mediante cálculos reproducibles, sensibilidad comercial y controles operativos.

**[Ver el dictamen ejecutivo](reports/EXECUTIVE_DECISION.md) · [Examinar los resultados](outputs/RESULTS.json) · [Reproducir los cálculos](#reproducir-el-análisis) · [Solicitar un diagnóstico](#conversación-ejecutiva)**

---

## El problema, en números

| Indicador | Hallazgo |
|:--|--:|
| Ventas netas anuales | **32.473.404,18 UM** |
| Resultado operativo simplificado anual | **8.211.449,91 UM** |
| Margen operativo anual | **25,29 %** |
| Margen operativo en enero | **28,35 %** |
| Margen operativo en diciembre | **22,17 %** |
| Deterioro enero–diciembre | **−6,18 puntos porcentuales** |
| Productos / período analizado | **14 SKU · 12 meses** |

Las ventas netas de diciembre superaban las de enero, pero el negocio retenía una menor proporción de cada venta. La pregunta correcta no era *«¿cómo hacemos para vender más?»*, sino **«¿qué está absorbiendo el margen y qué intervención conviene probar sin generar una pérdida mayor?»**

### Dónde estaba la presión

| Componente como % de ventas netas | Enero | Diciembre | Variación |
|:--|--:|--:|--:|
| Costo de receta | 36,23 % | 44,29 % | **+8,06 p. p.** |
| Merma | 0,43 % | 0,97 % | **+0,54 p. p.** |
| Delivery | 2,27 % | 3,28 % | **+1,01 p. p.** |

**Lectura gerencial:** el costo de los ingredientes es el frente principal a revisar; el desperdicio y la entrega agregan presión. La conclusión surge de conciliar ventas, consumo e inventario, no de atribuir automáticamente el problema al personal o al alquiler.

## El hallazgo que cambia una decisión comercial

**Reducir descuentos parecía una victoria inmediata.** El modelo calculó **+114.563,18 UM** frente a la situación base cuando se mantuvo el volumen de ventas. Pero al incorporar apenas **1 % de caída en unidades**, la misma iniciativa pasó a **−82.452,97 UM**.

| Decisión analizada | Supuesto de demanda | Diferencia anual contra base | Resolución |
|:--|:--|--:|:--|
| H1 · Precio de SKU-001 +5 % | Unidades −3 % | **+95.150,38 UM** | Investigar demanda |
| H1 · Prueba de estrés | Unidades −8 % | **−10.419,55 UM** | Detener ese escenario |
| H2 · Reducir descuentos 15 % | Unidades estables | **+114.563,18 UM** | Investigar demanda |
| H2 · Prueba de estrés | Unidades −1 % | **−82.452,97 UM** | Detener ese escenario |

**La diferencia entre un análisis y una decisión:** un aumento potencial de ganancias no se trata como ganancia realizada. Se incorpora el comportamiento posible del cliente, se calcula el costo del error y se decide qué información falta antes de tocar un precio.

## Qué se construyó

**01 · Diagnóstico financiero.** Reconstrucción de ventas, descuentos, costo de recetas, merma, delivery, gastos, resultado y márgenes por mes.

**02 · Conciliación de inventario.** Cruce entre unidades vendidas, consumo de ingredientes, movimientos de inventario y desperdicios; las inconsistencias detienen el proceso.

**03 · Ingeniería comercial.** Escenarios de precio y descuentos con sensibilidad al volumen, comparación contra una referencia común y condiciones de detención.

**04 · Diseño operativo.** Dos líneas de intervención —control de lotes/mermas y redistribución de horarios— tratadas como pilotos alternativos, con indicadores y criterios de aceptación.

**05 · Gobierno de ejecución.** Controles demostrables para reservar una intervención, impedir superposiciones, cancelar antes de ejecutar y exigir reversión documentada después de ejecutar.

**06 · Verificación reproducible.** Cuatro fuentes CSV, código Python sin paquetes externos, pruebas automatizadas y resultados regenerables a partir de los mismos insumos.

## Decisión ejecutiva

| Alternativa | Resolución | Próximo movimiento |
|:--|:--|:--|
| H0 · Mantener referencia | **HOLD** | Seguir midiendo contra la base |
| H1 · Ajustar precio | **RESEARCH** | Medir sensibilidad de la demanda |
| H2 · Reducir descuentos | **RESEARCH** | Comprobar respuesta de clientes |
| A · Controlar lotes y merma | **DESIGN PILOT** | Diseñar prueba con indicadores |
| B · Redistribuir cobertura horaria | **DESIGN PILOT** | Preparar piloto alternativo |

Las opciones A y B compiten por una sola ventana de prueba. No se les atribuye un ahorro monetario sin cálculo. La decisión evita sumar beneficios incompatibles o ejecutar una medida solo porque se ve atractiva en una planilla.

## Evidencia que un decisor puede revisar

| Entregable | Qué permite verificar |
|:--|:--|
| [Cuenta de resultados y escenarios](outputs/RESULTS.json) | Montos, supuestos y sensibilidades exactos |
| [Serie de indicadores mensuales](outputs/MONTHLY_METRICS.csv) | Evolución de ventas, resultado y margen |
| [Matriz de alternativas](outputs/OPTION_MATRIX.csv) | Opciones, criterios y decisiones |
| [Informe ejecutivo](reports/EXECUTIVE_DECISION.md) | Diagnóstico y recomendación gerencial |
| [Metodología](docs/METHODOLOGY.md) | Reglas contables, alcance y supuestos |
| [Pruebas](tests/test_restaurant_case.py) | Conciliaciones, escenarios y casos adversos |
| [Control operativo](src/operational_controls.py) | Cancelación, reserva y reversión |

**Base del caso:** 168 registros mensuales por producto y 36 registros operativos, de gastos e inventario; datos sintéticos, período enero–diciembre de 2025; cifras expresadas en unidades monetarias (UM). La metodología explica las reglas del modelo en detalle.

## Reproducir el análisis

**Requisito:** Python 3.10+; únicamente biblioteca estándar.

```bash
python -m src.restaurant_case --check-anchors
python -m src.operational_controls
python -m unittest discover -s tests -v
python tools/verify_manifest.py
```

En Windows, reemplazar `python` por `py -3` si corresponde. La ejecución recalcula los resultados en `outputs/`. La validación automatizada se define en `.github/workflows/validate.yml`. Ver [instrucciones de pruebas](docs/TESTING.md).

## La pregunta para tu empresa

**¿Sabés qué parte de tu facturación se está convirtiendo en margen y cuál se está perdiendo por costos, mermas, precios, inventario o ejecución?**

Un diagnóstico serio debería entregarte algo más útil que gráficos: **cifras reconciliadas, riesgos medidos, alternativas comparables y una decisión accionable**.

### Conversación ejecutiva

**Ricardo Vera** — Análisis de negocios, inteligencia operativa y apoyo a decisiones de gestión.

**Consultoría:** diagnóstico de rentabilidad, análisis de costos y productos, evaluación comercial, controles operativos y modelos de decisión reproducibles.

**Contacto:** [richardvera084@gmail.com](mailto:richardvera084@gmail.com?subject=Diagn%C3%B3stico%20de%20rentabilidad%20%7C%20CIEC%20LAB)

Para iniciar, enviá **el problema de negocio, el sector y la decisión que necesitás tomar**. El objetivo de la primera conversación es delimitar un diagnóstico útil y sus entregables.

**[English executive summary](README_EN.md) · [Más trabajos de CIEC LAB](https://github.com/RicardoVera-Lab)**
