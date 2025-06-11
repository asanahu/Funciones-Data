# Repositorio de fórmulas para ETL

Este repositorio contiene una colección de funciones útiles para analistas de datos.
Las funciones están escritas en **Python** y permiten cargar datos de diferentes
formatos, explorar su contenido y realizar tareas básicas de limpieza.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias en un entorno de Python (se recomienda `virtualenv`).
   ```bash
   pip install pandas seaborn matplotlib
   ```

## Uso

Importa el módulo `etl_utils` en tus notebooks o scripts y utiliza las funciones
según el tipo de archivo o la operación que necesites realizar.

```python
from etl_utils import cargar_csv, nulos, matriz_correlacion

df = cargar_csv('archivo.csv')
resumen = nulos(df)
matriz = matriz_correlacion(df, imprimir=True)
```

Consulta la documentación dentro de cada función para conocer los parámetros y
ver ejemplos de uso.

