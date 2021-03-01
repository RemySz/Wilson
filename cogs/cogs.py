from discord.ext import commands
from data.stream import DataStructure
import discord

class Cog_commands(commands.Cog, name="Cog"):
	def __init__(self, bot):
		self.bot = bot
		self.stream = DataStructure()
		self.access = False

	@commands.group(
		pass_context = True,
		name="cog"
	)
	async def cog(self, ctx):
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error",value="Your command required a subcommand. None was provided.", inline=False)
			await ctx.send(embed=embed)
		else:
			self.stream.load(ctx.author.id, "./data/user/")
			if int(self.stream.data["active_access_level"]) == 0:
				self.access = True
			else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)
				self.access = False


	@cog.command(  
		name='reload',  
		aliases=['rl']  
	)  
	async def reload(self, ctx, cog):
		'''
		Reloads a cog.
		'''
		if not self.access: return
		try:
			self.bot.unload_extension(f"cogs.{cog}")
			self.bot.load_extension(f"cogs.{cog}")
			await ctx.send(f"Reloaded {cog}")
		except Exception as e:
			await ctx.send(e)

		 
	
	@cog.command(name="unload", aliases=['ul']) 
	async def unload(self, ctx, cog):
		'''
		Unload a cog.
		'''
		if not self.access: return
		try:
			self.bot.unload_extension(f"cogs.{cog}")
			await ctx.send(f"{cog} was unloaded")
		except Exception as e:
			await ctx.send(e)
		
	
	@cog.command(name="load")
	async def load(self, ctx, cog):
		'''
		Loads a cog.
		'''
		if not self.access: return
		try:
			self.bot.load_extension(f"cogs.{cog}")
			await ctx.send(f"{cog} was loaded!")
		except Exception as e:
			await ctx.send(e)

		

	@cog.command(name="list", aliases=['lc'])
	async def listcogs(self, ctx):
		'''
		Returns a list of all enabled commands.
		'''
		if not self.access: return
		string = "```php\n"
		for cog in self.bot.extensions:
			string += f"${cog}"
			string += '\n'
		string += "```"
		await ctx.send(string)



def setup(bot):
	bot.add_cog(Cog_commands(bot))

def terminate(bot):
	bot.remove_cog(Cog_commands(bot))
	