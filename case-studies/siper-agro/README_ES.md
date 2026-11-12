# SIPER-AGRO | Inteligencia operativa para acopios y agroempresas

### De los registros dispersos a decisiones gerenciales verificables

**CIEC LAB · Ricardo Vera · Análisis empresarial e inteligencia operativa**

Una empresa puede tener compras registradas, ventas documentadas, stock informado, liquidaciones y costos de transporte, y aun así no saber **qué diferencias comprometen la confiabilidad de su cierre operativo**.

SIPER-AGRO organiza esas fuentes, reconcilia registros vinculados y transforma las inconsistencias en una agenda de verificación para la gerencia.

**Este caso de portafolio utiliza datos sintéticos para demostrar el método; no corresponde a una consultoría realizada a un cliente.**

## Resultados del caso

| Frente | Resultado | Qué conviene verificar |
|---|---:|---|
| Inventario | **−2 toneladas** | Movimientos, remitos, recuento físico y fecha de corte |
| Liquidaciones y cobros | **−500 ARS** | Imputación de pagos, comprobantes y fechas |
| Logística | **+200 ARS** | Fletes, facturas y registro independiente de costos |
| Precios de compra y venta | **−10 y +5 ARS/TN** | Producto, condiciones del contrato y base comparable |

**Balance del análisis:** cuatro familias conciliadas, siete comparaciones documentales, cinco diferencias para revisar y dos comparaciones coincidentes.

El punto no es mostrar alertas por mostrar. El valor está en **saber dónde investigar primero**, qué información solicitar y qué condición debe cumplirse antes de cerrar una observación.

## Cómo se convierte en un servicio

**Diagnóstico inicial.** Se define un período, el alcance de la operación y las fuentes disponibles.

**Conciliación documentada.** Se cruzan compras, ventas, stock, liquidaciones, registros financieros y costos logísticos, conservando el vínculo con la evidencia.

**Lectura gerencial.** Las diferencias se traducen en preguntas concretas, prioridades de revisión y responsables sugeridos.

**Devolución y seguimiento.** Se acuerdan los comprobantes faltantes, los controles siguientes y el criterio para considerar resuelto cada hallazgo.

Este enfoque complementa el trabajo administrativo y contable: permite a la gerencia concentrarse en decisiones respaldadas por información verificable.

## Evidencia técnica

El caso público permite reproducir las siete comparaciones mediante Python, con **nueve pruebas automatizadas** y ejecución en GitHub Actions para Python 3.10, 3.12 y 3.13. La aplicación SIPER-AGRO completa permanece privada.

[**Código de reproducción**](src/reproduce.py) · [**Datos del ejercicio**](data/synthetic_transactions.csv) · [**Pruebas**](tests/test_reproduce.py) · [**Lectura gerencial**](docs/DECISION_BRIEF_ES.md) · [**Alcance técnico**](docs/EVIDENCE_AND_LIMITATIONS.md)

## Qué puedo aportar a una empresa

- Reconstruir diferencias entre registros y determinar qué evidencia falta.
- Convertir inconsistencias operativas en un plan de verificación priorizado.
- Traducir análisis técnico a lenguaje gerencial.
- Diseñar controles y criterios de seguimiento para evitar cierres a ciegas.

**Ricardo Vera · CIEC LAB · Argentina**

[**Consultar por un diagnóstico de operaciones**](mailto:richardvera084@gmail.com?subject=SIPER-AGRO%20%7C%20Consulta%20empresarial) · [**Contactar por oportunidades profesionales**](mailto:richardvera084@gmail.com?subject=Ricardo%20Vera%20%7C%20Oportunidad%20profesional)

[English case study](README.md) · [Portafolio ejecutivo](../../EXECUTIVE_PORTFOLIO.md)
