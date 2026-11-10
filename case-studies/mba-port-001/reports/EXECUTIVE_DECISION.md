# Restaurante Horizonte — Informe ejecutivo de rentabilidad

**Dirección analítica:** Ricardo Vera · CIEC LAB  
**Caso:** MBA-PORT-001 · **Período:** enero–diciembre de 2025

## Diagnóstico ejecutivo

El negocio expande su facturación, pero pierde capacidad de convertir ventas en resultado operativo. El margen mensual desciende de **28,35 % a 22,17 %**, una disminución de **6,18 puntos porcentuales**. El resultado anual alcanza **8.211.449,91 UM** sobre **32.473.404,18 UM** de ventas netas (**25,29 %** de margen).

La lectura de costos identifica una presión dominante en ingredientes y aumentos relativos adicionales en merma y delivery:

| Participación sobre venta neta | Enero | Diciembre | Cambio |
|:--|--:|--:|--:|
| Costo de receta | 36,23 % | 44,29 % | +8,06 p. p. |
| Merma | 0,43 % | 0,97 % | +0,54 p. p. |
| Delivery | 2,27 % | 3,28 % | +1,01 p. p. |

**Interpretación:** la mejora de facturación no compensa automáticamente el deterioro de conversión en margen. La intervención debe concentrarse en las variables que explican la erosión y verificar el efecto de cualquier cambio comercial antes de ejecutarlo.

## Análisis de decisiones

| Alternativa | Comparación económica anual | Resolución |
|:--|--:|:--|
| H0: sostener referencia | 0,00 UM | HOLD |
| H1: precio SKU-001 +5 %, unidades −3 % | +95.150,38 UM | RESEARCH |
| H1: estrés con unidades −8 % | −10.419,55 UM | STOP SCENARIO |
| H2: descuento −15 %, volumen sin cambios | +114.563,18 UM | RESEARCH |
| H2: estrés con unidades −1 % | −82.452,97 UM | STOP SCENARIO |
| A: control de lotes y desperdicios | No cuantificado | DESIGN PILOT |
| B: rediseño de cobertura horaria | No cuantificado | DESIGN PILOT |

**Hallazgo prioritario:** el beneficio calculado de reducir descuentos se transforma en pérdida con una caída de volumen de apenas 1 %. Un cambio comercial no debe aprobarse por su resultado en un solo escenario.

## Resolución recomendada

1. **Proteger la línea base** y reforzar la medición periódica de margen, ingredientes, merma y delivery.
2. **Investigar elasticidad de demanda** antes de modificar precio o descuentos.
3. **Diseñar una prueba operativa acotada**, eligiendo una intervención entre control de merma y cobertura horaria, con responsables, indicadores y condición explícita de detención.
4. **No sumar beneficios hipotéticos** de escenarios incompatibles ni atribuir ahorro monetario a una medida sin cuantificación.
5. **Mantener trazabilidad** de aprobaciones, cancelaciones, ejecución y reversión, según controles demostrados por el proyecto.

## Entregables disponibles

- [Resultados completos y escenarios](../outputs/RESULTS.json)
- [Serie mensual](../outputs/MONTHLY_METRICS.csv)
- [Matriz de decisiones](../outputs/OPTION_MATRIX.csv)
- [Reglas y método](../docs/METHODOLOGY.md)
- [Pruebas automatizadas](../docs/TESTING.md)

**Fuente de análisis:** cuatro CSV sintéticos, 14 productos, 12 meses y conciliaciones reproducibles. Las cifras se expresan en unidades monetarias (UM) y el resultado es un indicador operativo simplificado, según la metodología disponible.

---

### ¿Tu negocio factura más, pero el margen no acompaña?

**Ricardo Vera** · Business Analysis · Operational Intelligence  
**[Solicitar diagnóstico ejecutivo](mailto:richardvera084@gmail.com?subject=Consulta%20sobre%20rentabilidad%20empresarial%20%7C%20CIEC%20LAB)**

El punto de partida es concreto: **qué decisión necesitás tomar, qué datos la sostienen y cuánto cuesta equivocarse.**
