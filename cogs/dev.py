from discord.ext import commands
import discord, os

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
		files = os.scandir("./cogs/")
		string += "Cogs found:\n"
		string += files
		string += "\n```"
		await ctx.send(string)

def setup(bot):
	bot.add_cog(Dev(bot))