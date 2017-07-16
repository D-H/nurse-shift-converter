import SQLDataManager
import DateParser
import ICSFileCreator
import EmailReceiver
import EmailMessageValidator
import EmailSender
import Cleanup


def main():
    received_emails = EmailReceiver.get_unread_emails()
    validated_emails = EmailMessageValidator.validate_messages(received_emails)

    for email in validated_emails:
        __create_ics_file(email)
        EmailSender.send_email_from_gmail(email)
        Cleanup.clean_up()

def __create_ics_file(email):
    email.download_attachment()
    # month, year = DateParser.get_month(email.subject)
    month, year = DateParser.get_month_and_year('July')
    calendar_entries = SQLDataManager.get_schedule_data(month, year)
    ICSFileCreator.create_ics_file(calendar_entries)

if __name__ == "__main__":
    main()