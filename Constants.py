DATABASE_DOWNLOAD_FOLDER = "DatabaseDownload/"
TEST_DATEBASE_FILE_NAME = "shift_worker_22-Jun-2017.swc"

OUTPUT_FILE = "Output/converted_schedule.ics"

SQL_QUERY =  '''SELECT  date, start, end, description, character
                FROM shifts
                INNER JOIN shifttype
                ON shifts.shifttype = shifttype.primarykey
                WHERE date >= "{}"
                AND date < "{}"
                ORDER BY DATE; '''

CHARACTER_TO_DESCRIPTION = {
    'd8': 'Day shift - 8 hours',
    'D12': 'Day shift - 12 hours',
    'E12': 'Evening shift - 12 hours',
    'N8': 'Night shift - 8 hours',
    'N12': 'Night shift - 12 hours'
}


MONTH_TO_NUMBER = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}

# Prevent SQL Injections
ACCEPTABLE_YEARS = ['2017', '2018', '2019']