from descarga_datos import filter_date_by_condition

import pandas as pd


def test_filter_date_by_condition():
    data_path = "tests/data/nidos_busqueda_aves_marinas.csv"
    data_to_filter = pd.read_csv(data_path)
    conditional_year = "< 2021"
    filter_date_by_condition(data_to_filter, conditional_year)
