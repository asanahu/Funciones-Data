"""Cálculos estadísticos básicos y avanzados."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro, probplot, norm

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


def describir_columnas(df: pd.DataFrame, columnas: Iterable[str]) -> dict[str, pd.DataFrame]:
    """Mostrar y resumir información de un conjunto de columnas.

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
    resumen: dict[str, pd.DataFrame] = {}
    for col in columnas:
        if col not in df.columns:
            print(f"La columna {col} no existe en el DataFrame")
            continue
        print(f"\nColumna: {col} - Tipo de datos: {df[col].dtype}")
        print(
            f"Valores nulos: {df[col].isnull().sum()}  -  Valores distintos: {df[col].nunique()}"
        )
        print("Valores más frecuentes:")
        top = df[col].value_counts().head(10)
        for valor, cuenta in top.items():
            print(f"{valor:<20} {cuenta}")
        resumen[col] = top.reset_index().rename(columns={"index": "valor", col: "frecuencia"})
    return resumen

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


def resumen_dataset(df: pd.DataFrame, imprimir: bool = True) -> pd.DataFrame:
    """Obtener un resumen general de un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    imprimir : bool, optional
        Mostrar o no el resumen por pantalla.

    Returns
    -------
    pandas.DataFrame
        Información resumida del DataFrame.

    Examples
    --------
    >>> resumen = resumen_dataset(df)
    """
    info = {
        "Filas": len(df),
        "Columnas": df.shape[1],
        "Porcentaje Nulos": (df.isnull().sum().sum() / df.size) * 100,
    }
    tipos = df.dtypes.to_frame("Tipo")
    resumen = tipos.copy()
    resumen["Nulos"] = df.isnull().sum()
    if imprimir:
        print("Resumen general del DataFrame:")
        print(info)
        print("\nTipos y nulos por columna:")
        print(resumen)
        print("\nPrimeras filas:")
        print(df.head())
    return resumen


def resumen_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Obtener un resumen detallado de cada columna de un ``DataFrame``.

    El resultado contiene estadísticas descriptivas, tipo de dato,
    recuento de valores únicos, nulos y duplicados, así como un ejemplo de
    valor no nulo.  Para las columnas numéricas se calcula además la
    asimetría y la curtosis.

    Parameters
    ----------
    df : pandas.DataFrame
        Conjunto de datos a analizar.

    Returns
    -------
    pandas.DataFrame
        Tabla con la información resumida por columna.

    Examples
    --------
    >>> resumen = resumen_columnas(df)
    >>> resumen.head()
    """

    # Estadísticas básicas generadas por ``pandas`` y transpuestas para
    # trabajar por columna en lugar de por fila
    column_info = df.describe(include="all").T

    # Añadimos información adicional de tipo de dato y distintos conteos
    column_info["Nombre"] = column_info.index
    column_info["Tipo de Dato"] = df.dtypes
    column_info["Valores Únicos"] = df.nunique()
    column_info["Valores Nulos"] = df.isnull().sum()
    column_info["Valores duplicados"] = df.duplicated().sum()

    # Ejemplo de valor no nulo por columna (si existe)
    column_info["Ejemplo de Valor"] = df.apply(
        lambda x: x.dropna().iloc[0] if not x.dropna().empty else "-", axis=0
    )

    # Asimetría y curtosis solo aplican a columnas numéricas
    column_info["Asimetría"] = df.select_dtypes(include="number").skew()
    column_info["Curtosis"] = df.select_dtypes(include="number").kurtosis()

    # Orden de columnas para una visualización más cómoda
    columnas_deseadas = [
        "Nombre",
        "Tipo de Dato",
        "Valores Únicos",
        "Valores Nulos",
        "Valores duplicados",
        "Ejemplo de Valor",
        "mean",
        "std",
        "min",
        "25%",
        "50%",
        "75%",
        "max",
        "Asimetría",
        "Curtosis",
    ]
    # Sólo conservamos las columnas presentes en ``column_info``
    column_info = column_info.reindex(
        columns=[col for col in columnas_deseadas if col in column_info.columns]
    )

    # Redondear valores numéricos para hacer el resultado más legible
    column_info = column_info.applymap(
        lambda x: round(x, 2) if isinstance(x, (int, float)) else x
    )

    # Reiniciar el índice para obtener un DataFrame limpio
    column_info.reset_index(drop=True, inplace=True)

    return column_info


def comprueba_normalidad(df: pd.DataFrame, titulo: str = "Comprobación de normalidad") -> pd.DataFrame:
    """Evaluar la normalidad de cada columna numérica de ``df``.

    Se representan los *Q-Q plots* de todas las columnas y se calcula el
    test de Shapiro-Wilk.  El DataFrame resultante incluye el estadístico y el
    ``p-value`` de cada variable.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos a evaluar. Solo se tendrán en cuenta las columnas numéricas.
    titulo : str, optional
        Texto mostrado como título de la figura.

    Returns
    -------
    pandas.DataFrame
        Resultados del test de Shapiro-Wilk por columna.

    Examples
    --------
    >>> comprueba_normalidad(df[["edad", "ingresos"]])
    """

    # Número de gráficos y distribución en la figura
    fig_tot = len(df.columns)
    fig_por_fila = 3.0
    tamanio_fig = 4.0
    num_filas = int(np.ceil(fig_tot / fig_por_fila))

    # Creamos la figura donde se dibujarán los Q-Q plots
    plt.figure(figsize=(fig_por_fila * tamanio_fig + 5, num_filas * tamanio_fig + 2))
    resultados: dict[str, tuple[float, float]] = {}
    for i, col in enumerate(df.columns):
        ax = plt.subplot(num_filas, fig_por_fila, i + 1)
        probplot(x=df[col], dist=norm, plot=ax)
        plt.title(col)
        # Guardamos el estadístico y p-valor del test de Shapiro
        resultados[col] = shapiro(df[col])

    plt.suptitle(titulo)
    plt.show()

    resultados = (
        pd.DataFrame(resultados, index=["Test Statistic", "p-value"]).transpose()
    )
    return resultados


