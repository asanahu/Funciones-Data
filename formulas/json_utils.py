"""Herramientas para archivos JSON."""

from typing import Union

import os
import json
import pandas as pd


def cargar_json(
    nombre_archivo: Union[str, os.PathLike], imprimir: bool = True, **kwargs
) -> pd.DataFrame:
    """Leer un archivo JSON.

    Parameters
    ----------
    nombre_archivo : str or PathLike
        Ruta del archivo JSON.

    Returns
    -------
    pandas.DataFrame
        DataFrame con la información del JSON.

    Examples
    --------
    >>> df = cargar_json("datos.json")
    """
    try:
        ruta_archivo = os.path.abspath(nombre_archivo)
        nombre_archivo_simple = os.path.basename(ruta_archivo)
        df = pd.read_json(ruta_archivo, **kwargs)
        if imprimir:
            print(f"Archivo JSON cargado: {nombre_archivo_simple}")
            print(f"Forma del DataFrame: {df.shape}")
            print("\nPrimeras filas del dataset:")
            print(df.head())
            print("\nTipos de datos:")
            print(df.dtypes)
        return df
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
    except ValueError:
        print(
            f"Error: No se pudo cargar el archivo '{nombre_archivo}'. Verifique si el archivo está en formato JSON válido o no está vacío."
        )
    except json.JSONDecodeError:
        print(
            f"Error: No se pudo analizar el archivo '{nombre_archivo}'. Verifique que el contenido tenga un formato JSON válido."
        )
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")


