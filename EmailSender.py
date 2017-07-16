import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import Constants

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def send_email_from_gmail(email):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(Constants.FROM_EMAIL, Constants.FROM_PWD)

        emaillist = [email.from_address]
        msg = MIMEMultipart()
        msg['Subject'] = Constants.SUBJECT_EMAIL
        msg['From'] = Constants.FROM_EMAIL
        msg['Reply-to'] = Constants.FROM_EMAIL

        msg.preamble = 'Multipart message.\n'

        part = MIMEText("Please let me know if anything is messed up! Just reply to this email.")
        msg.attach(part)

        part = MIMEApplication(open(Constants.OUTPUT_FILE_FULL, "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=Constants.OUTPUT_FILE)
        msg.attach(part)

        server.sendmail(msg['From'], emaillist, msg.as_string())

        server.quit()

    except Exception, e:
        print str(e)

