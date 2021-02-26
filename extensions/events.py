import discord
from discord.ext import tasks, commands
from data.stream import DataStructure

class Event(commands.Cog, name="Event"):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, ctx: discord.Context):
		embed = discord.Embed(colour=discord.Colour.gold())
		embed.set_author(name=f"Welcome! {ctx.author.name}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
		data = {
			"name": ctx.author.name,
			"id": ctx.author.id,
			"access_level": 3,
			"active_access_level": 3
		}
		stream = DataStructure()
		stream.data = data
		stream.dump()
		del stream

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		embed = discord.Embed(colour=discord.Colour.gold())
		embed.set_author(name="Goodbye & Good luck!", icon_url=member.avatar_url)
		await member.send(embed=embed)
		stream = DataStructure()
		stream.delete()
		del stream
	
	@command.Cog.listener()
	async def on_guild_join(self, ctx):
		pass
	
	@command.Cog.listener()
	async def on_guild_remove(self, ctx):
		pass



def setup(bot):
	bot.add_cogs(Event(bot))
	
def teardown(bot):
	pass
