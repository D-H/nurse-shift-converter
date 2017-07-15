DATABASE_DOWNLOAD_FOLDER = "DatabaseDownload/"
TEST_DATEBASE_FILE_NAME = "shift_worker_06-Jul-2017.swc"

OUTPUT_FILE_DIRECTORY = "Output/"
OUTPUT_FILE = "converted_schedule.ics"

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
    'N12': 'Night shift - 12 hours',
    'O': 'Could pick up'
}


MONTH_TO_NUMBER = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
}

# Prevent SQL Injections
ACCEPTABLE_YEARS = ['2017', '2018', '2019']

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "shift.converter.mountain.time" + ORG_EMAIL
FROM_PWD    = "converter4Sofe"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993