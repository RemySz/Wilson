import discord
from discord.ext import commands
from data.stream import DataStructure

class Event(commands.Cog, name="Events"):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, ctx):
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
	async def on_message(self, message: discord.Member):
		if message.author.name == self.bot.user.name:
			return 
    # do some extra stuff here
		if "--remove" in message.content:
			await message.delete()
			# remove message
			
		elif "--say" in message.content:
			await message.channel.send(message.content.replace("--say",''))
			# make wilson say message contents

		#elif "--quote" in message.content or "--q" in message.content:
			#await message.channel.send(f"\"{message.content.replace("--quote",'')}\" - {message.author.name}")

		await self.bot.process_commands(message)
	
	@commands.Cog.listener()
	async def on_guild_join(self, ctx):
		"""
		Generate a guild data set:
			Guild name, guild id, owner
		"""
		pass
	




def setup(bot):
	bot.add_cog(Event(bot))
	
def teardown(bot):
	pass
