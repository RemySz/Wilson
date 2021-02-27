import discord
from discord.ext import commands

class Help(commands.Cog, name="Help"):
	def __init__(self, bot):
		self.bot = bot
		with open("./config/help.txt", 'r') as f:
			self.lines = f.readlines()
			for line in self.lines:
				if line.startswith("#"):
					self.lines.remove(line)

	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(colour=discord.Colour.orange())
		embed.set_author(name="Help menu", icon_url="https://cdn3.iconfinder.com/data/icons/tiny-weather-1/512/sun-256.png")
		embed.add_field(name="::help", value="Shows this message!", inline=False)
		embed.add_field(name="::poll \"Poll name\" \"Poll item\"", value="Create polls for your server to vote on! Maximum of 9 poll items!", inline=False)
		embed.add_field(name="::login dev/admin/mod/member", value="Allows users to switch their access level and use bot secrets O_O (WIP)", inline=False)
		await ctx.send(embed=embed)
		

def setup(bot):
	bot.remove_command('help')
	bot.add_cog(Help(bot))