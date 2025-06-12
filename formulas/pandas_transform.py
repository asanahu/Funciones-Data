"""Transformaciones comunes con pandas."""

from typing import Iterable, Optional, Union, Callable

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def combinar(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    on: Union[str, Iterable[str]],
    how: str = "inner",
) -> pd.DataFrame:
    """Realizar merge entre dos DataFrames.

    Parameters
    ----------
    df1, df2 : pandas.DataFrame
        DataFrames a combinar.
    on : str or iterable of str
        Columnas por las que se realizará el merge.
    how : str, optional
        Tipo de combinación (``"inner"``, ``"left"``...).

    Returns
    -------
    pandas.DataFrame
        Resultado del merge.

    Examples
    --------
    >>> combinado = combinar(df1, df2, on="id")
    """
    return pd.merge(df1, df2, on=on, how=how)


def pivotar(
    df: pd.DataFrame,
    index: Union[str, Iterable[str]],
    columns: Union[str, Iterable[str]],
    values: Union[str, Iterable[str]],
    aggfunc: Union[str, Callable, Iterable[Union[str, Callable]]] = "sum",
) -> pd.DataFrame:
    """Crear tabla dinámica.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos de entrada.
    index, columns, values : str or iterable of str
        Parámetros para :func:`pandas.pivot_table`.
    aggfunc : str, optional
        Función de agregación a utilizar.

    Returns
    -------
    pandas.DataFrame
        Tabla dinámica resultante.
    """
    tabla = pd.pivot_table(
        df,
        index=index,
        columns=columns,
        values=values,
        aggfunc=aggfunc,
    )
    return tabla.reset_index()


def limpiar_nombres(df: pd.DataFrame, formato: str = "snake_case") -> pd.DataFrame:
    """Normalizar los nombres de columna.

    Con ``formato="simple"`` se eliminan espacios iniciales/finales y se
    convierten los nombres a minúsculas.  Con ``formato="snake_case"`` además se
    reemplazan los espacios por ``_`` y se eliminan caracteres no alfanuméricos.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame cuyas columnas se normalizarán.
    formato : {"simple", "snake_case"}, optional
        Estilo deseado para los nombres. Por defecto ``"snake_case"``.

    Returns
    -------
    pandas.DataFrame
        Copia del DataFrame con los nombres normalizados.
    """
    df = df.copy()
    if formato not in {"simple", "snake_case"}:
        raise ValueError("formato debe ser 'simple' o 'snake_case'")
    df.columns = df.columns.str.strip().str.lower()
    if formato == "snake_case":
        df.columns = (
            df.columns
            .str.replace(" ", "_")
            .str.replace(r"[^a-z0-9_]+", "", regex=True)
        )
    return df


def limpiar_columnas(df: pd.DataFrame, formato: str = "simple") -> pd.DataFrame:
    """Compatibilidad para ``limpiar_columnas`` existente.

    Esta función delega en :func:`limpiar_nombres` para mantener retro
    compatibilidad con el nombre anterior.
    """
    return limpiar_nombres(df, formato=formato)


def convertir_a_datetime(df: pd.DataFrame, columnas: Union[str, Iterable[str]], formato: Optional[str] = None) -> pd.DataFrame:
    """Convertir columnas a tipo ``datetime``.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    columnas : str or iterable of str
        Columnas a convertir.
    formato : str, optional
        Formato de fecha a utilizar.

    Returns
    -------
    pandas.DataFrame
        DataFrame con las columnas convertidas.
    """
    df = df.copy()
    cols = [columnas] if isinstance(columnas, str) else columnas
    for col in cols:
        if col not in df.columns:
            raise KeyError(f"La columna '{col}' no existe en el DataFrame")
        df[col] = pd.to_datetime(df[col], format=formato, errors="coerce")
    return df


def detectar_outliers_iqr(df: pd.DataFrame, columna: str, factor: float = 1.5) -> pd.Series:
    """Detectar outliers en una columna utilizando el método IQR.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    columna : str
        Columna sobre la que aplicar el método.
    factor : float, optional
        Multiplicador del rango intercuartílico, por defecto ``1.5``.

    Returns
    -------
    pandas.Series
        Serie booleana que indica si cada fila es un outlier.
    """
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - factor * iqr
    upper = q3 + factor * iqr
    return (df[columna] < lower) | (df[columna] > upper)


def eliminar_duplicados(
    df: pd.DataFrame, subset: Optional[Union[str, Iterable[str]]] = None,
    keep: str = "first", mensaje: bool = True
) -> pd.DataFrame:
    """Eliminar filas duplicadas del DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    subset : str or iterable of str, optional
        Columnas a considerar para detectar duplicados.
    keep : {"first", "last", False}, optional
        Cómo manejar las filas duplicadas.
    mensaje : bool, optional
        Mostrar por pantalla cuántas filas se eliminaron.

    Returns
    -------
    pandas.DataFrame
        DataFrame sin duplicados.

    Examples
    --------
    >>> df = eliminar_duplicados(df)
    """
    df = df.copy()
    antes = len(df)
    df = df.drop_duplicates(subset=subset, keep=keep)
    despues = len(df)
    if mensaje:
        logger.info("Filas eliminadas: %s", antes - despues)
    return df


def imputar_nulos(
    df: pd.DataFrame,
    estrategia: str = "media",
    columnas: Optional[Union[str, Iterable[str]]] = None,
    valor: Optional[float] = None,
) -> pd.DataFrame:
    """Imputar valores nulos de forma sencilla.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    estrategia : {"media", "mediana", "moda", "constante"}, optional
        Estrategia de imputación.
    columnas : str or iterable of str, optional
        Columnas a procesar. Por defecto solo numéricas.
    valor : float, optional
        Valor a utilizar si ``estrategia`` es ``"constante"``.

    Returns
    -------
    pandas.DataFrame
        DataFrame con valores imputados.
    """
    df = df.copy()
    if columnas is None:
        columnas = df.select_dtypes(include="number").columns
    if isinstance(columnas, str):
        columnas = [columnas]
    for col in columnas:
        if estrategia == "media":
            valor_imputado = df[col].mean()
        elif estrategia == "mediana":
            valor_imputado = df[col].median()
        elif estrategia == "moda":
            valor_imputado = df[col].mode().iloc[0]
        elif estrategia == "constante":
            valor_imputado = valor
        else:
            raise ValueError("Estrategia no soportada")
        df[col] = df[col].fillna(valor_imputado)
    return df


def codificar_onehot(df: pd.DataFrame, columnas: Iterable[str]) -> pd.DataFrame:
    """Aplicar one-hot encoding a columnas categóricas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    columnas : iterable of str
        Columnas categóricas a codificar.

    Returns
    -------
    pandas.DataFrame
        DataFrame con las columnas codificadas.

    Examples
    --------
    >>> df = codificar_onehot(df, ["genero", "pais"])
    """
    return pd.get_dummies(df, columns=list(columnas), drop_first=False)


