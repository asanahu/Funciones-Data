"""Módulo para trabajar con bases de datos usando SQLAlchemy."""

import pandas as pd
from sqlalchemy import create_engine


def crear_conexion(url):
    """Crear un motor de conexión a partir de una URL."""
    engine = create_engine(url)
    return engine


def leer_query(sql, engine):
    """Ejecutar una consulta y devolver un DataFrame."""
    with engine.connect() as conn:
        df = pd.read_sql(sql, conn)
    return df


def escribir_df(df, tabla, engine, if_exists="replace"):
    """Guardar un DataFrame en la tabla indicada."""
    with engine.connect() as conn:
        df.to_sql(tabla, conn, if_exists=if_exists, index=False)


