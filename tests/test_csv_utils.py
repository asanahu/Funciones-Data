import pandas as pd
from formulas.csv_utils import cargar_csv


def test_cargar_csv_detects_delimiter_and_encoding(tmp_path):
    contenido = "col1;col2\ná;2\n"
    ruta = tmp_path / "sample.csv"
    ruta.write_bytes(contenido.encode("latin-1"))

    df = cargar_csv(ruta, imprimir=False)

    assert df is not None
    assert list(df.columns) == ["col1", "col2"]
    assert df.loc[0, "col1"] == "á"
    assert df.loc[0, "col2"] == 2
