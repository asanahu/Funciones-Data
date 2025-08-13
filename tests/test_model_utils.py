import pandas as pd
import pytest
from formulas.model_utils import dividir_train_test, estandarizar_datos


def test_dividir_train_test_stratified():
    df = pd.DataFrame({
        "A": range(100),
        "B": range(100, 200),
        "target": [0, 1] * 50,
    })
    X_train, X_test, y_train, y_test = dividir_train_test(
        df, "target", test_size=0.2, random_state=42, estratificar=True
    )
    assert X_train.shape[0] == 80
    assert X_test.shape[0] == 20
    assert y_train.value_counts()[0] == 40
    assert y_train.value_counts()[1] == 40
    assert y_test.value_counts()[0] == 10
    assert y_test.value_counts()[1] == 10


def test_estandarizar_datos_default_columns():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": ["x", "y", "z"],
    })
    scaled, scaler = estandarizar_datos(df)
    assert list(scaled.columns) == ["A", "B", "C"]
    assert all(scaled["C"] == df["C"])
    assert scaled["A"].mean() == pytest.approx(0, abs=1e-8)
    assert scaled["A"].std(ddof=0) == pytest.approx(1, abs=1e-8)
    assert scaled["B"].mean() == pytest.approx(0, abs=1e-8)
    assert scaled["B"].std(ddof=0) == pytest.approx(1, abs=1e-8)
    assert list(scaler.mean_) == pytest.approx([2.0, 5.0])
