"""Colección de funciones reutilizables para análisis de datos."""
__version__ = "0.1.0"

from .excel_utils import leer_excel, escribir_excel, cargar_excel
from .csv_utils import cargar_csv, limpiar_columnas
from .json_utils import cargar_json
from .sql_utils import crear_conexion, leer_query, escribir_df
from .pandas_transform import (
    combinar,
    pivotar,
    limpiar_nombres,
    convertir_a_datetime,
    detectar_outliers_iqr,
    eliminar_duplicados,
    imputar_nulos,
    codificar_onehot,
)
from .estadisticas import (
    nulos,
    describir_columnas,
    matriz_correlacion,
    resumen_dataset,
)
from .visualizaciones import (
    grafico_lineas,
    grafico_barras,
    grafico_dispersion,
    grafico_histograma,
    grafico_interactivo_lineas,
)
from .file_utils import cargar_archivo
from .html_utils import cargar_html

__all__ = [
    "__version__",
    "leer_excel",
    "cargar_excel",
    "escribir_excel",
    "cargar_csv",
    "limpiar_columnas",
    "cargar_json",
    "crear_conexion",
    "leer_query",
    "escribir_df",
    "convertir_a_datetime",
    "detectar_outliers_iqr",
    "eliminar_duplicados",
    "imputar_nulos",
    "codificar_onehot",
    "combinar",
    "pivotar",
    "limpiar_nombres",
    "cargar_archivo",
    "cargar_html",
    "nulos",
    "describir_columnas",
    "matriz_correlacion",
    "resumen_dataset",
    "grafico_lineas",
    "grafico_barras",
    "grafico_dispersion",
    "grafico_histograma",
    "grafico_interactivo_lineas",
]

