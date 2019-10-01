def group_measurements(query_set, data, slice, aggregate_type):
    raw_data = {}
    dates = []
    for measurement in query_set.order_by("created_at"):
        d = getattr(measurement, data, None)
        if not d:
            continue
        date = None
        if slice == "month":
            date = measurement.created_at.strftime("%b %y")
        if date not in dates:
            dates.append(date)
        m = raw_data.get(date, None)
        if m:
            raw_data[date]["data"].append(d)
        else:
            raw_data[date] = {"data": [d]}

    measurements = []
    for date in dates:
        all_data = raw_data[date]["data"]
        data = 0
        if aggregate_type == "sum":
            data = sum(map(float, all_data))
        m = {"date": date, "data": data}
        measurements.append(m)
    return measurements
