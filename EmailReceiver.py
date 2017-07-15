import imaplib
import email
import os

import Constants

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

detach_dir = '.'

def read_email_from_gmail():
    try:
        imapSession = imaplib.IMAP4_SSL(Constants.SMTP_SERVER)
        typ, accountDetails = imapSession.login(Constants.FROM_EMAIL,Constants.FROM_PWD)

        if typ != 'OK':
            print 'Not able to sign in!'
            raise

        imapSession.select('inbox')

        # type, data = mail.search(None, '(UNSEEN)')
        type, data = imapSession.search(None, '(ALL)')

        if type != 'OK':
            print 'Error searching Inbox.'
            raise

        mail_ids = data[0]

        mail_id_list = mail_ids.split()
        # first_email_id = int(id_list[0])
        # latest_email_id = int(id_list[-1])


        for i in mail_id_list[1]:
            typ, messageParts = imapSession.fetch(i, '(RFC822)' )

            if typ != 'OK':
                print 'Error fetching mail.'
                raise

            emailBody = messageParts[0][1]
            mail = email.message_from_string(emailBody)

            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    # print part.as_string()
                    continue
                if part.get('Content-Disposition') is None:
                    # print part.as_string()
                    continue

                fileName = part.get_filename()

                if bool(fileName):
                    filePath = os.path.join(detach_dir, 'DatabaseDownload', fileName)
                    if not os.path.isfile(filePath):
                        print fileName
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()

        imapSession.close()
        imapSession.logout()

    except Exception, e:
        print str(e)

if __name__ == "__main__":
    read_email_from_gmail()

