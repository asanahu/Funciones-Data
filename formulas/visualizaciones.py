"""Funciones para gráficos con matplotlib, seaborn y plotly."""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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


def correlacion(df: pd.DataFrame) -> None:
    """Mostrar un mapa de calor de la matriz de correlación de ``df``."""

    df_numerico = df.select_dtypes(include=["number"])
    corr_matrix = df_numerico.corr()
    plt.figure(figsize=(16, 12))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Mapa de Calor - Matriz de Correlación")
    plt.show()


def relaciones_vs_target(
    X: pd.DataFrame, Y: pd.Series, return_type: str = "axes"
) -> None:
    """Graficar relaciones de cada variable en ``X`` frente al ``target``."""

    fig_tot = len(X.columns)
    fig_por_fila = 4
    tamanio_fig = 4
    num_filas = int(np.ceil(fig_tot / fig_por_fila))
    plt.figure(figsize=(fig_por_fila * tamanio_fig + 5, num_filas * tamanio_fig + 5))
    for i, col in enumerate(X.columns):
        plt.subplot(num_filas, fig_por_fila, i + 1)
        sns.regplot(x=X[col], y=Y)
        plt.title(f"{col} vs target")
        plt.ylabel("Target")
        plt.xlabel(col)
    plt.show()


def represento_doble_hist(
    x_1: pd.Series,
    x_0: pd.Series,
    n_bins: int = 11,
    title: str = "",
    label_1: str = "Clase 1",
    label_0: str = "Clase 0",
    density: bool = False,
) -> None:
    """Representar dos histogramas en la misma figura."""

    plt.hist(x_1, n_bins, density=density, alpha=0.5, label=label_1, color="red")
    plt.hist(x_0, n_bins, density=density, alpha=0.5, label=label_0, color="green")
    plt.title(title)
    plt.legend()


def hist_pos_neg_feat(
    x: pd.DataFrame,
    y: pd.Series,
    density: bool = False,
    nbins: int = 11,
    targets: tuple[int, int] = (0, 1),
) -> None:
    """Histograma comparativo de cada feature separado por clase."""

    fig_tot = len(x.columns)
    fig_tot_fila = 4
    fig_tamanio = 4
    num_filas = int(np.ceil(fig_tot / fig_tot_fila))
    plt.figure(figsize=(fig_tot_fila * fig_tamanio + 2, num_filas * fig_tamanio + 2))
    target_neg, target_pos = targets
    for i, feat in enumerate(x.columns):
        plt.subplot(num_filas, fig_tot_fila, i + 1)
        plt.title(f"{feat}")
        idx_pos = y == target_pos
        idx_neg = y == target_neg
        represento_doble_hist(
            x[feat][idx_pos].values,
            x[feat][idx_neg].values,
            nbins,
            density=density,
            title=f"{feat}",
        )



