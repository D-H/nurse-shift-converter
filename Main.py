import SQLDataManager
import DateParser
import Constants
import ICSFileCreator

def main():

    month = DateParser.get_month(Constants.TEST_DATEBASE_FILE_NAME)
    year = DateParser.get_year(Constants.TEST_DATEBASE_FILE_NAME)
    calendar_entries = SQLDataManager.get_schedule_data(month, year)
    ICSFileCreator.create_ics_file(calendar_entries)


if __name__ == "__main__":
    main()