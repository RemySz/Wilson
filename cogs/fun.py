import discord
from discord.ext import commands
import random

# TODO 
# Web scrap giphy instead of using pre found gifs

class Fun(commands.Cog, name="Fun!"):
	def __init__(self, bot):
		self.bot = bot
		self.kill_gifs = [
			"https://media0.giphy.com/media/yNFjQR6zKOGmk/giphy.gif?cid=ecf05e47iawezg7dah6p1ttfe21vpx7egfh7qa6perxagvov&rid=giphy.gif",
			"https://media3.giphy.com/media/PnhOSPReBR4F5NT5so/giphy.gif",
			"https://media4.giphy.com/media/12zQQNVooHEIGQ/giphy.gif",
			"https://media2.giphy.com/media/uTCAwWNtz7U2c/giphy.gif",
			"https://media4.giphy.com/media/12zQQNVooHEIGQ/giphy.gif",
			"https://media1.giphy.com/media/3orif0HPtMKPs8su6Q/giphy.gif",
			"https://media4.giphy.com/media/QRnpmCPP8z7JS/giphy.gif",
			"https://media3.giphy.com/media/9tXn7DEOsjifNDEenF/giphy.gif",
			"https://media3.giphy.com/media/HCK2ro8NtZX1e/giphy.gif?cid=ecf05e47qy8ti18wks2xug5edomdvi60h5cjbex7koduav6e&rid=giphy.gif"
		]
	
	@commands.command() 
	async def quote(self, ctx, message, author):
		await ctx.send(f"\"{message}\" - {author}")

	@commands.command()
	async def kill(self, ctx, member: discord.Member):
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name=f"{ctx.author.name} killed {member.name}", icon_url=ctx.author.avatar_url)
		embed.set_image(url=random.choice(self.kill_gifs))
		await ctx.send(embed=embed)
	
	@commands.command()
	async def kiss(self, ctx, member: discord.Member):
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name=f"{ctx.author.name} kissed {member.name}", icon_url=ctx.author.avatar_url)
		embed.set_image(url=random.choice(self.kiss_gifs))
		await ctx.send(embed=embed)

	@commands.command()
	async def fuckyou(self, ctx, member: discord.Member):
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name=f"{ctx.author.name} fucks up {member.name}", icon_url=ctx.author.avatar_url)
		embed.set_image(url=random.choice(self.fuckyou_gifs))
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Fun(bot))