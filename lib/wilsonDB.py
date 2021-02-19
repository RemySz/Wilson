import sqlite3 as sql

"""
WilsonDB
\
\
\
Datastream:
    Easy to use wrapper for manipulating and reading database/json files.
"""

class Datastream:
    total_streams: int = 0
    live_streams: int = 0
    def __new__(cls):
        Datastream.total_streams += 1
        Datastream.live_streams += 1

    def __init__(self, file: str):
        self.filename: str = file
        self.connection = sql.connect(f"{self.filename}.db")
        self.cursor = self.connection.cursor()

    def __del__(self):
        Datastream.live_streams -= 1
        self.connection.close(f"{self.filename}.db")
        self.connection.close()

    def create_table(self, tablename: str, fields: str):
        """
            Creates a table in the database.
            Arguments: tablename: string, fields: string
        """
        self.cursor.execute(f"CREATE TABLE {tablename} ({fields})")

    def rename_table(self, tablename: str, new_tablename: str):
        """
            Renames an existing table
            Arguments: tablename: string, new_tablename: string
        """
        self.cursor.execute(f"ALTER TABLE {tablename} RENAME TO {new_tablename}")

    def add_column(self, tablename: str, column: str):
        """
            Adds a column to an existing table
            Arguments: tablename: string, column: string
        """
        self.cursor.execute(f"ALTER TABLE {tablename} ADD COLUMN {column}")

    def add_row(self, tablename: str, column: str, values: set): 
        """
            Adds a row to an existing table
            Arguments: tablename: string, column: string, value: set
        """
        self.cursor.execute(f"INSERT INTO {tablename} VALUES {str(values)}")

    def read_column(self, tablename: str, columns: str): 
        """
            Returns all data from a specific column(s)
            Arguments: tablename: string, columns: string
        """
        return self.cursor.execute(f"SELECT {columns} FROM {tablename}").fetchall()

    def read_column_specific(self, tablename: str, columns: str, target: str, column_target: str): 
        """
            Returns all data from a specific column(s) where target matches in the target column.
            Arguments: tablename: string, columns: string, target: string, column_target: string
        """
        return self.cursor.execute(f"SELECT {columns} FROM {tablename} WHERE {column_target} = ?",(target)).fetchall()



    
