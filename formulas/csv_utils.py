"""Funciones para trabajar con archivos CSV."""

from typing import Union

import os
import pandas as pd


def cargar_csv(
    nombre_archivo: Union[str, os.PathLike], imprimir: bool = True, **kwargs
) -> pd.DataFrame:
    """Cargar un archivo CSV.

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
    try:
        ruta_archivo = os.path.abspath(nombre_archivo)
        nombre_archivo_simple = os.path.basename(ruta_archivo)
        df = pd.read_csv(ruta_archivo, **kwargs)
        if imprimir:
            print(f"Archivo CSV cargado: {nombre_archivo_simple}")
            print(f"Forma del DataFrame: {df.shape}")
            print("\nPrimeras filas del dataset:")
            print(df.head())
            print("\nTipos de datos:")
            print(df.dtypes)
        return df
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo '{nombre_archivo}' está vacío")
    except ValueError:
        print(
            f"Error: No se pudo cargar el archivo '{nombre_archivo}'. Verifique si el archivo está en formato CSV válido."
        )
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")


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


