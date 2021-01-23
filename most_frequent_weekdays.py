import calendar


def most_frequent_days(year):

    my_calendar = calendar.Calendar(firstweekday=0)
    week_days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
                 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    week_days_accumulator = []
    month = 1

    while month <= 12:
        for days_list in my_calendar.monthdays2calendar(year, month):
            for days_tuple in days_list:
                if days_tuple[0] != 0:
                    week_days_accumulator.append(days_tuple[1])
        month += 1

    days_frequency = {key: week_days_accumulator.count(
        day) for key, day in week_days.items()}
    max_frequency = max(days_frequency.values())

    return [key for key, value in days_frequency.items()
            if value == max_frequency]
