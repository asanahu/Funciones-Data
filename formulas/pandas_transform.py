"""Transformaciones comunes con pandas."""

import pandas as pd


def combinar(df1, df2, on, how="inner"):
    """Realizar merge entre dos DataFrames."""
    return pd.merge(df1, df2, on=on, how=how)


def pivotear(df, index, columns, values, aggfunc="sum"):
    """Crear tabla dinámica."""
    tabla = pd.pivot_table(df, index=index, columns=columns, values=values, aggfunc=aggfunc)
    return tabla.reset_index()


def limpiar_nombres(df):
    """Convertir columnas a formato snake_case."""
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]+", "", regex=True)
    )
    return df


