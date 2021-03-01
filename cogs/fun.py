import discord
from discord.ext import commands

class Fun(commands.Cog, name="Fun!"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command() 
	async def quote(self, ctx, message, author):
		await ctx.send(f"\"{message}\" - {author}")

def setup(bot):
	bot.add_cog(Fun(bot))