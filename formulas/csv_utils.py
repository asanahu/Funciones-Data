"""Funciones para trabajar con archivos CSV."""

from typing import Union

import os
import pandas as pd
import logging

from .pandas_transform import limpiar_nombres

logger = logging.getLogger(__name__)


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
            logger.info("Archivo CSV cargado: %s", nombre_archivo_simple)
            logger.info("Forma del DataFrame: %s", df.shape)
            logger.info("Primeras filas del dataset:\n%s", df.head())
            logger.info("Tipos de datos:\n%s", df.dtypes)
        return df
    except FileNotFoundError:
        logger.error("Error: No se pudo encontrar el archivo '%s'", nombre_archivo)
    except pd.errors.EmptyDataError:
        logger.error("Error: El archivo '%s' está vacío", nombre_archivo)
    except ValueError:
        logger.error(
            "Error: No se pudo cargar el archivo '%s'. Verifique si el archivo está en formato CSV válido.",
            nombre_archivo,
        )
    except Exception as e:
        logger.error("Error al cargar el archivo: %s", str(e))


def limpiar_columnas(df: pd.DataFrame, formato: str = "simple") -> pd.DataFrame:
    """Normalizar nombres de columnas.

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
    return limpiar_nombres(df, formato=formato)


