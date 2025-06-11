"""Utilidades para archivos Excel."""

from typing import Optional, Union

import os
import pandas as pd


def leer_excel(ruta_archivo: Union[str, os.PathLike], hoja: Optional[str] = None) -> pd.DataFrame:
    """Leer un archivo de Excel y devolver un :class:`pandas.DataFrame`.

    Parameters
    ----------
    ruta_archivo : str or PathLike
        Ruta del archivo a leer.
    hoja : str, optional
        Nombre de la hoja a cargar. Si se omite se lee la primera.

    Returns
    -------
    pandas.DataFrame
        Datos del archivo Excel.

    Examples
    --------
    >>> df = leer_excel("archivo.xlsx", hoja="Datos")
    >>> len(df)
    10
    """
    if hoja:
        df = pd.read_excel(ruta_archivo, sheet_name=hoja)
    else:
        df = pd.read_excel(ruta_archivo)
    return df


def cargar_excel(nombre_archivo: Union[str, os.PathLike], hoja: Optional[str] = None) -> pd.DataFrame:
    """Cargar un archivo de Excel e imprimir un resumen.

    Parameters
    ----------
    nombre_archivo : str or PathLike
        Ruta del archivo a cargar.
    hoja : str, optional
        Nombre de la hoja a procesar.

    Returns
    -------
    pandas.DataFrame
        DataFrame cargado.

    Examples
    --------
    >>> cargar_excel("datos.xlsx")
    Archivo Excel cargado: datos.xlsx
    """
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


def escribir_excel(df: pd.DataFrame, ruta_archivo: Union[str, os.PathLike], hoja: str = "Sheet1") -> None:
    """Guardar un :class:`pandas.DataFrame` en un archivo de Excel.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame a guardar.
    ruta_archivo : str or PathLike
        Destino del archivo a escribir.
    hoja : str, optional
        Nombre de la hoja en la que se guardará, por defecto ``"Sheet1"``.

    Examples
    --------
    >>> escribir_excel(df, "salida.xlsx")
    """
    with pd.ExcelWriter(ruta_archivo) as writer:
        df.to_excel(writer, sheet_name=hoja, index=False)


