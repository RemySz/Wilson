import discord

class Event(commands.Cog, name="Event"):
	def __init__(self, bot):
		self.bot = bot



def setup(bot):
	bot.add_cogs(Event(bot))
	
def teardown(bot):
	pass
