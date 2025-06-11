"""Utilidades para archivos Excel."""

import pandas as pd


def leer_excel(ruta_archivo, hoja=None):
    """Leer un archivo de Excel y devolver un DataFrame."""
    if hoja:
        df = pd.read_excel(ruta_archivo, sheet_name=hoja)
    else:
        df = pd.read_excel(ruta_archivo)
    return df


def escribir_excel(df, ruta_archivo, hoja="Sheet1"):
    """Guardar un DataFrame en un archivo de Excel."""
    with pd.ExcelWriter(ruta_archivo) as writer:
        df.to_excel(writer, sheet_name=hoja, index=False)


