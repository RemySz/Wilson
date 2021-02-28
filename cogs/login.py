from discord.ext import commands
import discord
from data.stream import DataStructure
from cogs.__init__ import AccessLevel

class Login(commands.Cog, name="Login"):
	def __init__(self, bot):
		self.bot = bot
		self.struct = DataStructure()

	@commands.group(pass_context=True, name="login")
	async def login(self, ctx):
		if self.struct.load(ctx.author.id, additional_path_info="./data/user/") == Exception:
			print("Exception")
			self.struct.user_id = ctx.author.id
			self.struct.data = {
				"name": ctx.author.name + '#' + ctx.author.discriminator, 
				"id": ctx.author.id,
				"access_level": AccessLevel.Member,
				"active_access_level": AccessLevel.Member
			}
			print(self.struct.user_id)
			self.struct.dump()
		else:
			self.struct.load(ctx.author.id, additional_path_info="./data/user/")

		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error", value="Invoked subcommand was not found in command group context")
			await ctx.send(embed=embed)
			
	@login.command(
		pass_context=True,
		name = "developer",
		aliases = ["dev"]
	)
	async def developer(self, ctx):
		if ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Developer and int(self.struct.data["active_access_level"]) != AccessLevel.Developer:

			public_embed = discord.Embed(colour=discord.Colour.magenta())
			public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			public_embed.add_field(name="Access granted", value="You are now a developer", inline=False)

			private_embed = discord.Embed(colour=discord.Colour.magenta())
			private_embed.set_author(name="Logged in as Developer", icon_url=ctx.author.avatar_url)
			commands_string = "use \"::dev help\" to see a list of commands you have access to"
			private_embed.add_field(name="Commands",value=commands_string, inline=False)

			await ctx.send(embed=public_embed)
			user = self.bot.get_user(ctx.author.id)
			await user.send(embed=private_embed)

			self.struct.data["active_access_level"] = AccessLevel.Developer
			self.struct.dump(additional_path_info="./data/user/")
			self.struct.clear()

		elif ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Developer and int(self.struct.data["active_access_level"]) == AccessLevel.Developer:

			public_embed = discord.Embed(colour=discord.Colour.magenta())
			public_embed.set_author(name="You are already logged in as developer", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=public_embed)

	@login.command(
		pass_context=True,
		name = "owner",
	)
	async def owner(self, ctx):
		if ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Owner and int(self.struct.data["active_access_level"]) != AccessLevel.Owner:
			public_embed = discord.Embed(colour=discord.Colour.purple())
			public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			public_embed.add_field(name="Access granted", value="You are now an owner", inline=False)

			private_embed = discord.Embed(colour=discord.Colour.purple())
			private_embed.set_author(name="Logged in as Owner", icon_url=ctx.author.avatar_url)
			commands_string = "use \"::owner help\" to see a list of commands you have access to"
			private_embed.add_field(name="Commands",value=commands_string, inline=False)

			await ctx.send(embed=public_embed)
			user = self.bot.get_user(ctx.author.id)
			await user.send(embed=private_embed)

			self.struct.data["active_access_level"] = AccessLevel.Owner
			print("yo")
			self.struct.dump(additional_path_info="./data/user/")
			self.struct.clear()

		elif ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Owner and int(self.struct.data["active_access_level"]) == AccessLevel.Owner:
			print("in")
			public_embed = discord.Embed(colour=discord.Colour.purple())
			public_embed.set_author(name="You are already logged in as owner", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=public_embed)

	@login.command(
		pass_context=True,
		name = "administrator",
		aliases = ["admin"]
	)
	async def administrator(self, ctx):
		if ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Administrator and int(self.struct.data["active_access_level"]) != AccessLevel.Administrator:
			public_embed = discord.Embed(colour=discord.Colour.purple())
			public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			public_embed.add_field(name="Access granted", value="You are now an administrator", inline=False)

			private_embed = discord.Embed(colour=discord.Colour.purple())
			private_embed.set_author(name="Logged in as Administrator", icon_url=ctx.author.avatar_url)
			commands_string = "use \"::admin help\" to see a list of commands you have access to"
			private_embed.add_field(name="Commands",value=commands_string, inline=False)

			await ctx.send(embed=public_embed)
			user = self.bot.get_user(ctx.author.id)
			await user.send(embed=private_embed)

			self.struct.data["active_access_level"] = AccessLevel.Administrator
			print("yo")
			self.struct.dump(additional_path_info="./data/user/")
			self.struct.clear()

		elif ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Administrator and int(self.struct.data["active_access_level"]) == AccessLevel.Administrator:
			print("in")
			public_embed = discord.Embed(colour=discord.Colour.purple())
			public_embed.set_author(name="You are already logged in as administrator", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=public_embed)
	
	@login.command(
		pass_context=True,
		name = "moderator",
		aliases = ["mod"]
	)
	async def moderator(self, ctx):
		if ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Moderator and int(self.struct.data["active_access_level"]) != AccessLevel.Moderator:

			public_embed = discord.Embed(colour=discord.Colour.blue())
			public_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			public_embed.add_field(name="Access granted", value="You are now a moderator", inline=False)

			private_embed = discord.Embed(colour=discord.Colour.blue())
			private_embed.set_author(name="Logged in as Moderator", icon_url=ctx.author.avatar_url)
			commands_string = "use \"::mod help\" to see a list of commands you have access to"
			private_embed.add_field(name="Commands",value=commands_string, inline=False)

			await ctx.send(embed=public_embed)
			user = self.bot.get_user(ctx.author.id)
			await user.send(embed=private_embed)

			self.struct.data["active_access_level"] = AccessLevel.Moderator
			self.struct.dump(additional_path_info="./data/user/")
			self.struct.clear()

		elif ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Moderator and int(self.struct.data["active_access_level"]) == AccessLevel.Moderator:

			public_embed = discord.Embed(colour=discord.Colour.blue())
			public_embed.set_author(name="You are already logged in as moderator", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=public_embed)

	@login.command(
		pass_context=True,
		name = "member",
	)
	async def member(self, ctx):
		if ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Member and int(self.struct.data["active_access_level"]) != AccessLevel.Member:
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

			self.struct.data["active_access_level"] = AccessLevel.Member
			self.struct.dump(additional_path_info="./data/user/")
			self.struct.clear()

		elif ctx.author.id == int(self.struct.data["id"]) and int(self.struct.data["access_level"]) <= AccessLevel.Member and int(self.struct.data["active_access_level"]) == AccessLevel.Member:

			public_embed = discord.Embed(colour=discord.Colour.teal())
			public_embed.set_author(name="You are already logged in as member", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=public_embed)



def setup(bot):
	bot.add_cog(Login(bot))



