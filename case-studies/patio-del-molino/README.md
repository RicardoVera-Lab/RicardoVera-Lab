# Facturó 4,44 millones. Su margen apenas alcanzaba el 3,42 %.

### SIPER-X | Inteligencia operativa y diagnóstico de rentabilidad gastronómica

**Dirección del análisis: Ricardo Vera · CIEC LAB**

## Un restaurante puede estar lleno y tener muy poco margen para equivocarse.

Cuando los costos, el stock, los reembolsos y la operación empiezan a enviar señales al mismo tiempo, el verdadero desafío no es acumular alertas.

**Es identificar qué problema puede consumir primero la rentabilidad y qué decisión debería tomar el propietario.**

En el caso Patio del Molino, SIPER-X organiza señales operativas y el análisis ejecutivo las convierte en preguntas, prioridades y controles concretos.

[**Consultar un diagnóstico**](mailto:richardvera084@gmail.com?subject=Diagn%C3%B3stico%20SIPER-X%20%7C%20Ricardo%20Vera) · [**Abrir informe gerencial**](reports/EXECUTIVE_BRIEF.md)

---

## La radiografía financiera

| Variable reconstruida | Resultado |
|---|---:|
| Ventas declaradas | **4.444.400 UM** |
| Compras e insumos declarados | **1.911.092 UM** |
| Diferencia ventas menos compras | **2.533.308 UM** |
| Gastos operativos declarados | **2.381.310 UM** |
| **Resultado operativo simplificado** | **151.998 UM** |
| **Margen operativo simplificado** | **3,42 %** |

**Por cada 100 UM de venta, el ejercicio deja apenas 3,42 UM después de las compras y gastos incluidos.**

Esta medida es una aproximación gerencial construida a partir de las cifras declaradas; no reemplaza el costo de consumo por receta.

### ¿Qué pasa si las compras suben un 8 %?

| Escenario | Resultado simplificado |
|---|---:|
| Referencia | **+151.998 UM** |
| Compras +8 %, otras variables iguales | **−889,36 UM** |

Una variación aparentemente moderada **borra por completo el resultado modelado**. Esa es la señal que justifica ordenar la discusión directiva.

## Las señales que deben investigarse

El diagnóstico SIPER-X reúne indicadores de merma, inventario, carta, caja, reembolsos y gastos. Entre los valores informados aparecen:

- **14,7 %** de merma en un indicador operativo.
- **6,4 %** de diferencia inventario/sistema.
- **43 %** en el indicador reportado de food cost de carta.
- **+70 %** en importe de reembolsos: de 40.000 a 68.000 UM.
- **9,3 %** en la diferencia caja/ticket.
- **+19 %** en la variación de gasto operativo.

Los indicadores describen **áreas de revisión**. El 43 % reportado no surge de dividir compras declaradas por ventas; requiere el contraste de recetas, consumos e inventarios. El +70 % corresponde a importes, no a la cantidad de reembolsos.

## De los datos a cinco decisiones gerenciales

| Frente | Decisión inmediata |
|---|---|
| **Rentabilidad por plato** | Conciliar recetas, compras, consumo y contribución real |
| **Caja y reembolsos** | Vincular tickets, anulaciones y comprobantes |
| **Inventario y desperdicio** | Diseñar conteos y controles de merma |
| **Carta y bebidas** | Analizar mix y contribución antes de cambiar precios |
| **Clientes** | Validar identificadores y períodos antes de inferir fidelidad |

**Resultado:** una agenda de intervención ordenada. Las hipótesis de riesgo no se convierten automáticamente en pérdidas ni en autorizaciones para modificar la operación.

## Mi metodología de intervención

**Semana 1 — Evidencia.** Reunir fuentes, responsables, registros y criterios de medición.

**Semana 2 — Conciliación.** Separar costos, stock, caja y variables todavía no verificadas.

**Semana 3 — Diseño de piloto.** Definir alternativa, responsable, indicador y condición de detención.

**Semana 4 — Decisión.** Comparar resultados y emitir un dictamen gerencial.

[**Leer el informe ejecutivo**](reports/EXECUTIVE_BRIEF.md) · [**Ver el método**](docs/METHODOLOGY.md)

## Evidencia que podés revisar

[Registros financieros](data/financial_snapshot.csv) · [Indicadores](data/kri_snapshot.csv) · [Reproducción Python](src/reproduce.py) · [Pruebas](tests/test_case.py)

Desde la raíz del repositorio, con Python 3.10+:

```bash
python case-studies/patio-del-molino/src/reproduce.py
python -m unittest discover -s case-studies/patio-del-molino/tests -v
```

**Ficha del caso:** diagnóstico empresarial de prueba con cifras en unidades monetarias. Las cuentas financieras centrales y el escenario de sensibilidad son reproducibles; los indicadores complementarios provienen del diagnóstico SIPER-X.

---

## ¿Conocés tu facturación, pero no qué está consumiendo tu margen?

**No esperes a que una caída de caja convierta en urgente lo que hoy ya puede medirse.**

**Ricardo Vera · CIEC LAB** · Inteligencia operativa · Análisis de negocios · Diagnóstico de rentabilidad

[**Solicitar un diagnóstico empresarial SIPER-X**](mailto:richardvera084@gmail.com?subject=Quiero%20un%20diagn%C3%B3stico%20SIPER-X) · [English summary](README_EN.md) · [Portafolio](../../EXECUTIVE_PORTFOLIO.md)
