import discord
from discord.ext import commands
from data.stream import DataStructure
import os

class Console(commands.Cog, name="console"):
	def __init__(self, bot):
		self.bot = bot
		self.stream = DataStructure()
		self.access = False
	
	@commands.group(
		name="console",
		pass_context=True,
		aliases=["terminal"]
	)
	async def console(self, ctx):
		"""
		Edit guild configs, user configs, bot configs, cog configs, recieve command errors, etc
		"""
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error",value="Your command required a subcommand. None was provided.", inline=False)
			await ctx.send(embed=embed)

		elif self.stream.load(ctx.author.id, "./data/user/") != Exception:
			if not (self.stream.data["active_access_level"] <= 2):
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)
				self.access = False

	@console.group(
		pass_context = True
	)
	async def config(self, ctx):
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error",value="Your command required a subcommand. None was provided.", inline=False)
			await ctx.send(embed=embed)
	
	@config.command()
	async def read(self, ctx, config):
		string = "```css\n"
		try:
			with open(f"./config/{config}.txt", 'r') as f:
				string += f"Contents of {config}:\n"
				string += f.read()
				string += "\n```"
		except:
			string += f"{config} could not be found.\n"
			string += "```"
		await ctx.send(string)
			
	
	@config.command()
	async def list_configs(self, ctx):
		configs = os.scandir("./config/")
		embed = discord.Embed(colour=discord.Colour.green())
		embed.set_author(name="Global configs")
		string = ""
		for config in configs:
			config = config.replace(".txt",'').replace("\n", '')
			string += config
			string += "\n"
		embed.add_field(name="Configs found", value=string, inline=False)
		embed.add_field(name="Num of configs", value=len(configs), inline=False)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Console(bot))

