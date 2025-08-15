"""Utilidades para preparación de datos previo a modelado."""

from __future__ import annotations

from typing import Iterable, Optional, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def dividir_train_test(
    df: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    random_state: Optional[int] = None,
    estratificar: bool = True,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Dividir el ``DataFrame`` en conjuntos de entrenamiento y prueba.

    Parameters
    ----------
    df : pandas.DataFrame
        Conjunto de datos completo.
    target : str
        Columna objetivo.
    test_size : float, optional
        Proporción del conjunto de prueba, por defecto ``0.2``.
    random_state : int or None, optional
        Semilla para la aleatoriedad.
    estratificar : bool, optional
        Si se debe estratificar según la variable objetivo.

    Returns
    -------
    tuple of pandas.DataFrame and pandas.Series
        ``X_train``, ``X_test``, ``y_train`` y ``y_test``.

    Examples
    --------
    >>> X_train, X_test, y_train, y_test = dividir_train_test(df, "target")
    """
    X = df.drop(columns=[target])
    y = df[target]
    strat = y if estratificar else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=strat
    )
    return X_train, X_test, y_train, y_test


def estandarizar_datos(
    df: pd.DataFrame,
    columnas: Optional[Iterable[str]] = None,
) -> Tuple[pd.DataFrame, StandardScaler]:
    """Aplicar ``StandardScaler`` a columnas numéricas.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos de entrada.
    columnas : iterable of str, optional
        Columnas a escalar. Por defecto numéricas.

    Returns
    -------
    tuple[pandas.DataFrame, StandardScaler]
        DataFrame con las columnas escaladas y el ``StandardScaler`` ajustado.

    Examples
    --------
    >>> df_std, scaler = estandarizar_datos(df, ["edad", "ingresos"])
    """
    df = df.copy()
    if columnas is None:
        columnas = df.select_dtypes(include="number").columns
    scaler = StandardScaler()
    df[list(columnas)] = scaler.fit_transform(df[list(columnas)])
    return df, scaler
