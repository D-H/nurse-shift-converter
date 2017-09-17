import os
import Constants


def clean_up():
    # Delete created ics file
    os.remove(Constants.OUTPUT_FILE_FULL)

    # Delete downloaded file from email
    path = os.path.join(Constants.DIR_PATH, Constants.DATABASE_DOWNLOAD_FOLDER, Constants.DATABASE_DOWNLOAD_FILE)
    os.remove(path)

