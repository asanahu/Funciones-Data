"""Funciones para gráficos con matplotlib, seaborn y plotly."""

import matplotlib.pyplot as plt
import seaborn as sns


def grafico_lineas(df, x, y, titulo=""):
    """Crear un gráfico de líneas sencillo."""
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=df, x=x, y=y)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()


