"""Herramientas para archivos JSON."""

import json
import logging
import os
from typing import Union

import pandas as pd

logger = logging.getLogger(__name__)


def cargar_json(
    nombre_archivo: Union[str, os.PathLike], imprimir: bool = True, **kwargs
) -> pd.DataFrame:
    """Leer un archivo JSON.

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
    try:
        ruta_archivo = os.path.abspath(nombre_archivo)
        nombre_archivo_simple = os.path.basename(ruta_archivo)
        df = pd.read_json(ruta_archivo, **kwargs)
        if imprimir:
            logger.info("Archivo JSON cargado: %s", nombre_archivo_simple)
            logger.info("Forma del DataFrame: %s", df.shape)
            logger.info("Primeras filas del dataset:\n%s", df.head())
            logger.info("Tipos de datos:\n%s", df.dtypes)
        return df
    except FileNotFoundError:
        logger.error("Error: No se pudo encontrar el archivo '%s'", nombre_archivo)
    except ValueError:
        logger.error(
            "Error: No se pudo cargar el archivo '%s'. Verifique si el archivo está en formato JSON válido o no está vacío.",
            nombre_archivo,
        )
    except json.JSONDecodeError:
        logger.error(
            "Error: No se pudo analizar el archivo '%s'. Verifique que el contenido tenga un formato JSON válido.",
            nombre_archivo,
        )
    except Exception as e:
        logger.error("Error al cargar el archivo: %s", str(e))


def guardar_json(
    df: pd.DataFrame,
    ruta_archivo: Union[str, os.PathLike],
    orient: str = "records",
    lines: bool = False,
    **kwargs,
) -> None:
    """Guardar un :class:`pandas.DataFrame` en formato JSON.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos que se escribirán en el archivo.
    ruta_archivo : str or PathLike
        Destino del archivo JSON.
    orient : str, optional
        Orientación del JSON a generar, por defecto ``"records"``.
    lines : bool, optional
        Si se debe escribir cada registro en una línea.
    **kwargs : dict, optional
        Parámetros adicionales para :func:`pandas.DataFrame.to_json`.

    Examples
    --------
    >>> guardar_json(df, "salida.json")
    """
    ruta = os.path.abspath(ruta_archivo)
    df.to_json(ruta, orient=orient, lines=lines, force_ascii=False, **kwargs)
