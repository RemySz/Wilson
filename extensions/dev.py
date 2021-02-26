from discord.ext import commands
import discord
from lib.check import correct_access_level
from __init__ import AccessLevel

class Dev(commands.Cog, name="Dev"):
	def __init__(self, bot):
		self.bot = bot

	@commands.group(
		pass_context=True,
		name = "cog",
		aliases = []
	)
	async def cog(self, ctx):
		if not correct_access_level(AccessLevel.Developer, ctx.author.id): return ''
		if ctx.invoked_subcommand is None:
			pass
	
	@cog.command(
		pass_context=True,
		name = "add_cog",
		aliases = ["add"]
	)
	async def add_cog(self, ctx):
		pass

	@cog.command(
		pass_context=True,
		name = "remove_cog",
		aliases = ["remove", "rm"]
	)
	async def remove_cog(self, ctx):
		pass

	@cog.command(
		pass_context=True,
		name = "unload_cog",
		aliases = ["unload"]
	)
	async def unload_cog(self, ctx):
		pass

	@cog.command(
		pass_context=True,
		name = "load_cog",
		aliases = ["load", "include"]
	)
	async def load_cog(self, ctx):
		pass

	@commands.group(
		pass_context=True,
		name = "connection",
		aliases = ["connection"]
	)
	async def connection(self, ctx):
		if not correct_access_level(AccessLevel.Developer, ctx.author.id): return ''
		if ctx.invoked_subcommand is None:
			# Error, 
			pass 
	
	@connection.command(
		pass_context=True,
		name="close_connection",
		aliases = ["disconnect","close"]
	)
	async def close_connection(self, ctx):
		embed = discord.Embed(colour=discord.Colour.dark_purple())
		embed.set_author(name="Bot connection closed", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
		await self.bot.close()

	


def setup(bot):
	bot.add_cog(Dev(bot))

def terminate(bot):
	bot.remove_cog(Dev(bot))

	