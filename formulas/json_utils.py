"""Herramientas para archivos JSON."""

from typing import Union

import os
import pandas as pd


def cargar_json(nombre_archivo: Union[str, os.PathLike]) -> pd.DataFrame:
    """Leer un archivo JSON y mostrar un resumen.

    Parameters
    ----------
    nombre_archivo : str or PathLike
        Ruta del archivo JSON.

    Returns
    -------
    pandas.DataFrame
        DataFrame con la información del JSON.

    Examples
    --------
    >>> df = cargar_json("datos.json")
    """
    ruta_archivo = os.path.abspath(nombre_archivo)
    df = pd.read_json(ruta_archivo)
    print(f"Archivo JSON cargado: {os.path.basename(ruta_archivo)}")
    print("\nPrimeras filas del dataset:")
    print(df.head())
    print("\nResumen estadístico del DataFrame:")
    print(df.describe())
    return df


