# El restaurante facturó 4,44 millones. Le quedaron 151.998.

### SIPER-X + CIEC LAB | Diagnóstico operativo convertido en decisión empresarial

**Ricardo Vera — Business Analysis · Operational Intelligence · Decision Systems**

> **La pregunta no era si el restaurante tenía problemas. Era cuál podía consumir primero su margen y qué evidencia necesitaba la dirección para actuar.**

[**Executive summary in English**](README_EN.md) · [**Informe gerencial**](reports/EXECUTIVE_BRIEF.md) · [**Reproducir cifras**](src/reproduce.py) · [**Contactar**](mailto:richardvera084@gmail.com?subject=Diagn%C3%B3stico%20empresarial%20%7C%20CIEC%20LAB)

## 01 | El diagnóstico, en números

| Indicador | Resultado |
|---|---:|
| Ventas del período | **4.444.400 UM** |
| Compras/insumos declarados | **1.911.092 UM** |
| Margen bruto aproximado por diferencia | **2.533.308 UM** |
| Gastos operativos declarados | **2.381.310 UM** |
| **Resultado operativo simplificado** | **151.998 UM** |
| **Margen operativo simplificado** | **3,42 %** |
| Índice interno de riesgo operativo | **80,04 / 100** |
| Hipótesis operativas a investigar | **13** |
| Clientes con identificador único | **35** |

**En otras palabras:** sobre cada 100 UM de ventas, el modelo deja **3,42 UM** después de las compras declaradas y gastos incluidos. Con tan poco margen, una variación pequeña de costos merece investigación prioritaria.

## 02 | La sensibilidad que cambia la conversación

**¿Qué ocurre si los insumos cuestan 8 % más y el resto permanece igual?**

| Escenario | Resultado simplificado |
|---|---:|
| Situación base | **+151.998 UM** |
| Compras/insumos +8 % | **−889,36 UM** |

Este cálculo no depende de una promesa de ahorro. Muestra **cuán estrecho es el margen de maniobra** y justifica revisar recetas, compras, inventario y estructura de gastos antes de una decisión comercial precipitada.

## 03 | Las señales que valía la pena investigar

- **Merma declarada:** 14,7 %.
- **Diferencia inventario/sistema:** 6,4 %.
- **Food cost de carta:** 43 %.
- **Variación del importe de reembolsos:** +70 %, de 40.000 a 68.000 UM; **no es** la cantidad de operaciones anuladas.
- **Diferencia caja/ticket:** 9,3 %.
- **Variación del gasto operativo:** +19 %.

No se sumaron tasas, diferencias de inventario y reembolsos como si fueran pérdidas independientes. La misma operación puede aparecer en más de un indicador.

## 04 | De 13 señales a 5 líneas de decisión

| Prioridad | Decisión | Qué se necesita para actuar |
|---|---|---|
| 1. Rentabilidad por plato | **Investigar** | Recetas, compras, consumo real, inventario y estructura de gastos |
| 2. Caja y reembolsos | **Investigar** | Comprobantes, identificadores y conciliación operación por operación |
| 3. Stock y merma | **Diseñar piloto** | Conteos físicos, movimientos y registros de descarte por insumo |
| 4. Carta y bebidas | **Diseñar piloto** | Mix comercial por operación, precios y contribución por producto |
| 5. Clientes | **Investigar / mantener** | Identificadores y períodos comparables; no inferir cambios de lealtad de una sola foto |

**La decisión relevante:** el índice de riesgo prioriza la investigación; no sustituye una autorización gerencial. Cada frente tiene condiciones de evidencia y detención.

## 05 | Lo que desarrollamos

**SIPER-X:** aplicación web local que ordena ventas e indicadores, identifica alertas, prepara un informe y exporta un expediente trazable.

**CIEC LAB:** revisión y conciliación económica, análisis de hipótesis, comprobación de métricas, evaluación de alternativas y diseño del plan gerencial.

**Ricardo Vera:** dirección del problema de negocio, integración del análisis y presentación del criterio de decisión.

El repositorio muestra el **resultado verificable de esa integración**: cifras públicas de la prueba, controles y metodología. La aplicación local y los mecanismos internos no forman parte del código publicado.

## 06 | Cuatro semanas para convertir el diagnóstico en ejecución

**Semana 1:** recopilar fuentes, identificadores y registros originales. **Semana 2:** conciliar costos, caja, stock y la línea base. **Semana 3:** diseñar pilotos reversibles con indicadores y reglas de detención. **Semana 4:** comparar resultados y elevar una decisión documentada.

[**Abrir informe ejecutivo completo**](reports/EXECUTIVE_BRIEF.md)

## 07 | Reproducción pública

Python 3.10+, biblioteca estándar. La reconstrucción se calcula a partir del conjunto financiero del caso:

    python case-studies/patio-del-molino/src/reproduce.py
    python -m unittest discover -s case-studies/patio-del-molino/tests -v

[Fuente financiera](data/financial_snapshot.csv) · [Indicadores operativos](data/kri_snapshot.csv) · [Metodología](docs/METHODOLOGY.md) · [Pruebas](tests/test_case.py)

Los valores proceden de un escenario de prueba de restaurante, documentado en la metodología. La lectura financiera es una **aproximación gerencial**, no una contabilidad de costos por recetas cerrada.

---

## La pregunta para tu empresa

**¿Tenés ventas, pero no sabés qué está consumiendo el margen? ¿Conocés las alertas, pero no sabés qué decisión justificar?**

Puedo ayudarte a ordenar los datos, localizar presiones económicas y comparar alternativas con indicadores verificables.

**Ricardo Vera · CIEC LAB**

[**Solicitar un diagnóstico de negocio**](mailto:richardvera084@gmail.com?subject=CIEC%20LAB%20%7C%20Diagn%C3%B3stico%20de%20rentabilidad) · [**Ver portafolio**](../../EXECUTIVE_PORTFOLIO.md)
