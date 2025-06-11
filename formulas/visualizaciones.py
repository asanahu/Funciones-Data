"""Funciones para gráficos con matplotlib, seaborn y plotly."""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


