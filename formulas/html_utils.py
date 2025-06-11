"""Funciones para manejar tablas HTML."""

import os
import pandas as pd


def cargar_html(fuente):
    """Cargar tablas desde una URL o archivo HTML.

    Devuelve una lista de DataFrames con las tablas encontradas.
    Imprime un resumen de las tablas cargadas.
    """
    if fuente.startswith("http://") or fuente.startswith("https://"):
        print(f"Cargando tablas desde la URL: {fuente}")
        dfs = pd.read_html(fuente)
    else:
        ruta_archivo = os.path.abspath(fuente)
        print(f"Cargando tablas desde el archivo: {os.path.basename(ruta_archivo)}")
        dfs = pd.read_html(ruta_archivo)

    print(f"\nNúmero de tablas encontradas: {len(dfs)}")
    for i, df in enumerate(dfs):
        print(f"\nTabla {i + 1}:")
        print(df.head())
    return dfs

