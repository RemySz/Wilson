from discord.ext import commands

class Dev(commands.Cog, name="Dev"):
	def __init__(self, bot):
		self.bot = bot

	@commands.group()
	async def cog(self, ctx):
		if ctx.invoked_subcommand is None:
			pass
	
	@cog.command()
	async def add_cog(self, ctx):
		pass

	@cog.command()
	async def remove_cog(self, ctx):
		pass

	@cog.command()
	async def unload_cog(self, ctx):
		pass

	@cog.command()
	async def load_cog(self, ctx):
		pass

def setup(bot):
	bot.add_cog(Dev(bot))

def terminate(bot):
	pass
	