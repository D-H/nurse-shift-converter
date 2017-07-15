import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

import Constants

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

detach_dir = '.'

def send_email_from_gmail():
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(Constants.FROM_EMAIL, Constants.FROM_PWD)

        emaillist = ['david.clifford.henderson@gmail.com']
        msg = MIMEMultipart()
        msg['Subject'] = 'Dis subject'
        msg['From'] = Constants.FROM_EMAIL
        msg['Reply-to'] = Constants.FROM_EMAIL

        msg.preamble = 'Multipart message.\n'

        part = MIMEText("Swof")
        msg.attach(part)

        part = MIMEApplication(open("Output/converted_schedule.ics", "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename="converted_schedule.ics")
        msg.attach(part)

        server.sendmail(msg['From'], emaillist, msg.as_string())

        server.quit()

    except Exception, e:
        print str(e)

if __name__ == "__main__":
    send_email_from_gmail()

