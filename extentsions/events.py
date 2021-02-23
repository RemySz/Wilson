import discord
from discord.ext import tasks, commands

class Event(commands.Cog, name="Event"):
	def __init__(self, bot):
		self.bot = bot


def setup(bot):
    bot.add_cog(Event(bot))


def teardown(bot):
	pass
