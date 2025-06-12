"""Utilidades para archivos Excel."""

from typing import Optional, Union

import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def cargar_excel(
    nombre_archivo: Union[str, os.PathLike],
    hoja: Optional[str] = None,
    imprimir: bool = True,
    **kwargs,
) -> pd.DataFrame:
    """Cargar un archivo de Excel.

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
            df = pd.read_excel(ruta_archivo, sheet_name=hoja, **kwargs)
        else:
            df = pd.read_excel(ruta_archivo, **kwargs)

        if imprimir:
            logger.info("Archivo Excel cargado: %s", nombre_archivo_simple)
            logger.info("Forma del DataFrame: %s", df.shape)
            logger.info("Primeras filas del dataset:\n%s", df.head())
            logger.info("Tipos de datos:\n%s", df.dtypes)
        return df
    except FileNotFoundError:
        logger.error(
            "Error: No se pudo encontrar el archivo '%s'", nombre_archivo_simple
        )
    except ValueError:
        logger.error(
            "Error: No se pudo cargar el archivo '%s'. Verifique si el archivo está en formato Excel válido.",
            nombre_archivo_simple,
        )
    except Exception as e:
        logger.error("Error al cargar el archivo: %s", str(e))


# Alias para mantener compatibilidad con versiones anteriores
leer_excel = cargar_excel


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


