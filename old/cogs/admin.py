import discord 
from discord.ext import commands 
from data.stream import DataStructure

class Admin(commands.Cog, name="Admin Commands"):
	def __init__(self, bot):
		self.bot = bot
		self.stream = DataStructure()

	@commands.group(
		name="admin",
		pass_context=True
	)
	async def admin(self, ctx):
		"""
		Run admin only commands.
			Guild config, custom admin commands, etc
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
				return
		
	@admin.command()
	async def kick(self, ctx, member: discord.Member, reason=""):
		try:
			await member.kick(reason=reason)
		except Exception:
			await ctx.send("Couldn't find user!")

	@admin.command()
	async def ban(self, ctx, member: discord.Member, reason=""):
		try:
			await member.ban(reason=reason)
		except Exception:
			await ctx.send("Couldn't find user!")
	
	@admin.command()
	async def mass_kick(self, ctx, *members: discord.Member):
		for member in members:
			member.kick()
	
	@admin.command()
	async def mass_ban(self, ctx, *members: discord.Member):
		for member in members:
			member.kick()

	@admin.command()
	async def mute(self, ctx, member: discord.Member):
		# Add role which removes permissiosn to talk in channels
		pass
		

def setup(bot):
	bot.add_cog(Admin(bot))