import SQLDataManager
import DateParser
import ICSFileCreator
import EmailReceiver
import EmailMessageValidator
import EmailSender
import Cleanup

import datetime


def main():
    received_emails = EmailReceiver.get_unread_emails()
    validated_emails = EmailMessageValidator.validate_messages(received_emails)

    for email in validated_emails:
        __create_ics_file(email)
        EmailSender.send_email_from_gmail(email)
        Cleanup.clean_up()
        print "Sent out email! " + str(datetime.datetime.now()) + " - " + email.from_address + " - " + email.subject


def __create_ics_file(email):
    email.download_attachment()
    month, year = DateParser.get_month_and_year(email.subject)
    calendar_entries = SQLDataManager.get_schedule_data(month, year)
    ICSFileCreator.create_ics_file(calendar_entries)

if __name__ == "__main__":
    main()