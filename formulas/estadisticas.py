"""Cálculos estadísticos básicos y avanzados."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def nulos(df, ordenar_por="Nulos", imprimir=True):
    """Resumen de valores nulos, porcentaje y valores únicos."""
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


def describir_columnas(df, columnas):
    """Mostrar información resumida de un conjunto de columnas."""
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


def matriz_correlacion(df, imprimir=False):
    """Calcular y mostrar la matriz de correlación para columnas numéricas."""
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


