from discord.ext import tasks, commands
import discord
import json

class Data(object):
	with open("../data/users.json", "r") as file:
		users = json.load(file.read())

class Login(commands.Cog, name="Login"):
	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True, name="login")
	async def login(self, ctx):
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error", value="Invoked subcommand was not found in command gorup context")
			await ctx.send(embed=embed)

	@login.command(pass_context=True)
	async def admin(self, ctx):
		for user in Data.users["Users"]:
			if ctx.author.id == user["id"] and user["access_level"] >= 1 and user["active_access_level"] != 1:

				public_embed = discord.Embed(colour=discord.Colour.purple())
				public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
				public_embed.add_field(name="Access granted", inline=False)

				private_embed = discord.Embed(colour=discord.Colour.purple())
				private_embed.set_author(name="Logged in as Administrator", icon_url="../assets/key_icon.png")
				commands_string = "use \"admin --help\" to see a list of commands you have access to"
				private_embed.add_field(name="Commands",value=commands_string, inline=False)

				await ctx.send(embed=public_embed)
				await self.bot.send_message(embed=private_embed)
			elif ctx.author.id == user["id"] and user["access_level"] >= 1 and user["active_access_level"] == 1:
				public_embed = discord.Embed(colour=discord.Colour.purple())
				public_embed.set_author(name="You are already logged in as administrator", icon_url=ctx.author.avatar_url, inline=False)
				await ctx.send(embed=public_embed)

def setup(bot):
    bot.add_cog(Login(bot))		


