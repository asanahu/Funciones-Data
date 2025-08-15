"""Funciones para trabajar con archivos o URLs de HTML."""

import logging
import os
from typing import List, Union

import pandas as pd

logger = logging.getLogger(__name__)


def cargar_html(
    fuente: Union[str, os.PathLike], imprimir: bool = True, **kwargs
) -> List[pd.DataFrame]:
    """Cargar tablas de una URL o archivo HTML.

    Parameters
    ----------
    fuente : str or PathLike
        Ruta local o URL de la página a analizar.

    Returns
    -------
    list of pandas.DataFrame
        Todas las tablas encontradas.

    Examples
    --------
    >>> tablas = cargar_html("pagina.html")
    """
    try:
        if fuente.startswith("http://") or fuente.startswith("https://"):
            if imprimir:
                logger.info("Cargando tablas desde la URL: %s", fuente)
            dfs = pd.read_html(fuente, **kwargs)
        else:
            ruta_archivo = os.path.abspath(fuente)
            nombre_archivo_simple = os.path.basename(ruta_archivo)
            if imprimir:
                logger.info(
                    "Cargando tablas desde el archivo: %s", nombre_archivo_simple
                )
            dfs = pd.read_html(ruta_archivo, **kwargs)

        if imprimir:
            logger.info("\nNúmero de tablas encontradas: %s", len(dfs))
            for i, df in enumerate(dfs):
                logger.info("\nTabla %s - forma: %s", i + 1, df.shape)
                logger.info("%s", df.head())
                logger.info("Tipos de datos:\n%s", df.dtypes)
        return dfs

    except FileNotFoundError:
        logger.error("Error: No se pudo encontrar el archivo '%s'", fuente)
    except ValueError:
        logger.error(
            "Error: No se pudo cargar la fuente '%s'. Verifique si contiene tablas HTML válidas.",
            fuente,
        )
    except Exception as e:
        logger.error("Error al cargar la fuente: %s", str(e))
