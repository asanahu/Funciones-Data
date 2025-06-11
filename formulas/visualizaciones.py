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
    """Mostrar un mapa de calor de la matriz de correlación de ``df``.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame del que se calculará la correlación (solo columnas numéricas).

    Examples
    --------
    >>> correlacion(df)
    """

    # Seleccionamos únicamente variables numéricas
    df_numerico = df.select_dtypes(include=["number"])
    # Calculamos la matriz de correlación
    corr_matrix = df_numerico.corr()
    # Dibujamos el heatmap con ``seaborn``
    plt.figure(figsize=(16, 12))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Mapa de Calor - Matriz de Correlación")
    plt.show()


def relaciones_vs_target(x: pd.DataFrame, y: pd.Series) -> None:
    """Graficar la relación de cada variable de ``x`` frente a ``y``.

    Parameters
    ----------
    x : pandas.DataFrame
        Conjunto de variables independientes.
    y : pandas.Series
        Variable objetivo contra la que comparar.

    Examples
    --------
    >>> relaciones_vs_target(features, target)
    """

    # Preparamos la rejilla de gráficos
    fig_tot = len(x.columns)
    fig_por_fila = 4
    tamanio_fig = 4
    num_filas = int(np.ceil(fig_tot / fig_por_fila))
    plt.figure(figsize=(fig_por_fila * tamanio_fig + 5, num_filas * tamanio_fig + 5))
    for i, col in enumerate(x.columns):
        # Dibujamos cada relación de forma individual
        plt.subplot(num_filas, fig_por_fila, i + 1)
        sns.regplot(x=x[col], y=y)
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
    """Representar dos histogramas en la misma figura.

    Parameters
    ----------
    x_1, x_0 : pandas.Series
        Datos de cada grupo a comparar.
    n_bins : int, optional
        Número de intervalos del histograma.
    title : str, optional
        Título mostrado en la gráfica.
    label_1, label_0 : str, optional
        Etiquetas de cada grupo.
    density : bool, optional
        Si ``True`` se muestra densidad en lugar de recuento.

    Examples
    --------
    >>> represento_doble_hist(grupo1, grupo0, n_bins=20)
    """

    # Dibujamos ambos histogramas sobre la misma figura
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
    """Histograma comparativo de cada feature separado por clase.

    Parameters
    ----------
    x : pandas.DataFrame
        Conjunto de variables de entrada.
    y : pandas.Series
        Serie con las clases objetivo.
    density : bool, optional
        Mostrar densidad en lugar de recuento.
    nbins : int, optional
        Número de intervalos para el histograma.
    targets : tuple[int, int], optional
        Etiquetas de las clases negativa y positiva.

    Examples
    --------
    >>> hist_pos_neg_feat(X_train, y_train)
    """

    fig_tot = len(x.columns)
    fig_tot_fila = 4
    fig_tamanio = 4
    # Configuramos el tamaño de la figura en función del número de variables
    num_filas = int(np.ceil(fig_tot / fig_tot_fila))
    plt.figure(figsize=(fig_tot_fila * fig_tamanio + 2, num_filas * fig_tamanio + 2))
    target_neg, target_pos = targets
    for i, feat in enumerate(x.columns):
        # Histograma de la variable ``feat`` separado por clase
        plt.subplot(num_filas, fig_tot_fila, i + 1)
        plt.title(f"{feat}")
        idx_pos = y == target_pos
        idx_neg = y == target_neg
        # Usamos la función auxiliar para superponer las distribuciones
        represento_doble_hist(
            x[feat][idx_pos].values,
            x[feat][idx_neg].values,
            nbins,
            density=density,
            title=f"{feat}",
        )



