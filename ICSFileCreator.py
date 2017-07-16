import Constants
import DateParser
import os

def __write_header(output_file):
    output_file.write('BEGIN:VCALENDAR\r\n')
    output_file.write('VERSION:2.0\r\n')
    output_file.write('PRODID:-DavidH\r\n')

def __write_footer(output_file):
    output_file.write('END:VCALENDAR\r\n')

def __write_events(output_file, calender_entries):
    for entry in calender_entries:
        start_date_time = DateParser.get_utc_date_time(entry.date, entry.start, False)
        end_date_time = DateParser.get_utc_date_time_end_date(entry.date, entry.start, entry.end)

        output_file.write('BEGIN:VEVENT\r\n')
        output_file.write('UID:{}-SWAGYO@example.com\r\n'.format(start_date_time))
        output_file.write('DTSTART:{}\r\n'.format(start_date_time))
        output_file.write('DTEND:{}\r\n'.format(end_date_time))
        output_file.write('SUMMARY:{}\r\n'.format(entry.description))
        output_file.write('END:VEVENT\r\n')


def create_ics_file(calender_entries):
    with open(Constants.OUTPUT_FILE_FULL, 'w+') as output_file:
        __write_header(output_file)
        __write_events(output_file, calender_entries)
        __write_footer(output_file)