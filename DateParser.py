import re

import Constants
import datetime


def get_month_and_year(subject):
    for month in Constants.MONTH_TO_NUMBER:
        if month in subject:
            return Constants.MONTH_TO_NUMBER[month], Constants.MONTH_TO_YEAR[month]

    print "Could not parse date in " + subject
    raise


def get_utc_date_time_end_date(date, start_time, end_time):
    day_changed_during_shift = False

    # The day has skipped over because start time is before end time
    if end_time < start_time:
        day_changed_during_shift = True

    return get_utc_date_time(date, end_time, day_changed_during_shift)

def get_utc_date_time(date, time, day_changed_during_shift):
    date = datetime.datetime.strptime(date, "%m-%d-%Y %H:%M:%S")
    time = datetime.datetime.strptime(time, "%H:%M:%S")

    # Add extra day to schedule
    if day_changed_during_shift:
        date = date + datetime.timedelta(days=1)

    # Combine date and time
    date_time = date + datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    # UTC to mountain time
    date_time = date_time + datetime.timedelta(hours=6)

    year = date_time.year
    month = '%02d' % date_time.month
    day = '%02d' % date_time.day

    hour = '%02d' % date_time.hour
    minute = '%02d' % date_time.minute
    second = '%02d' % date_time.second

    final_utc_time = "{}{}{}T{}{}{}Z".format(year, month, day, hour, minute, second)

    return final_utc_time

