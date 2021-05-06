from discord.ext import commands
from data.stream import DataStructure
import discord
from .__init__ import AccessLevel

class Dev(commands.Cog, name="Developer Commands"):
	def __init__(self, bot):
		self.bot = bot
		self.stream = DataStructure()

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
			try:
				self.stream.load(ctx.author.id, "./data/user/")
			except: 
				self.stream.data = {
				"name": ctx.author.name + '#' + ctx.author.discriminator,
				"id": ctx.author.id,
				"access_level": 4, "active_access_level": 4
				}
				self.stream.dump("./data/user/")

			if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:
				pass
			else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)
				return

	@dev.command()
	async def load(self, ctx, extension):
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:

			try:
				with open("./config/cogs.txt",'a') as f:
					f.write(f"cogs.{extension}\n")
					self.bot.load_extension("cogs." + extension)
					embed = discord.Embed(colour=discord.Colour.purple())
					embed.set_author(name=f"{extension} was loaded!", icon_url=ctx.author.avatar_url)
					embed.add_field(
						name=f"Succesfully loaded {extension}!",
						value="Extension was loaded with success. This will now load upon restart automatically and be stored in config.cogs.", 
						inline=False
					)
				self.stream.clear()

			except Exception as e:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name=f"Error while unloading {extension}", icon_url=ctx.author.avatar_url)
				embed.add_field(name="Error!", value=str(e), inline=False)
		
		else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
		
		await ctx.send(embed=embed)

	@dev.command()
	async def unload(self, ctx, extension):
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:
			
			embed = discord.Embed(colour=discord.Colour.blurple())
			embed.set_author(name=f"Unloaded {extension}", icon_url=ctx.author.avatar_url)
			embed.add_field(
				name=f"Succesfully unloaded {extension}!",
				value="Extension was unloaded with success. Extension has been removed from config.cogs and will not long automatically boot on restart.", 
				inline=False
			)

			with open("./config/cogs.txt", 'r') as f:
				contents = f.readlines()

				try:
					self.bot.unload_extension("cogs." + extension)
					contents.remove("cogs."+extension+"\n")
					with open("./config/cogs.txt",'w') as f:
						f.writelines(contents)
				except Exception as e:
					del embed
					embed = discord.Embed(colour=discord.Colour.red())
					embed.set_author(name=f"Error while unloading {extension}", icon_url=ctx.author.avatar_url)
					embed.add_field(name="Error!", value=str(e), inline=False)
			
		else:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)

		await ctx.send(embed=embed)

	@dev.command()
	async def log(self, ctx, user_id):
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:

			user = self.bot.get_user(user_id)
			self.stream.data = {
				"name": user.name + '#' + user.discriminator,
				"id": user.id,
				"access_level": 4, "active_access_level": 4
			}
			self.stream.dump(additional_path_info="./data/user/")
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name="Logged new user!", icon_url=ctx.author.avatar_url)
			embed.add_field(
				name=f"Logged {user.name}'",
				value="Only name, and id are logged. These are publicly available anyway.",
				inline=True
			)
			self.stream.clear()

		
		else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
	
	@dev.command()
	async def override(self, ctx, user_id, new_access_level):
		if int(self.stream.data["active_access_level"]) == AccessLevel.Developer:

			try:
				self.stream.load(user_id, "./data/user/")
				old_access_level = self.stream.data["access_level"]
				self.stream.data["access_level"] = new_access_level
				self.stream.dump("./data/user/")
				embed = discord.Embed(colour=discord.Colour.blue())
				embed.set_author(name="Override complete!", icon_url=ctx.author.avatar_url)
				embed.add_field(
					name=f"Over written {ctx.author.name}'s access_level!'",
					value=f"{ctx.author.name}'s access_level was over wriiten from {old_access_level} to {new_access_level}!",
					inline=True
				)
				del old_access_level

			except Exception as e:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="An attempt was made to override but it caused an error", icon_url=ctx.author.avatar_url)
				embed.add_field(name="Error", value=str(e))

			finally:
				self.stream.clear()
		
		else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
			
		await ctx.send(f"{self.stream.data['name']}'s access_level was overridden to {new_access_level}!")
		




	

def setup(bot):
	bot.add_cog(Dev(bot))