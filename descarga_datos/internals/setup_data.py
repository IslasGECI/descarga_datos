import json


def setup_data_by_report(data_to_filter, target_report, analyses_list):
    report_content = find_report(target_report, analyses_list)
    filter_condition = find_filter_condition(report_content)
    return filter_date_by_condition(data_to_filter, filter_condition)


def filter_date_by_condition(data_to_filter, conditional_year):
    copy_data_to_filter = data_to_filter.copy()
    copy_data_to_filter["year"] = copy_data_to_filter["Fecha"].str.slice(7, 11).astype(int)
    copy_data_to_filter.query("year " + conditional_year, inplace=True)
    return copy_data_to_filter.drop(columns=["year"])


def find_filter_condition(report_content):
    return report_content["setup_data"][0]["season"]


def find_report(target_report, analyses_list):
    target_report_content = [
        report_content
        for report_content in analyses_list
        if report_content["report"] == target_report
    ]
    return target_report_content[0]


def read_json(json_path):
    with open(json_path) as json_analyses:
        analyses_list = json.load(json_analyses)
    return analyses_list
