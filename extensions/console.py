from discord.ext import commands
from __init__ import AccessLevel
from lib.check import correct_access_level

class Console(commands.Cog, name="console"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.group(
		pass_context=True,
		name = "console",
		aliases = []
	)
	async def console(self, ctx):
		if not correct_access_level(AccessLevel.Administrator, ctx.author.id):
			return ''
		if ctx.invoked_subcommand is None:
			# Error
			pass
	
	@console.command(
		pass_context = True,
		name = "initialise",
		aliases = ["init"]
	) 
	async def initialise(self, ctx, *flags):
		# initialise channel as a channel console
		# interprete flags using a lib
		pass

	@console.group(
		pass_context = True,
		name = "setting",
		aliases = ["settings"]
	) 
	async def setting(self, ctx):
		if ctx.invoked_subcommand is None:
			# EnvironmentError
			pass

	@setting.command(
		pass_context = True,
		name = "add_setting",
		aliases = ["add"]
	)
	async def add_setting(self, ctx, new_setting, value):
		pass

	@setting.command(
		pass_context = True,
		name = "remove_setting",
		aliases = ["remove"]
	)
	async def remove_setting(self, ctx, setting):
		pass
	
	@setting.command(
		pass_context = True,
		name = "manipulate_seting",
		aliases = ["change", "alter", "manipulate", "mani"]
	)
	async def manipulate_setting(self, ctx, new_setting, new_value):
		pass

	@setting.command(
		pass_context = True,
		name = "checkout_setting",
		aliases = ["checkout", "switch"]
	)
	async def checkout_setting(self, ctx, setting):
		pass

def setup(bot):
	bot.add_cog(Console(bot))

def terminate(bot):
	bot.remove_cog(Console(bot))
	

	
