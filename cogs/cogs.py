from discord.ext import commands
from data.stream import DataStructure
from .__init__ import AccessLevel
import cogs.__init__ as cc
import discord

class Cog_commands(commands.Cog, name="Cog"):
	def __init__(self, bot):
		self.bot = bot
		self.stream = DataStructure()

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
			if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:
				pass
			else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)


	@cog.command(  
		name='reload',  
		aliases=['rl']  
	)  
	async def reload(self, ctx, cog):
		'''
		Reloads a cog.
		'''
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:
			if not self.access: return
			try:
				self.bot.unload_extension(f"cogs.{cog}")
				self.bot.load_extension(f"cogs.{cog}")
				embed = discord.Embed(colour=discord.Colour.green())
				embed.set_author(name=f"Reloaded {cog}", icon_url=ctx.author.avatar_url)
			except Exception as e:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name=f"Attempt a reloading {cog} cause the following error", icon_url=ctx.author.avatar_url)
				embed.add_field(name="Error", value=str(e))
		
		else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
		
		await ctx.send(embed=embed)

		 
	
	@cog.command(name="unload", aliases=['ul']) 
	async def unload(self, ctx, cog):
		'''
		Unload a cog.
		'''
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:
			try:
				self.bot.unload_extension(f"cogs.{cog}")
				embed = discord.Embed(colour=discord.Colour.green())
				embed.set_author(name=f"Unloaded {cog}", icon_url=ctx.author.avatar_url)
			except Exception as e:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name=f"Attempt a reloading {cog} cause the following error", icon_url=ctx.author.avatar_url)
				embed.add_field(name="Error", value=str(e))
		
		else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
		
		await ctx.send(embed=embed)
		
	
	@cog.command(name="load")
	async def load(self, ctx, cog):
		'''
		Loads a cog.
		'''
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:
			try:
				self.bot.load_extension(f"cogs.{cog}")
				embed = discord.Embed(colour=discord.Colour.green())
				embed.set_author(name=f"Loaded {cog}", icon_url=ctx.author.avatar_url)
			except Exception as e:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name=f"Attempt a reloading {cog} cause the following error", icon_url=ctx.author.avatar_url)
				embed.add_field(name="Error", value=str(e))

		else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
		
		await ctx.send(embed=embed)

		

	@cog.command(name="list", aliases=['lc'])
	async def listcogs(self, ctx):
		'''
		Returns a list of all enabled commands.
		'''
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:
			embed = discord.Embed(colour=discord.Colour.green())
			embed.set_author(name="List of Cogs", icon_url=ctx.author.avatar_url)
			string = ""
			for cog in self.bot.extensions:
				string += f"${cog}"
				string += '\n'
			embed.add_field(name="Loaded Cogs", value=string)
			with open("./config/cogs.txt",'r') as f:
				embed.add_field(name="Cogs in config", value=f.read())
			string = ""
			for cog in cc.list_of_cogs:
				string += str(cog) + "\n"
			embed.add_field(name="All cogs", value=string)
		
		else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
		
		await ctx.send(embed=embed)



def setup(bot):
	bot.add_cog(Cog_commands(bot))

def terminate(bot):
	bot.remove_cog(Cog_commands(bot))
	