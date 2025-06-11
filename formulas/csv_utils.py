"""Funciones para trabajar con archivos CSV."""

from typing import Union

import os
import pandas as pd


def cargar_csv(nombre_archivo: Union[str, os.PathLike]) -> pd.DataFrame:
    """Cargar un archivo CSV y mostrar un resumen inicial.

    Parameters
    ----------
    nombre_archivo : str or PathLike
        Ruta del archivo CSV a leer.

    Returns
    -------
    pandas.DataFrame
        DataFrame cargado del archivo.

    Examples
    --------
    >>> df = cargar_csv("datos.csv")
    Archivo CSV cargado: datos.csv
    >>> df.head()
    """
    ruta_archivo = os.path.abspath(nombre_archivo)
    df = pd.read_csv(ruta_archivo)
    print(f"Archivo CSV cargado: {os.path.basename(ruta_archivo)}")
    print("\nPrimeras filas del dataset:")
    print(df.head())
    print("\nResumen estadístico del DataFrame:")
    print(df.describe())
    return df


def limpiar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Eliminar espacios y convertir nombres de columna a minúsculas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con las columnas a limpiar.

    Returns
    -------
    pandas.DataFrame
        DataFrame con los nombres normalizados.

    Examples
    --------
    >>> df = limpiar_columnas(df)
    >>> list(df.columns)
    ['columna1', 'columna2']
    """
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df


