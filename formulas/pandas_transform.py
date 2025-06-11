"""Transformaciones comunes con pandas."""

from typing import Iterable, Optional, Union

import pandas as pd


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


def pivotear(
    df: pd.DataFrame,
    index: Union[str, Iterable[str]],
    columns: Union[str, Iterable[str]],
    values: Union[str, Iterable[str]],
    aggfunc: str = "sum",
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
    tabla = pd.pivot_table(df, index=index, columns=columns, values=values, aggfunc=aggfunc)
    return tabla.reset_index()


def limpiar_nombres(df: pd.DataFrame) -> pd.DataFrame:
    """Convertir columnas a formato ``snake_case``.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame cuyas columnas se normalizarán.

    Returns
    -------
    pandas.DataFrame
        Copia del DataFrame con nombres normalizados.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]+", "", regex=True)
    )
    return df


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
    for col in [columnas] if isinstance(columnas, str) else columnas:
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


