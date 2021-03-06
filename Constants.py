import os

DATABASE_DOWNLOAD_FOLDER = "DatabaseDownload/"
DATABASE_DOWNLOAD_FILE = "Downloaded_File.sqlite"
TEST_DATEBASE_FILE_NAME = "shift_worker_20-Jun-2017.sqlite"

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIRECTORY = "Output"
OUTPUT_FILE = "converted_schedule.ics"
OUTPUT_FILE_FULL = os.path.join(DIR_PATH, OUTPUT_DIRECTORY, OUTPUT_FILE)

DELAY_IN_SECONDS = 3

SQL_QUERY =  '''SELECT  date, start, end, description, character
                FROM shifts
                INNER JOIN shifttype
                ON shifts.shifttype = shifttype.primarykey
                WHERE substr(date,7,4)||substr(date,1,2)||substr(date,4,2)
                BETWEEN {} AND {}
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

MONTH_TO_YEAR = {
    'January': '2019',
    'February': '2019',
    'March': '2019',
    'April': '2019',
    'May': '2019',
    'June': '2019',
    'July': '2019',
    'August': '2019',
    'September': '2019',
    'October': '2019',
    'November': '2018',
    'December': '2018'
}

ORG_EMAIL   = "@gmail.com"
# Change to correct gmail account information
FROM_EMAIL  = "" + ORG_EMAIL
FROM_PWD    = "" 
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
SUBJECT_EMAIL = "Shifts converted for this month!"
EMAIL_ATTACHMENT_FILE_EXTENSTION = '.swc'

EMAIL_INBOX_FILTER = '(UNSEEN)'
# EMAIL_INBOX_FILTER = '(ALL)'