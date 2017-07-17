import imaplib
import email

import Constants
import IncomingMessage

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------


def get_unread_emails():
    imap_session = __login_to_gmail()
    mail_id_list = __get_unread_mail_ids(imap_session)
    incoming_messages = __create_incoming_messages(imap_session, mail_id_list)
    __logout_of_gmail(imap_session)

    return incoming_messages


def __login_to_gmail():
    imap_session = imaplib.IMAP4_SSL(Constants.SMTP_SERVER)
    typ, account_details = imap_session.login(Constants.FROM_EMAIL,Constants.FROM_PWD)

    if typ != 'OK':
        print 'Not able to sign in!'
        raise

    return imap_session


def __get_unread_mail_ids(imap_session):
    imap_session.select('inbox')

    type, data = imap_session.search(None, Constants.EMAIL_INBOX_FILTER)

    if type != 'OK':
        print 'Error searching Inbox.'
        raise

    mail_ids = data[0]

    mail_id_list = mail_ids.split()

    return mail_id_list


def __create_incoming_messages(imap_session, mail_id_list):
    incoming_messages = []

    for i in mail_id_list:
        typ, messageParts = imap_session.fetch(i, '(RFC822)')

        if typ != 'OK':
            print 'Error fetching mail.'
            raise

        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)

        email_subject = mail['subject']
        email_from = mail['from']

        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            if not Constants.EMAIL_ATTACHMENT_FILE_EXTENSTION in part.get_filename():
                continue

            incoming_message = IncomingMessage.IncomingMessage(email_from, email_subject, part)
            incoming_messages.append(incoming_message)

    return incoming_messages

def __logout_of_gmail(imap_session):
    imap_session.close()
    imap_session.logout()

if __name__ == "__main__":
    get_unread_emails()

