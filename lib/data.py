"""
For managing and scraping data from json files.

Classes:
    DataStream:
        inputting/outputting data from a specific file

    DataSearch:
        finding a specific file in a directory

    DataBase:
        for managing a large set of files
"""


class DataSteam:
    """

    """
    def __init__(self, file=None):
        self.file = file
        self.contents = ""
        with open(self.file, 'r') as f:
            self.contents = f.read()


class DataSearch:
    """

    """
    pass


class DataBase:
    """

    """
    pass






