"""Módulo para trabajar con bases de datos usando SQLAlchemy."""

from typing import Any

import pandas as pd
from sqlalchemy import create_engine


def crear_conexion(url: str) -> Any:
    """Crear un motor de conexión a partir de una URL.

    Parameters
    ----------
    url : str
        Cadena de conexión a la base de datos.

    Returns
    -------
    sqlalchemy.Engine
        Motor de conexión creado.

    Examples
    --------
    >>> engine = crear_conexion('sqlite:///data.db')
    """
    engine = create_engine(url)
    return engine


def leer_query(sql: str, engine: Any) -> pd.DataFrame:
    """Ejecutar una consulta y devolver un DataFrame.

    Parameters
    ----------
    sql : str
        Consulta SQL a ejecutar.
    engine : sqlalchemy.Engine
        Conexión a utilizar.

    Returns
    -------
    pandas.DataFrame
        Resultado de la consulta.
    """
    with engine.connect() as conn:
        df = pd.read_sql(sql, conn)
    return df


def escribir_df(df: pd.DataFrame, tabla: str, engine: Any, if_exists: str = "replace") -> None:
    """Guardar un DataFrame en la tabla indicada.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame a guardar.
    tabla : str
        Nombre de la tabla destino.
    engine : sqlalchemy.Engine
        Conexión a utilizar.
    if_exists : str, optional
        Comportamiento si la tabla existe, por defecto ``"replace"``.

    Examples
    --------
    >>> escribir_df(df, 'ventas', engine)
    """
    with engine.connect() as conn:
        df.to_sql(tabla, conn, if_exists=if_exists, index=False)


