"""Funciones útiles para tareas de ETL (compatibilidad).

Este módulo mantiene la interfaz antigua delegando en las funciones del paquete
`formulas`. Puedes importar directamente desde `formulas` para obtener todas las
nuevas funcionalidades.
"""

import os
from typing import Union
from formulas import (
    cargar_csv,
    cargar_json,
    cargar_excel,
    nulos,
    describir_columnas,
    matriz_correlacion,
)


def cargar_archivo(nombre_archivo: Union[str, os.PathLike]):
    """Cargar un archivo según su extensión."""
    extension = os.path.splitext(nombre_archivo)[1].lower()
    if extension == ".csv":
        return cargar_csv(nombre_archivo)
    if extension == ".json":
        return cargar_json(nombre_archivo)
    if extension in [".xls", ".xlsx"]:
        return cargar_excel(nombre_archivo)
    raise ValueError(f"Formato de archivo no soportado: {extension}")
