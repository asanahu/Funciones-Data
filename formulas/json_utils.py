"""Herramientas para archivos JSON."""

import os
import pandas as pd


def cargar_json(nombre_archivo):
    """Leer un archivo JSON y mostrar un resumen."""
    ruta_archivo = os.path.abspath(nombre_archivo)
    df = pd.read_json(ruta_archivo)
    print(f"Archivo JSON cargado: {os.path.basename(ruta_archivo)}")
    print("\nPrimeras filas del dataset:")
    print(df.head())
    print("\nResumen estadístico del DataFrame:")
    print(df.describe())
    return df


