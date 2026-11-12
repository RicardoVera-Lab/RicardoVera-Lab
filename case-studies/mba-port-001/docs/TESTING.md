# Pruebas y regeneración

Desde la raíz del repositorio, ingresá primero en el directorio del caso:

```bash
cd case-studies/mba-port-001
python -m src.restaurant_case --check-anchors
python -m src.operational_controls
python -m unittest discover -s tests -v
python tools/verify_manifest.py
```

Python 3.10+; no se instala paquete alguno. Los resultados financieros se pueden regenerar en `outputs/` o con `--output-dir /ruta/alternativa`. El CLI devuelve código 2 con `STOP: ...` cuando una fuente es incoherente o falla una conciliación. Para inspección sin escritura: `python -m src.restaurant_case --no-write --check-anchors`.

## Casos positivos

Conciliaciones de 168 filas de ventas, 12 meses en cada fuente mensual; ventas netas y resultado anual con precisión de centavo; margen de enero y diciembre; H1 3% / H2 0%; estados decisorios; liberación por cancelación preejecución; liberación tras reversión referenciada.

## Casos adversos

Unidades fraccionarias o alteradas, consumo de inventario inconsistente, apertura de inventario que no coincide con el mes previo, archivo ausente, supuesto de volumen inválido; caída de unidades H1 8% y H2 1% vuelve negativo el resultado relativo; cancelación posterior a ejecución retiene slot; reversión con referencia incorrecta; IDs vacíos o no canónicos y reserva duplicada son rechazados.

El archivo `MANIFEST_SHA256.txt` fija los bytes de todos los archivos de publicación excepto el propio manifiesto. Las cuatro fuentes además conservan los hashes de congelamiento comprobados por las pruebas. El flujo activo está en la raíz del repositorio, en `.github/workflows/mba01-validation.yml`, y vuelve a comprobar las cuentas en Python 3.10, 3.12 y 3.13.
