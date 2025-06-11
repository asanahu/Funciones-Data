"""Modelos de clasificación comunes y utilidades de evaluación."""

from __future__ import annotations

from typing import Optional, Sequence, Any

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report,
    confusion_matrix,
    RocCurveDisplay,
)


def entrenar_regresion_logistica(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    **kwargs: Any,
) -> LogisticRegression:
    """Entrenar un modelo de regresión logística.

    Parameters
    ----------
    X_train : pandas.DataFrame
        Variables de entrenamiento.
    y_train : pandas.Series
        Variable objetivo.
    **kwargs : dict, optional
        Parámetros adicionales para ``LogisticRegression``.

    Returns
    -------
    sklearn.linear_model.LogisticRegression
        Modelo ajustado.

    Examples
    --------
    >>> model = entrenar_regresion_logistica(X_train, y_train)
    """
    model = LogisticRegression(**kwargs)
    model.fit(X_train, y_train)
    return model


def entrenar_mlp(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    hidden_layer_sizes: Sequence[int] = (100,),
    random_state: Optional[int] = None,
    **kwargs: Any,
) -> MLPClassifier:
    """Entrenar un ``MLPClassifier`` de scikit-learn.

    Parameters
    ----------
    X_train : pandas.DataFrame
        Variables de entrenamiento.
    y_train : pandas.Series
        Variable objetivo.
    hidden_layer_sizes : sequence of int, optional
        Estructura de capas ocultas.
    random_state : int, optional
        Semilla para la aleatoriedad.
    **kwargs : dict, optional
        Parámetros adicionales para ``MLPClassifier``.

    Returns
    -------
    sklearn.neural_network.MLPClassifier
        Modelo ajustado.

    Examples
    --------
    >>> model = entrenar_mlp(X_train, y_train, hidden_layer_sizes=(50, 50))
    """
    model = MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes,
        random_state=random_state,
        **kwargs,
    )
    model.fit(X_train, y_train)
    return model


def entrenar_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    n_estimators: int = 100,
    random_state: Optional[int] = None,
    **kwargs: Any,
) -> RandomForestClassifier:
    """Entrenar un ``RandomForestClassifier``.

    Parameters
    ----------
    X_train : pandas.DataFrame
        Variables de entrenamiento.
    y_train : pandas.Series
        Variable objetivo.
    n_estimators : int, optional
        Número de árboles del bosque.
    random_state : int, optional
        Semilla para la aleatoriedad.
    **kwargs : dict, optional
        Parámetros adicionales para ``RandomForestClassifier``.

    Returns
    -------
    sklearn.ensemble.RandomForestClassifier
        Modelo ajustado.

    Examples
    --------
    >>> model = entrenar_random_forest(X_train, y_train, n_estimators=200)
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
        **kwargs,
    )
    model.fit(X_train, y_train)
    return model


def evaluar_modelo(
    model: Any,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    titulo: str = "",
) -> dict[str, float]:
    """Calcular métricas y mostrar gráficas de evaluación.

    Se imprime el ``classification_report`` y se representan la matriz de
    confusión y la curva ROC (si es un problema binario).

    Parameters
    ----------
    model : estimador de scikit-learn
        Modelo previamente entrenado.
    X_test : pandas.DataFrame
        Variables de prueba.
    y_test : pandas.Series
        Valores reales de la variable objetivo.
    titulo : str, optional
        Texto a añadir al título de las gráficas.

    Returns
    -------
    dict[str, float]
        Diccionario con ``accuracy``, ``precision`` y ``recall``.

    Examples
    --------
    >>> metricas = evaluar_modelo(modelo, X_test, y_test)
    """
    y_pred = model.predict(X_test)
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_prob = None

    # Matriz de confusión
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Matriz de Confusión" + (f" - {titulo}" if titulo else ""))
    plt.xlabel("Predicho")
    plt.ylabel("Real")
    plt.tight_layout()
    plt.show()

    # Curva ROC solo para binario
    if y_prob is not None and len(set(y_test)) == 2:
        RocCurveDisplay.from_predictions(y_test, y_prob)
        plt.title("Curva ROC" + (f" - {titulo}" if titulo else ""))
        plt.tight_layout()
        plt.show()

    precision = precision_score(
        y_test, y_pred, average="binary" if len(set(y_test)) == 2 else "weighted"
    )
    recall = recall_score(
        y_test, y_pred, average="binary" if len(set(y_test)) == 2 else "weighted"
    )
    accuracy = accuracy_score(y_test, y_pred)

    print("\nReporte de clasificación:\n")
    print(classification_report(y_test, y_pred))

    return {"accuracy": accuracy, "precision": precision, "recall": recall}
