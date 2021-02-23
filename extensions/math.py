import discord
from discord.ext import commands

class Math(commands.Cog, name="Math"):
	def __init__(self, bot):
		self.bot = bot

class Calculate(commands.Cogs, name="Calculate"):
	def __init__(self, bot):
		self.bot = bot


def setup(bot):
  bot.add_cog(Math(bot))
	bot.add_cog(Calculate(bot))
