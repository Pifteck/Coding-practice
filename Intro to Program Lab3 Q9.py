from datetime import date, timedelta

def date_range_generator(start, end):
    current_date = start
    while current_date <= end:
        yield current_date
        current_date += timedelta(days=1)

startDate = date(2025, 4, 27)
endDate = date(2025, 5, 7)

for single_date in date_range_generator(startDate, endDate):
    print(single_date)