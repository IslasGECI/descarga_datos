def filter_date_by_condition(data_to_filter, conditional_year):
    data_to_filter["year"] = data_to_filter["Fecha"].str.slice(7, 11).astype(int)
    return data_to_filter.query("year " + conditional_year)
