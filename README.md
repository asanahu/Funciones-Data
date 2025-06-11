# Repositorio de fórmulas para ETL y análisis de datos

Este proyecto agrupa funciones reutilizables para manipulación y exploración de 
datos con **pandas**. Las utilidades están organizadas en el paquete `formulas` y
se acompañan de algunos notebooks de ejemplo.

## Estructura principal

```
formulas/
    excel_utils.py      # Leer y escribir Excel
    csv_utils.py        # Limpieza y carga de CSV
    json_utils.py       # Manejo de JSON
    html_utils.py       # Leer tablas HTML
    sql_utils.py        # Conexión a bases de datos
    pandas_transform.py # Transformaciones comunes con pandas
    estadisticas.py     # Resúmenes y cálculos estadísticos
    visualizaciones.py  # Gráficos rápidos
```

Los notebooks de la carpeta `ejemplos` muestran cómo utilizar estas funciones
para tareas habituales.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso rápido

Importa las funciones que necesites desde `formulas`:

```python
from formulas import cargar_csv, cargar_html, nulos, grafico_lineas

df = cargar_csv("datos.csv")
resumen = nulos(df)
grafico_lineas(df, "fecha", "ventas", titulo="Ventas diarias")
# También puedes cargar tablas HTML
# tablas = cargar_html("pagina.html")
```

Consulta cada módulo para obtener más detalles y ejemplos de uso.

