"""Colección de funciones reutilizables para análisis de datos."""
__version__ = "0.1.0"

from .excel_utils import leer_excel, escribir_excel, cargar_excel
from .csv_utils import cargar_csv, limpiar_columnas, guardar_csv
from .json_utils import cargar_json, guardar_json
from .sql_utils import crear_conexion, leer_query, escribir_df
from .pandas_transform import (
    combinar,
    pivotar,
    limpiar_nombres,
    convertir_a_datetime,
    detectar_outliers_iqr,
    eliminar_outliers,
    eliminar_duplicados,
    imputar_nulos,
    codificar_onehot,
)
from .estadisticas import (
    nulos,
    describir_columnas,
    matriz_correlacion,
    resumen_dataset,
    resumen_columnas,
    comprueba_normalidad,
)
from .visualizaciones import (
    grafico_lineas,
    grafico_barras,
    grafico_dispersion,
    grafico_histograma,
    grafico_interactivo_lineas,
    correlacion,
    relaciones_vs_target,
    represento_doble_hist,
    hist_pos_neg_feat,
    histogramas_df,
    boxplot_variables,
)
from .file_utils import cargar_archivo
from .html_utils import cargar_html
from .model_utils import dividir_train_test, estandarizar_datos
from .modelos import (
    entrenar_regresion_logistica,
    entrenar_mlp,
    entrenar_random_forest,
    evaluar_modelo,
    evaluar_modelo_binario,
    entrenar_modelo_con_split,
)

__all__ = [
    "__version__",
    "leer_excel",
    "cargar_excel",
    "escribir_excel",
    "cargar_csv",
    "guardar_csv",
    "limpiar_columnas",
    "cargar_json",
    "guardar_json",
    "crear_conexion",
    "leer_query",
    "escribir_df",
    "convertir_a_datetime",
    "detectar_outliers_iqr",
    "eliminar_outliers",
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
    "resumen_columnas",
    "comprueba_normalidad",
    "grafico_lineas",
    "grafico_barras",
    "grafico_dispersion",
    "grafico_histograma",
    "grafico_interactivo_lineas",
    "correlacion",
    "relaciones_vs_target",
    "represento_doble_hist",
    "hist_pos_neg_feat",
    "dividir_train_test",
    "estandarizar_datos",
    "histogramas_df",
    "boxplot_variables",
    "entrenar_regresion_logistica",
    "entrenar_mlp",
    "entrenar_random_forest",
    "evaluar_modelo",
    "evaluar_modelo_binario",
    "entrenar_modelo_con_split",
]

