"""Funciones para trabajar con archivos CSV."""

from typing import Union
import csv
import os
import pandas as pd
import logging

from .pandas_transform import limpiar_nombres

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def detectar_delimitador(ruta_archivo: Union[str, os.PathLike]) -> str:
    """
    Detectar automáticamente el delimitador del archivo.
    """
    separadores_comunes = [',', ';', '\t', '|']
    
    try:
        with open(ruta_archivo, 'r', encoding='latin-1') as f:
            sample = f.read(2048)
            for sep in separadores_comunes:
                if sep in sample:
                    return sep
            return ','  # default delimiter if none found
    except Exception as e:
        logger.warning(f"Error al detectar delimitador: {str(e)}")
        return None

def cargar_csv(
    nombre_archivo: Union[str, os.PathLike], 
    imprimir: bool = True,
    **kwargs
) -> pd.DataFrame:
    """
    Cargar un CSV de forma automática usando parámetros optimizados.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(nombre_archivo):
            logger.error(f"El archivo {nombre_archivo} no existe")
            return None

        # Parámetros por defecto que sabemos que funcionan
        default_params = {
            'encoding': 'latin-1',
            'sep': None,
            'engine': 'python'
        }
        
        # Actualizar con kwargs si se proporcionan
        default_params.update(kwargs)
        
        # Intentar cargar el archivo
        df = pd.read_csv(nombre_archivo, **default_params)
        
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


