import sqlite3 as sql
import os
import __init__

class DatastreamInitialisationFailure(Exception):
	"""
	Exception raised when Datastream object failed to initialise usually due to
	file argument being incorrect.
	"""
	def __init__(self):
		self.statement = "Datastream failed to initialise: check your parameters"

	def __str__(self): return self.statement
	def __repr__(self): return self.statement


class DatastreamInitialisationError(Exception):
	"""
	Exception raised when a Datastream object's method is called but object 
	is not initialised.
	"""
	def __init__(self):
		self.statement = "Datastream object not initalised upon function call"

	def __str__(self): return self.statement
	def __repr__(self): return self.statement


class Datastream:
	"""Easy to use wrapper for manipulating and reading database files."""

	def check_initialisation(self, function, *args, **kwargs):
		def run():
			if self.initialised:
				return function()
			else:
				raise DatastreamInitialisationError
		return run()

  total_streams: int = 0
  live_streams: int = 0

  def __new__(cls):
    Datastream.total_streams += 1
    Datastream.live_streams += 1
		
	def __init__(self, file: str = "", initialised: bool = True):
		if initialised and file != "":
			self.filename: str = file
			self.connection = sql.connect(f"{self.filename}.db")
			self.cursor = self.connection.cursor()

		elif file == "":
			raise DatastreamInitialisationError

		else:
			self.filename = None
		
		self.initialised = initialised

  def __del__(self):
    Datastream.live_streams -= 1
    self.connection.close()

	@check_initialisation
	def close_connection(self):
		self.connection.close()

	def initialise(self, filename):
		"""
		Allows datastream to remain uninitialised as long as user calls initialise() before
		calling other methods of Datastream object.
		"""
		self.filename: str = file
		self.connection = sql.connect(f"{self.filename}.db")
		self.cursor = self.connection.cursor()
		self.initialised = True

	@check_initialisation
  def create_table(self, tablename: str, fields: str):
    """
		Creates a table in the database.
		Arguments: tablename: string, fields: string
    """
    self.cursor.execute(f"CREATE TABLE {tablename} ({fields})")

	@check_initialisation
  def rename_table(self, tablename: str, new_tablename: str):
    """
    Renames an existing table
    Arguments: tablename: string, new_tablename: string
    """
  	self.cursor.execute(f"ALTER TABLE {tablename} RENAME TO {new_tablename}")

	@check_initialisation
  def add_column(self, tablename: str, column: str):
    """
    Adds a column to an existing table
    Arguments: tablename: string, column: string
    """
    self.cursor.execute(f"ALTER TABLE {tablename} ADD COLUMN {column}")

	@check_initialisation
  def add_row(self, tablename: str, column: str, values: set): 
    """
    Adds a row to an existing table
    Arguments: tablename: string, column: string, value: set
    """
    self.cursor.execute(f"INSERT INTO {tablename} VALUES {str(values)}")

	@check_initialisation
  def read_column(self, tablename: str, columns: str): 
    """
    Returns all data from a specific column(s)
    Arguments: tablename: string, columns: string
    """
    return self.cursor.execute(f"SELECT {columns} FROM {tablename}").fetchall()

	@check_initialisation
  def read_column_specific(self, tablename: str, columns: str, target: str, column_target: str): 
    """
    Returns all data from a specific column(s) where target matches in the target column.
    Arguments: tablename: string, columns: string, target: string, column_target: string
    """
    return self.cursor.execute(f"SELECT {columns} FROM {tablename} WHERE {column_target} = ?",(target)).fetchall()


# Consideration code
"""class Database(object):
	def __init__(self):
		self.files = []
		for file in os.scandir(__init__.Path.data):
			if file.endswith(".db"):
				self.files.append(file)
		self.standard_datastream = Datastream(initialised = False)"""

	

		
