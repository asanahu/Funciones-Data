"""Funciones para trabajar con archivos o URLs de HTML."""

from typing import List, Union

import os
import pandas as pd


def cargar_html(fuente: Union[str, os.PathLike]) -> List[pd.DataFrame]:
    """Cargar tablas de una URL o archivo HTML.

    Parameters
    ----------
    fuente : str or PathLike
        Ruta local o URL de la página a analizar.

    Returns
    -------
    list of pandas.DataFrame
        Todas las tablas encontradas.

    Examples
    --------
    >>> tablas = cargar_html("pagina.html")
    """
    try:
        if fuente.startswith("http://") or fuente.startswith("https://"):
            print(f"Cargando tablas desde la URL: {fuente}")
            dfs = pd.read_html(fuente)
        else:
            ruta_archivo = os.path.abspath(fuente)
            nombre_archivo_simple = os.path.basename(ruta_archivo)
            print(f"Cargando tablas desde el archivo: {nombre_archivo_simple}")
            dfs = pd.read_html(ruta_archivo)

        print(f"\nNúmero de tablas encontradas: {len(dfs)}")
        for i, df in enumerate(dfs):
            print(f"\nTabla {i+1}:")
            print(df.head())
        return dfs

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{fuente}'")
    except ValueError:
        print(
            f"Error: No se pudo cargar la fuente '{fuente}'. Verifique si contiene tablas HTML válidas."
        )
    except Exception as e:
        print(f"Error al cargar la fuente: {str(e)}")
