import pandas as pd

from formulas.pandas_transform import convertir_a_datetime, limpiar_nombres


def test_limpiar_nombres_snake_case():
    df = pd.DataFrame(columns=[" Col 1 ", "Col-2", "COL 3"])
    result = limpiar_nombres(df)
    assert list(result.columns) == ["col_1", "col2", "col_3"]


def test_convertir_a_datetime_single_column():
    df = pd.DataFrame({"fecha": ["2021-01-01", "2021-02-01"]})
    result = convertir_a_datetime(df, "fecha")
    assert pd.api.types.is_datetime64_any_dtype(result["fecha"])
    assert result.loc[0, "fecha"] == pd.Timestamp("2021-01-01")
