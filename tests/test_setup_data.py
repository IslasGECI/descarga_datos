from descarga_datos import (
    filter_date_by_condition,
    find_report,
    read_json,
    find_filter_condition,
    setup_data_by_report,
)

import pandas as pd


conditional_year = "< 2021"

data_path = "tests/data/nidos_busqueda_aves_marinas.csv"
data_to_filter = pd.read_csv(data_path)
target_report = "tamano_poblacional.pdf"
json_path = "tests/data/analyses_tamanio.json"
analyses_list = read_json(json_path)


def test_setup_data_by_report():
    obtained = setup_data_by_report(data_to_filter, target_report, analyses_list)
    data_to_filter_len = len(data_to_filter)
    obtained_filtered_len = len(obtained)
    assert obtained_filtered_len < data_to_filter_len

    report_without_setup = "densidad_kernel_gls.pdf"
    obtained = setup_data_by_report(data_to_filter, report_without_setup, analyses_list)
    data_to_filter_len = len(data_to_filter)
    obtained_filtered_len = len(obtained)
    assert obtained_filtered_len == data_to_filter_len


def test_filter_date_by_condition():
    obtained_filtered_data = filter_date_by_condition(data_to_filter, conditional_year)
    expected_filtered_rows = 13
    obtained_filtered_data_length = len(obtained_filtered_data)
    assert obtained_filtered_data_length == expected_filtered_rows
    obtained_columns = obtained_filtered_data.columns
    assert "year" not in obtained_columns


def tests_extract_filter_condition():
    filter_condition = "< 2019"
    report_content = {
        "report": "muestreo_aves.pdf",
        "setup_data": [{"filter": "true", "season": filter_condition}],
    }
    obtained_condition = find_filter_condition(report_content)
    assert obtained_condition == filter_condition


def tests_find_report():
    target_report = "tamano_poblacional.pdf"
    obtained_content = find_report(target_report, analyses_list)
    assert "setup_data" in obtained_content.keys()

    target_report = "densidad_kernel_gls.pdf"
    obtained_content = find_report(target_report, analyses_list)
    assert "setup_data" not in obtained_content.keys()
