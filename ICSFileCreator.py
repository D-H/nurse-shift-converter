import Constants
import DateParser

def __write_header(output_file):
    output_file.write('BEGIN:VCALENDAR\n')
    output_file.write('VERSION:2.0\n')

def __write_footer(output_file):
    output_file.write('END:VCALENDAR\n')

def __write_events(output_file, calender_entries):
    for entry in calender_entries:
        start_date_time = DateParser.get_utc_date_time(entry.date, entry.start)
        end_date_time = DateParser.get_utc_date_time(entry.date, entry.end)

        output_file.write('BEGIN:VEVENT\n')
        output_file.write('UID:{}-SWAGYO@example.com\n'.format(start_date_time))
        output_file.write('DTSTAMP:{}\n'.format(start_date_time))
        output_file.write('DTSTART:{}\n'.format(start_date_time))
        output_file.write('DTEND:{}\n'.format(end_date_time))
        output_file.write('SUMMARY:{}\n'.format(entry.description))
        output_file.write('END:VEVENT\n')


def create_ics_file(calender_entries):
    with open(Constants.OUTPUT_FILE, 'w+') as output_file:
        __write_header(output_file)
        __write_events(output_file, calender_entries)
        __write_footer(output_file)