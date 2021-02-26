from discord.ext import commands, tasks

class Console(commands.Cog, name="console"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.group()
	async def console(self, ctx):
		if ctx.invoked_subcommand is None:
			# Error
			pass
	
	@console.command() 
	async def initialise(self, ctx, *flags):
		# initialise channel as a channel console
		# interprete flags using a lib
		pass

	@console.group() 
	async def setting(self, ctx):
		if ctx.invoked_subcommand is None:
			# EnvironmentError
			pass

	@setting.group() 
	async def add_setting(self, ctx, new_setting, value):
		pass

	@setting.group() 
	async def remove_setting(self, ctx, setting):
		pass
	
	@setting.group() 
	async def manipulate_setting(self, ctx, new_setting, new_value):
		pass

	@setting.group() 
	async def checkout_setting(self, ctx, setting):
		pass

def setup(bot):
	bot.add_cog(Console(bot))

def terminate(bot):
	pass
	

	
