"""Cálculos estadísticos básicos y avanzados."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from typing import Iterable, Optional


def nulos(df: pd.DataFrame, ordenar_por: str = "Nulos", imprimir: bool = True) -> pd.DataFrame:
    """Resumen de valores nulos, porcentaje y valores únicos.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    ordenar_por : str, optional
        Columna por la que ordenar el resultado.
    imprimir : bool, optional
        Si se debe imprimir el resumen por pantalla.

    Returns
    -------
    pandas.DataFrame
        Resumen de nulos y duplicados.

    Examples
    --------
    >>> resumen = nulos(df)
    """
    nulos_por_columna = df.isnull().sum()
    porcentaje = (nulos_por_columna / len(df)) * 100
    valores_unicos = df.nunique()
    filas_dup = df.duplicated().sum()
    resumen = pd.DataFrame({
        "Nulos": nulos_por_columna,
        "Porcentaje Nulos": porcentaje.round(2),
        "Valores únicos": valores_unicos,
    })
    resumen.loc["Duplicados"] = [filas_dup, (filas_dup / len(df)) * 100, "N/A"]
    if ordenar_por in resumen.columns:
        resumen = resumen.sort_values(by=ordenar_por, ascending=False)
    if imprimir:
        print("Número de nulos, porcentaje de nulos y valores únicos:")
        print(resumen)
    return resumen


def describir_columnas(df: pd.DataFrame, columnas: Iterable[str]) -> None:
    """Mostrar información resumida de un conjunto de columnas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los datos.
    columnas : iterable of str
        Columnas a describir.

    Examples
    --------
    >>> describir_columnas(df, ["col1", "col2"])
    """
    for col in columnas:
        if col not in df.columns:
            print(f"La columna {col} no existe en el DataFrame")
            continue
        print(f"\nColumna: {col} - Tipo de datos: {df[col].dtype}")
        print(f"Valores nulos: {df[col].isnull().sum()}  -  Valores distintos: {df[col].nunique()}")
        print("Valores más frecuentes:")
        top = df[col].value_counts().head(10)
        for valor, cuenta in top.items():
            print(f"{valor:<20} {cuenta}")


def matriz_correlacion(df: pd.DataFrame, imprimir: bool = False) -> Optional[pd.DataFrame]:
    """Calcular y mostrar la matriz de correlación para columnas numéricas.

    Parameters
    ----------
    df : pandas.DataFrame
        Conjunto de datos de entrada.
    imprimir : bool, optional
        Mostrar o no la matriz en consola.

    Returns
    -------
    pandas.DataFrame or None
        Matriz de correlación calculada.
    """
    df_num = df.select_dtypes(include=["number"])
    if df_num.shape[1] < 2:
        print("El DataFrame no tiene suficientes columnas numéricas para calcular la correlación.")
        return None
    corr = df_num.corr()
    if imprimir:
        print("Matriz de correlación:")
        print(corr)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Mapa de Calor - Matriz de Correlación")
    plt.show()
    return corr


