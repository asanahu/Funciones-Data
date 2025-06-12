"""Herramientas para archivos JSON."""

from typing import Union

import os
import json
import pandas as pd
import logging

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


