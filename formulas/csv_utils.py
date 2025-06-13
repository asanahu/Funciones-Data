"""Funciones para trabajar con archivos CSV."""

from typing import Union
import csv
import os
import pandas as pd
import logging
import sys

try:
    import chardet
except Exception:  # pragma: no cover - library optional
    chardet = None

from .pandas_transform import limpiar_nombres

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def en_modo_interactivo() -> bool:
    return hasattr(sys, 'ps1') or sys.flags.interactive or 'ipykernel' in sys.modules

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
    modo: str = "auto",  # 'auto', 'print' o 'logger'
    **kwargs,
) -> Union[pd.DataFrame, None]:
    """Carga un CSV con detección de delimitador y codificación.

    Parameters
    ----------
    nombre_archivo : str or PathLike
        Ruta del archivo CSV a leer.
    imprimir : bool, optional
        Si ``True`` muestra información básica del DataFrame cargado.
    modo : {"auto", "print", "logger"}, optional
        Controla cómo se muestran los mensajes. En ``"auto"`` se
        imprime por pantalla solo si se está en un entorno interactivo.
        Con ``"print"`` se utiliza siempre ``print`` y con ``"logger"`` se
        envían los mensajes al ``logger``.
    **kwargs : dict, optional
        Parámetros adicionales que se pasarán a :func:`pandas.read_csv`.
    """

    # Permitir recibir "modo" dentro de kwargs y hacerlo case-insensitive
    modo = str(kwargs.pop("modo", modo)).lower()

    ruta_archivo = os.path.abspath(nombre_archivo)
    nombre_archivo_simple = os.path.basename(ruta_archivo)

    # Determinar si usamos print o logger
    if modo == "print":
        usar_print = True
    elif modo == "logger":
        usar_print = False
    elif modo == "auto":
        usar_print = en_modo_interactivo()
    else:
        logger.warning("Modo no reconocido, utilizando 'auto'.")
        usar_print = en_modo_interactivo()

    if not os.path.exists(ruta_archivo):
        logger.error(f"❌ El archivo {nombre_archivo} no existe")
        return None

    params = {
        "encoding": kwargs.pop("encoding", detectar_encoding(ruta_archivo)),
        "sep": kwargs.pop("sep", detectar_delimitador(ruta_archivo)),
        "engine": "python",
    }

    try:
        df = pd.read_csv(ruta_archivo, **params, **kwargs)

        if imprimir:
            msg = [
                f"✅ Archivo CSV cargado: {nombre_archivo_simple}",
                f"📊 Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas",
                f"📁 Columnas: {', '.join(df.columns[:5])}... ({len(df.columns)} columnas en total)",
                "\n🔍 Primeras filas:",
                str(df.head())
            ]
            for line in msg:
                print(line) if usar_print else logger.info(line)

        return df

    except Exception as e:
        logger.error(f"❌ Error al cargar el archivo '{nombre_archivo_simple}': {str(e)}")
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


