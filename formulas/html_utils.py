"""Funciones para trabajar con archivos o URLs de HTML."""

import os
import pandas as pd


def cargar_html(fuente):
    """Cargar tablas de una URL o archivo HTML.

    Devuelve una lista de DataFrames con las tablas encontradas.
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
