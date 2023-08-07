from descarga_datos import filter_date_by_condition

import pandas as pd


conditional_year = "< 2021"


def test_filter_date_by_condition():
    data_path = "tests/data/nidos_busqueda_aves_marinas.csv"
    data_to_filter = pd.read_csv(data_path)
    obtained_filtered_data = filter_date_by_condition(data_to_filter, conditional_year)
    expected_filtered_rows = 13
    obtained_filtered_data_length = len(obtained_filtered_data)
    assert obtained_filtered_data_length == expected_filtered_rows
    obtained_columns = obtained_filtered_data.columns
    assert "year" not in obtained_columns
