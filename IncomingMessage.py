import Constants

class IncomingMessage:
    """A message received by the account gmail account"""

    def __init__(self, from_address, subject, text, attachment):
        self.from_address = from_address
        self.subject = subject
        self.text = text
        self.attachement = attachment