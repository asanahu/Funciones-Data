"""Utilidades para archivos Excel."""

import os
import pandas as pd


def leer_excel(ruta_archivo, hoja=None):
    """Leer un archivo de Excel y devolver un DataFrame."""
    if hoja:
        df = pd.read_excel(ruta_archivo, sheet_name=hoja)
    else:
        df = pd.read_excel(ruta_archivo)
    return df


def cargar_excel(nombre_archivo, hoja=None):
    """Cargar un archivo de Excel e imprimir un resumen."""
    try:
        ruta_archivo = os.path.abspath(nombre_archivo)
        nombre_archivo_simple = os.path.basename(ruta_archivo)
        if hoja:
            df = pd.read_excel(ruta_archivo, sheet_name=hoja)
        else:
            df = pd.read_excel(ruta_archivo)

        print(f"Archivo Excel cargado: {nombre_archivo_simple}")
        print("\nPrimeras filas del dataset:")
        print(df.head())
        print("\nResumen estadístico del DataFrame:")
        print(df.describe())
        return df
    except FileNotFoundError:
        print(
            f"Error: No se pudo encontrar el archivo '{nombre_archivo_simple}'"
        )
    except ValueError:
        print(
            f"Error: No se pudo cargar el archivo '{nombre_archivo_simple}'. Verifique si el archivo está en formato Excel válido."
        )
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")


def escribir_excel(df, ruta_archivo, hoja="Sheet1"):
    """Guardar un DataFrame en un archivo de Excel."""
    with pd.ExcelWriter(ruta_archivo) as writer:
        df.to_excel(writer, sheet_name=hoja, index=False)


