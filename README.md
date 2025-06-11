# Repositorio de fórmulas para ETL y análisis de datos

Este proyecto agrupa funciones reutilizables para manipulación y exploración de 
datos con **pandas**. Las utilidades están organizadas en el paquete `formulas` y
se acompañan de algunos notebooks de ejemplo.

## Estructura principal

```
formulas/
    excel_utils.py      # Leer y escribir Excel
    csv_utils.py        # Limpieza y carga de CSV
    json_utils.py       # Manejo de JSON
    sql_utils.py        # Conexión a bases de datos
    pandas_transform.py # Transformaciones comunes con pandas
    estadisticas.py     # Resúmenes y cálculos estadísticos
    visualizaciones.py  # Gráficos rápidos (líneas, barras, scatter...)
```

Los notebooks de la carpeta `ejemplos` muestran cómo utilizar estas funciones
para tareas habituales.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso rápido

Importa las funciones que necesites desde `formulas`:

```python
from formulas import (
    cargar_csv,
    nulos,
    grafico_lineas,
    grafico_barras,
    convertir_a_datetime,
)

df = cargar_csv("datos.csv")
resumen = nulos(df)
df = convertir_a_datetime(df, "fecha")
grafico_lineas(df, "fecha", "ventas", titulo="Ventas diarias")
grafico_barras(df, "producto", "ventas")
```

Consulta cada módulo para obtener más detalles y ejemplos de uso.

## Nuevas transformaciones

El módulo `pandas_transform` incluye utilidades para convertir columnas de
fechas y detectar valores atípicos con el método IQR, además de funciones para
eliminar duplicados, imputar nulos y codificar variables categóricas mediante
one-hot encoding.

El módulo `estadisticas` ahora cuenta con `resumen_dataset` para obtener de un
vistazo las dimensiones, tipos y porcentaje de nulos de un DataFrame.

## Estandarización y división en train/test

El módulo `model_utils` incorpora herramientas básicas para preparar datos de
modelado. Con `dividir_train_test` puedes separar un DataFrame en conjuntos de
entrenamiento y prueba, mientras que `estandarizar_datos` aplica un
`StandardScaler` de *scikit-learn* a las columnas numéricas.

```python
from formulas import dividir_train_test, estandarizar_datos

X_train, X_test, y_train, y_test = dividir_train_test(df, "objetivo")
X_train, scaler = estandarizar_datos(X_train)
X_test[scaler.feature_names_in_] = scaler.transform(X_test[scaler.feature_names_in_])
```

## Modelos de clasificación

Para entrenar y evaluar modelos de clasificación se incluyen utilidades para
regresión logística, redes neuronales (*MLPClassifier*) y bosques aleatorios.
Al evaluar un modelo se muestran automáticamente la matriz de confusión y la
curva ROC junto con métricas de *precision*, *recall* y *accuracy*.

```python
from formulas import (
    entrenar_regresion_logistica,
    entrenar_mlp,
    entrenar_random_forest,
    evaluar_modelo,
    dividir_train_test,
)

X_train, X_test, y_train, y_test = dividir_train_test(df, "objetivo")
modelo = entrenar_regresion_logistica(X_train, y_train)
metricas = evaluar_modelo(modelo, X_test, y_test)
print(metricas)
```

De forma análoga pueden usarse `entrenar_mlp` o `entrenar_random_forest`
pasando los parámetros deseados.

