"""Funciones útiles para tareas de ETL.

Cada función está pensada para trabajar con distintos tipos de entrada y
facilitar las primeras etapas de exploración y limpieza de datos.
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def cargar_csv(nombre_archivo):
    """Cargar un archivo CSV y mostrar un resumen inicial.

    Parameters
    ----------
    nombre_archivo : str
        Ruta del archivo CSV.
    Returns
    -------
    pandas.DataFrame
    """
    ruta_archivo = os.path.abspath(nombre_archivo)
    df = pd.read_csv(ruta_archivo)
    print(f"Archivo CSV cargado: {os.path.basename(ruta_archivo)}")
    print("\nPrimeras filas del dataset:")
    print(df.head())
    print("\nResumen estadístico del DataFrame:")
    print(df.describe())
    return df


def cargar_json(nombre_archivo):
    """Cargar un archivo JSON y mostrar un resumen inicial."""
    ruta_archivo = os.path.abspath(nombre_archivo)
    df = pd.read_json(ruta_archivo)
    print(f"Archivo JSON cargado: {os.path.basename(ruta_archivo)}")
    print("\nPrimeras filas del dataset:")
    print(df.head())
    print("\nResumen estadístico del DataFrame:")
    print(df.describe())
    return df


def cargar_excel(nombre_archivo, hoja=None):
    """Cargar un archivo Excel.

    Si `hoja` es None se cargará la primera hoja disponible.
    """
    ruta_archivo = os.path.abspath(nombre_archivo)
    if hoja:
        df = pd.read_excel(ruta_archivo, sheet_name=hoja)
    else:
        df = pd.read_excel(ruta_archivo)
    print(f"Archivo Excel cargado: {os.path.basename(ruta_archivo)}")
    print("\nPrimeras filas del dataset:")
    print(df.head())
    print("\nResumen estadístico del DataFrame:")
    print(df.describe())
    return df


def cargar_html(fuente):
    """Cargar tablas desde un archivo o URL HTML."""
    if fuente.startswith("http://") or fuente.startswith("https://"):
        dfs = pd.read_html(fuente)
    else:
        ruta = os.path.abspath(fuente)
        dfs = pd.read_html(ruta)
    print(f"Número de tablas encontradas: {len(dfs)}")
    for i, df in enumerate(dfs, 1):
        print(f"\nTabla {i}:")
        print(df.head())
    return dfs


def cargar_archivo(nombre_archivo):
    """Cargar un archivo según su extensión."""
    extension = os.path.splitext(nombre_archivo)[1].lower()
    if extension == ".csv":
        return cargar_csv(nombre_archivo)
    if extension == ".json":
        return cargar_json(nombre_archivo)
    if extension in [".xls", ".xlsx"]:
        return cargar_excel(nombre_archivo)
    if extension == ".html":
        return cargar_html(nombre_archivo)[0]
    raise ValueError(f"Formato de archivo no soportado: {extension}")


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
