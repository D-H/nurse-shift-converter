import sqlite3
import Constants
from CalendarEntry import CalendarEntry


def get_schedule_data(month, year):
    # Connect to database
    connection_string = Constants.DATABASE_DOWNLOAD_FOLDER + Constants.TEST_DATEBASE_FILE_NAME
    conn = sqlite3.connect(connection_string)
    c = conn.cursor()

    # Create query
    start_date = "{}-01-{}".format(month, year)
    end_date = "{}-31-{}".format(month, year)

    start_date = "08-01-2017".format(month, year)
    end_date = "08-31-2017".format(month, year)

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
