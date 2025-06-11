"""Funciones genéricas para detección de archivos."""

import os
from .csv_utils import cargar_csv
from .json_utils import cargar_json
from .excel_utils import leer_excel


def cargar_archivo(nombre_archivo):
    """Cargar un archivo según su extensión."""
    extension = os.path.splitext(nombre_archivo)[1].lower()
    if extension == ".csv":
        return cargar_csv(nombre_archivo)
    if extension == ".json":
        return cargar_json(nombre_archivo)
    if extension in [".xls", ".xlsx"]:
        return leer_excel(nombre_archivo)
    raise ValueError(f"Formato de archivo no soportado: {extension}")

