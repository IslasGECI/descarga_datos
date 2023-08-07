def filter_date_by_condition(data_to_filter, conditional_year):
    copy_data_to_filter = data_to_filter.copy()
    copy_data_to_filter["year"] = copy_data_to_filter["Fecha"].str.slice(7, 11).astype(int)
    copy_data_to_filter.query("year " + conditional_year, inplace=True)
    return copy_data_to_filter.drop(columns=["year"])
