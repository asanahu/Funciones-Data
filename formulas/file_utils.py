"""Funciones genéricas para detección de archivos."""

import os
import pandas as pd
from typing import Union
from .csv_utils import cargar_csv
from .json_utils import cargar_json
from .excel_utils import leer_excel
from .html_utils import cargar_html


def cargar_archivo(nombre_archivo: Union[str, os.PathLike]) -> pd.DataFrame:
    """Cargar un archivo según su extensión.

    Parameters
    ----------
    nombre_archivo : str or PathLike
        Ruta del archivo a cargar.

    Returns
    -------
    pandas.DataFrame
        Datos cargados del archivo.

    Examples
    --------
    >>> df = cargar_archivo("datos.csv")
    """
    extension = os.path.splitext(nombre_archivo)[1].lower()
    ruta_archivo = os.path.abspath(nombre_archivo)
    if extension == ".csv":
        return cargar_csv(ruta_archivo)
    if extension == ".json":
        return cargar_json(ruta_archivo)
    if extension in [".xls", ".xlsx"]:
        return leer_excel(ruta_archivo)
    if extension in [".htm", ".html"]:
        return cargar_html(ruta_archivo)
    if extension == ".parquet":
        return pd.read_parquet(ruta_archivo)
    if extension == ".h5":
        return pd.read_hdf(ruta_archivo)
    if extension == ".feather":
        return pd.read_feather(ruta_archivo)
    if extension == ".pkl":
        return pd.read_pickle(ruta_archivo)
    if extension == ".dta":
        return pd.read_stata(ruta_archivo)
    if extension == ".sav":
        return pd.read_spss(ruta_archivo)
    raise ValueError(f"Formato de archivo no soportado: {extension}")

