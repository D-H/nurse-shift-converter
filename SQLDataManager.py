import sqlite3
import Constants
from CalendarEntry import CalendarEntry


def get_schedule_data(month, year):
    # Connect to database
    connection_string = Constants.DATABASE_DOWNLOAD_FOLDER + Constants.DATABASE_DOWNLOAD_FILE
    conn = sqlite3.connect(connection_string)
    c = conn.cursor()

    # Create query
    start_date = "'{}{}00'".format(year, month)
    end_date = "'{}{}32'".format(year, month)

    completed_sql_query = Constants.SQL_QUERY.format(start_date, end_date)

    # Exectue query
    c.execute(completed_sql_query)
    result = c.fetchall()

    # Create objects
    result_list = []
    for row in result:
        temp = CalendarEntry(row)
        result_list.append(temp)

    return result_list
