import Constants

# -------------------------------------------------
#
# Utility to validate email messages
#
# ------------------------------------------------


def validate_messages(incoming_messages):
    valid_messages = __validate_message_subject(incoming_messages)

    return valid_messages


def __validate_message_subject(messages):
    valid_messages = []

    for message in messages:
        for month in Constants.MONTH_TO_NUMBER:
            if month in message.subject:
                valid_messages.append(message)

    return valid_messages




