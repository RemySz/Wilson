from datetime import datetime

class Terminal:
	"""
		Interact with discord bot from Console (server side)
		Includes logging.
	"""
	def __init__(self):
		self.time = datetime.now("GMT-0")
		self.istream: str
		self.ostream: str
		self.terminal_should_close = False
	
	def get_input(self):
		"""
			Gets input
		"""
		self.istream = input(">> ")

	def interprete(self):
		"""
			Interpretes input (istream) and executes command
		"""
		output = f"{self.time} :: "
		if self.istream == "shutdown":
			print("Shutting down")
			self.terminal_should_close = True
		elif self.istream.startswith("echo"):
			output += self.istream.split(" ", maxsplit=1)[1]

		self.ostream = output
		return 0


def main():
	console = Terminal()
	while(not console.terminal_should_close):
		console.get_input()
		console.interprete()
		print(console.ostream)
	
	del console
