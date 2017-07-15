import SQLDataManager
import DateParser
import Constants
import ICSFileCreator

# 1 - Get email
# 2 - Convert
# 3 - Clean up
# 4 - Send email

def main():

    month = DateParser.get_month(Constants.TEST_DATEBASE_FILE_NAME)
    year = DateParser.get_year(Constants.TEST_DATEBASE_FILE_NAME)
    calendar_entries = SQLDataManager.get_schedule_data(month, year)
    ICSFileCreator.create_ics_file(calendar_entries)


if __name__ == "__main__":
    main()