"""Funciones para gráficos con matplotlib, seaborn y plotly."""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def grafico_lineas(df: pd.DataFrame, x: str, y: str, titulo: str = "") -> None:
    """Crear un gráfico de líneas sencillo.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame con los datos a graficar.
    x, y : str
        Columnas del eje X e Y.
    titulo : str, optional
        Título del gráfico.

    Examples
    --------
    >>> grafico_lineas(df, "fecha", "ventas")
    """
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=df, x=x, y=y)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()


def grafico_barras(df: pd.DataFrame, x: str, y: str, titulo: str = "") -> None:
    """Crear un gráfico de barras rápido.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos de entrada.
    x, y : str
        Columnas del eje X e Y.
    titulo : str, optional
        Título del gráfico.

    Examples
    --------
    >>> grafico_barras(df, "producto", "ventas")
    """
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df, x=x, y=y)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()


def grafico_dispersion(df: pd.DataFrame, x: str, y: str, titulo: str = "") -> None:
    """Crear un scatter plot sencillo.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos de entrada.
    x, y : str
        Columnas del eje X e Y.
    titulo : str, optional
        Título del gráfico.

    Examples
    --------
    >>> grafico_dispersion(df, "edad", "ingresos")
    """
    plt.figure(figsize=(8, 4))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()


def grafico_histograma(df: pd.DataFrame, columna: str, bins: int = 10, titulo: str = "") -> None:
    """Mostrar un histograma de una columna.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos de entrada.
    columna : str
        Columna sobre la que graficar el histograma.
    bins : int, optional
        Número de bins a utilizar.
    titulo : str, optional
        Título del gráfico.

    Examples
    --------
    >>> grafico_histograma(df, "ventas")
    """
    plt.figure(figsize=(8, 4))
    sns.histplot(data=df, x=columna, bins=bins)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()


def grafico_interactivo_lineas(
    df: pd.DataFrame, x: str, y: str, titulo: str = ""
) -> None:
    """Gráfico de líneas interactivo usando Plotly.

    Parameters
    ----------
    df : pandas.DataFrame
        Datos de entrada.
    x, y : str
        Columnas del eje X e Y.
    titulo : str, optional
        Título del gráfico.

    Examples
    --------
    >>> grafico_interactivo_lineas(df, "fecha", "ventas")
    """
    fig = px.line(df, x=x, y=y, title=titulo)
    fig.show()


