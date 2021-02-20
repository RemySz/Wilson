"""
lib: library folder contains all external libraries used in commands.
This helps keep commands small which improves readability.

Todo list:
- loki guild manager: gives guilds different commands depending on what flags are given upon init.
- github wrapper: basic wrapper around PyGitHub to access specific repositories.
- wilsonDB: basic database manager

"""
import os

class Path(object):
	def __init__(self):
		for item in os.scandir('..'):
			if os.path.exists(item) and os.path.isdir(item) and item == "data":
				self.data: str = "../data/"
			else:
				os.mkdir("../data/")
				self.data: str = "../data/"
			if os.path.exists(item) and os.path.isdir(item) and item == "cogs":
				self.cogs: str = "../cogs/"
			else:
				os.mkdir("../cogs/")
				self.cogs: str = "../cogs/"


	