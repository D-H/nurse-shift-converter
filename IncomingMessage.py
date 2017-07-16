import Constants
import imaplib
import email
import os

class IncomingMessage:
    """A message received by the account gmail account"""

    def __init__(self, from_address, subject, attachment):
        self.from_address = from_address
        self.subject = subject
        self.attachment = attachment

    def download_attachment(self):
        fileName = self.attachment.get_filename()

        if bool(fileName):
            filePath = os.path.join('.', Constants.DATABASE_DOWNLOAD_FOLDER, Constants.DATABASE_DOWNLOAD_FILE)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(self.attachment.get_payload(decode=True))
                fp.close()
        else:
            print 'error downloading attachement'
            raise
