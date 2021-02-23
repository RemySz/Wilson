from discord.ext import commands
import discord


users = {
	"users": {
		"remy": {
			"id": 739134752824754317,
			"name": "Соковий демон#5619",
			"access_level": 0,
			"active_access_level": 0
		}
	}
}

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

	@login.command(
		pass_context=True,
		name = "administrator",
		aliases = ["admin"]
	)
	async def administrator(self, ctx):
		for user, info in users["users"].items():
			if ctx.author.id == info["id"] and info["access_level"] <= 1 and info["active_access_level"] != 1:

				public_embed = discord.Embed(colour=discord.Colour.purple())
				public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
				public_embed.add_field(name="Access granted", value="You are now an administrator", inline=False)

				private_embed = discord.Embed(colour=discord.Colour.purple())
				private_embed.set_author(name="Logged in as Administrator", icon_url=ctx.author.avatar_url)
				commands_string = "use \"::admin --help\" to see a list of commands you have access to"
				private_embed.add_field(name="Commands",value=commands_string, inline=False)

				await ctx.send(embed=public_embed)
				user = self.bot.get_user(ctx.author.id)
				await user.send(embed=private_embed)

			elif ctx.author.id == info["id"] and info["access_level"] <= 1 and info["active_access_level"] == 1:

				public_embed = discord.Embed(colour=discord.Colour.purple())
				public_embed.set_author(name="You are already logged in as administrator", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=public_embed)
			
	@login.command(
		pass_context=True,
		name = "developer",
		aliases = ["dev"]
	)
	async def developer(self, ctx):
		for user, info in users["users"].items():
			if ctx.author.id == info["id"] and info["access_level"] <= 0 and info["active_access_level"] != 0:

				public_embed = discord.Embed(colour=discord.Colour.magenta())
				public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
				public_embed.add_field(name="Access granted", value="You are now a developer", inline=False)

				private_embed = discord.Embed(colour=discord.Colour.magenta())
				private_embed.set_author(name="Logged in as Developer", icon_url=ctx.author.avatar_url)
				commands_string = "use \"::dev --help\" to see a list of commands you have access to"
				private_embed.add_field(name="Commands",value=commands_string, inline=False)

				await ctx.send(embed=public_embed)
				user = self.bot.get_user(ctx.author.id)
				await user.send(embed=private_embed)

			elif ctx.author.id == info["id"] and info["access_level"] <= 0 and info["active_access_level"] == 0:

				public_embed = discord.Embed(colour=discord.Colour.magenta())
				public_embed.set_author(name="You are already logged in as developer", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=public_embed)
	
	@login.command(
		pass_context=True,
		name = "moderator",
		aliases = ["mod"]
	)
	async def moderator(self, ctx):
		for user, info in users["users"].items():
			if ctx.author.id == info["id"] and info["access_level"] <= 2 and info["active_access_level"] != 2:

				public_embed = discord.Embed(colour=discord.Colour.blue())
				public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
				public_embed.add_field(name="Access granted", value="You are now a moderator", inline=False)

				private_embed = discord.Embed(colour=discord.Colour.blue())
				private_embed.set_author(name="Logged in as Moderator", icon_url=ctx.author.avatar_url)
				commands_string = "use \"::mod --help\" to see a list of commands you have access to"
				private_embed.add_field(name="Commands",value=commands_string, inline=False)

				await ctx.send(embed=public_embed)
				user = self.bot.get_user(ctx.author.id)
				await user.send(embed=private_embed)

			elif ctx.author.id == info["id"] and info["access_level"] <= 2 and info["active_access_level"] == 2:

				public_embed = discord.Embed(colour=discord.Colour.blue())
				public_embed.set_author(name="You are already logged in as moderator", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=public_embed)

	@login.command(
		pass_context=True,
		name = "member",
	)
	async def member(self, ctx):
		for user, info in users["users"].items():
			if ctx.author.id == info["id"] and info["access_level"] <= 3 and info["active_access_level"] != 3:

				public_embed = discord.Embed(colour=discord.Colour.teal())
				public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
				public_embed.add_field(name="Access granted", value="You are now a member", inline=False)

				private_embed = discord.Embed(colour=discord.Colour.teal())
				private_embed.set_author(name="Logged in as Member", icon_url=ctx.author.avatar_url)
				commands_string = "use \"::help\" to see a list of commands you have access to"
				private_embed.add_field(name="Commands",value=commands_string, inline=False)

				await ctx.send(embed=public_embed)
				user = self.bot.get_user(ctx.author.id)
				await user.send(embed=private_embed)

			elif ctx.author.id == info["id"] and info["access_level"] <= 3 and info["active_access_level"] == 3:

				public_embed = discord.Embed(colour=discord.Colour.teal())
				public_embed.set_author(name="You are already logged in as member", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=public_embed)


def setup(bot):
    bot.add_cog(Login(bot))		


