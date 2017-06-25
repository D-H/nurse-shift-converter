import Constants

class CalendarEntry:
    """A single calendar entry"""

    def __get_description(self, character):
        if character in Constants.CHARACTER_TO_DESCRIPTION:
            return Constants.CHARACTER_TO_DESCRIPTION[character]
        else:
            return ''

    def __init__(self, sqL_row):
        self.date = sqL_row[0]
        self.start = sqL_row[1]
        self.end = sqL_row[2]
        self.description = self.__get_description(sqL_row[4])
