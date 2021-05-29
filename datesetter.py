def date_formatter(date):
    d = str(date)
    dt = d.split('-')
    new = dt[2]+'-'+dt[1]+'-'+dt[0]
    return (new)