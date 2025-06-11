"""Funciones para trabajar con archivos CSV."""

import os
import pandas as pd


def cargar_csv(nombre_archivo):
    """Cargar un archivo CSV y mostrar un resumen inicial."""
    ruta_archivo = os.path.abspath(nombre_archivo)
    df = pd.read_csv(ruta_archivo)
    print(f"Archivo CSV cargado: {os.path.basename(ruta_archivo)}")
    print("\nPrimeras filas del dataset:")
    print(df.head())
    print("\nResumen estadístico del DataFrame:")
    print(df.describe())
    return df


def limpiar_columnas(df):
    """Eliminar espacios y convertir nombres de columna a minúsculas."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df


