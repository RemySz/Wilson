from discord.ext import commands
from data.stream import DataStructure
import discord, os

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
	async def reload(self, ctx, *cog):
		'''
		Reloads a cog.
		'''
		if not self.access: return
		extensions = self.bot.extensions  
		embed = discord.Embed(colour=discord.Colour.blurple())
		embed.set_author(name="Reloaded extension(s)!", icon_url=ctx.author.avatar_url)

		if 'all' in cog or '*' in cog:  
			for extension in extensions:
				try:
					self.bot.unload_extension(cog)
					self.bot.load_extension(cog)
					embed.add_field(name=extension, value="was successfully unloaded!", inline=False)
				except commands.errors.ExtensionNotLoaded:
					embed.add_field(name=cog, value="Exception raised. Extension could not be loaded!", inline=False)
			await ctx.send(embed=embed) 

		else:
			for item in cog:
				if item in self.bot.extensions:
					self.bot.unload_extension(cog) 
					self.bot.load_extension(cog)  
					embed.add_field(name=item, value="was successfully unloaded!", inline=False)
				else:
					embed.add_field(name=extension, value="does not exist!", inline=False)

			await ctx.send(embed=embed) 
	
	@cog.command(name="unload", aliases=['ul']) 
	async def unload(self, ctx, *cog):
		'''
		Unload a cog.
		'''
		print(cog)
		if not self.access: return
		embed = discord.Embed(colour=discord.Colour.blurple())
		embed.set_author(name="Unloaded extension(s)!", icon_url=ctx.author.avatar_url)
		extensions = self.bot.extensions
		for item in cog:
			print(item)
			if item not in extensions:
				embed.add_field(name=cog, value="does not exist or is not currently loaded!", inline=False)
			else:
				try:
					self.bot.unload_extension(cog)
					embed.add_field(name=cog, value="was successfully unloaded!", inline=False)
				except commands.errors.ExtensionNotLoaded:
					embed.add_field(name=cog, value="Exception raised. Extension found in loaded extensions but is not loaded.", inline=False)
		await ctx.send(embed=embed)
	
	@cog.command(name="load")
	async def load(self, ctx, *cog):
		'''
		Loads a cog.
		'''
		if not self.access: return
		embed = discord.Embed(colour=discord.Colour.blurple())
		embed.set_author(name="Loaded extension(s)!", icon_url=ctx.author.avatar_url)
		for item in cog:
			try:
				self.bot.load_extension(item)
				embed.add_field(name=item, value="was loaded!", inline=False)

			except commands.errors.ExtensionNotFound:
				embed.add_field(name=item, value="was not loaded!", inline=False)
		await ctx.send(embed=embed)

	@cog.command(name="listcogs", aliases=['lc'])
	async def listcogs(self, ctx):
		if not self.access: return
		'''
		Returns a list of all enabled commands.
		'''
		embed = discord.Embed(colour=discord.Colour.blurple())
		embed.set_author(name="Extensions(s)!", icon_url=ctx.author.avatar_url)
		string: str = ""
		for cog in self.bot.extensions:
			string += cog
			string += '\n'
		embed.add_field(name="Extensions found:", value=string, inline=False)
		await ctx.send(embed=embed)

class Dev(commands.Cog, name="Developer Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.group(
		name="dev",
		pass_context=True
	)
	async def dev(self, ctx):
		"""
		Run developer only commands.
		"""
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
	
	@dev.command(
		pass_context = True,
		name = "list",
		alisases=["list"]
	) 
	async def list_extensions(self, ctx):
		string = "```css\n"
		files = os.scandir("./extensions")
		string += "Extensions found:\n"
		string += files
		string += "\n```"
		await ctx.send(string)



def setup(bot):
	bot.add_cog(Dev(bot))
	bot.add_cog(Cog_commands(bot))

def terminate(bot):
	bot.remove_cog(Dev(bot))
	bot.remove_cog(Cog_commands(bot))
	