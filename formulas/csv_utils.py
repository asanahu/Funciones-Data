"""Funciones para trabajar con archivos CSV."""

from typing import Union
import csv
import os
import pandas as pd
import logging

try:
    import chardet
except Exception:  # pragma: no cover - library optional
    chardet = None

from .pandas_transform import limpiar_nombres

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def detectar_encoding(ruta_archivo: Union[str, os.PathLike]) -> str:
    """Detectar automáticamente la codificación de un archivo."""
    try:
        with open(ruta_archivo, "rb") as f:
            sample = f.read(4096)
        if chardet:
            resultado = chardet.detect(sample)
            if resultado.get("encoding"):
                return resultado["encoding"]
    except Exception as e:  # pragma: no cover - detección fallida
        logger.warning(f"Error al detectar encoding: {str(e)}")
    return "utf-8"

def detectar_delimitador(ruta_archivo: Union[str, os.PathLike]) -> str:
    """Detectar automáticamente el delimitador del archivo."""

    try:
        with open(ruta_archivo, "rb") as f:
            sample_bytes = f.read(4096)

        encoding = "utf-8"
        if chardet:
            resultado = chardet.detect(sample_bytes)
            if resultado.get("encoding"):
                encoding = resultado["encoding"]
        sample = sample_bytes.decode(encoding, errors="replace")

        # Utilizar csv.Sniffer para determinar el delimitador
        dialect = csv.Sniffer().sniff(sample)
        return dialect.delimiter
    except Exception as e:  # pragma: no cover - detección fallida
        logger.warning(f"Error al detectar delimitador: {str(e)}")
        return ","

def cargar_csv(
    nombre_archivo: Union[str, os.PathLike], 
    imprimir: bool = True,
    **kwargs
) -> pd.DataFrame:
    """
    Cargar un CSV de forma automática usando parámetros optimizados.
    """
    try:
        ruta_archivo = os.path.abspath(nombre_archivo)
        if not os.path.exists(ruta_archivo):
            logger.error(f"El archivo {nombre_archivo} no existe")
            return None

        params = {
            "encoding": None,
            "sep": None,
            "engine": "python",
        }
        params.update(kwargs)

        if params["encoding"] is None:
            params["encoding"] = detectar_encoding(ruta_archivo)
        if params["sep"] is None:
            params["sep"] = detectar_delimitador(ruta_archivo)

        df = pd.read_csv(ruta_archivo, **params)
        
        if imprimir:
            logger.info(f"Archivo CSV cargado exitosamente")
            logger.info(f"Dimensiones: {df.shape}")
            logger.info(f"Columnas: {list(df.columns)}")
            logger.info("\nPrimeras filas:")
            logger.info(f"\n{df.head()}")
        
        return df
        
    except Exception as e:
        logger.error(f"Error al cargar el archivo: {str(e)}")
        return None



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


def guardar_csv(df: pd.DataFrame, ruta_archivo: Union[str, os.PathLike], **kwargs) -> None:
    """Guardar un :class:`pandas.DataFrame` en un archivo CSV.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame a guardar.
    ruta_archivo : str or PathLike
        Ubicación donde se escribirá el CSV.
    **kwargs : dict, optional
        Parámetros adicionales para :func:`pandas.DataFrame.to_csv`.

    Examples
    --------
    >>> guardar_csv(df, "salida.csv")
    """
    ruta = os.path.abspath(ruta_archivo)
    df.to_csv(ruta, index=False, **kwargs)


