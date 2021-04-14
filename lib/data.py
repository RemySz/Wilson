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

# Packages
from enum import Enum
import json


class FileType(Enum):
    Json = 0
    Rect = 1
    Python = 2
    Txt = 3


class DataSteam:
    """
    Finds user file and returns a dictionary of all the user information inside.
    """
    def __init__(self, directory="", file=None, type_: FileType = FileType.Json):
        self.file = file
        self.directory = directory
        self.contents: str
        self.type = type_
        if self.file is not None:
            with open(self.directory + self.file, 'r') as f:
                if self.type == FileType.Json:
                    self.contents = json.load(f)
                else:
                    self.contents = None
                    return

    def get_file(self, file):
        self.file = file
        with open(self.directory + self.file, 'r') as f:
            if self.type == FileType.Json:
                self.contents = json.load(f)
            else:
                self.contents = None
                return

    def set_directory(self, new_directory):
        self.directory = new_directory
        return

    def field(self, fields=None):
        output = 0
        if fields is not None:
            fields = list(fields)
            output = self.contents[fields[0]]
            if len(fields) == 1:
                del fields
                return output
            else:
                for i in range(1, len(fields)-1):
                    output = output[fields[i]]
                del fields
                return output
        return





class DataSearch:
    """

    """
    pass


class DataBase:
    """

    """
    pass





