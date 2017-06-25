import re

import Constants
import datetime

def get_month(filename):
    m = re.search('(?<=\-)(.*?)(?=\-)', filename)
    month = m.group(0)

    if month in Constants.MONTH_TO_NUMBER:
        return Constants.MONTH_TO_NUMBER[month]
    else:
        return datetime.datetime.now().strftime("%m")

def get_year(filename):
    m = re.search('(\d{4})', filename)
    year = m.group(0)

    if year in Constants.ACCEPTABLE_YEARS:
        return year
    else:
        return datetime.datetime.now().strftime("%Y")

def get_utc_date_time(date, time):
    date = datetime.datetime.strptime(date, "%m-%d-%Y %H:%M:%S")
    time = datetime.datetime.strptime(time, "%H:%M:%S")

    date_time = date + datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    # wtf dawg
    # date_time = temp_date_time + datetime.timedelta(hours=12)

    # Could do conversions here
    date_time = date_time - datetime.timedelta(hours=6)

    year = date_time.year
    month = '%02d' % date_time.month
    day = '%02d' % date_time.day

    hour = '%02d' % date_time.hour
    minute = '%02d' % date_time.minute
    second = '%02d' % date_time.second

    final_utc_time = "{}{}{}T{}{}{}Z".format(year, month, day, hour, minute, second)

    return final_utc_time

