import discord
from discord.ext import commands
import random

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

		self.kiss_gifs = [
			"https://media0.giphy.com/media/Ij1cbMbIWDKDK/giphy.webp?cid=ecf05e47ta3tbbxemhfrwtochg23s8yurr0t79vaqb7trrtg&rid=giphy.webp",
			"https://media0.giphy.com/media/lTQF0ODLLjhza/giphy.webp?cid=ecf05e470yk9ilr6si89o97jm7y4c2bxohlgw3sr147tnx7w&rid=giphy.webp",
			"https://media2.giphy.com/media/dpSrm4cwUmCeQ/200w.webp?cid=ecf05e470yk9ilr6si89o97jm7y4c2bxohlgw3sr147tnx7w&rid=200w.webp",
			"https://media1.giphy.com/media/10UUe8ZsLnaqwo/giphy.webp?cid=ecf05e470yk9ilr6si89o97jm7y4c2bxohlgw3sr147tnx7w&rid=giphy.webp",
			"https://media0.giphy.com/media/egjCAYphmLmrm/200.webp?cid=ecf05e47ta3tbbxemhfrwtochg23s8yurr0t79vaqb7trrtg&rid=200.webp",
			"https://media3.giphy.com/media/3o72FiXBdWRy3aZHJm/200w.webp?cid=ecf05e474v1zd0jhaznpy8zj0dn9hjsitux9fug3rc9nxjrj&rid=200w.webp",
			"https://media3.giphy.com/media/nxNwAJqEty4py/200w.webp?cid=ecf05e47p39nyu7uats6zp20o4b33s5lurrix6edduo5umbd&rid=200w.webp",
			"https://media1.giphy.com/media/3og0IvIXD1UrcEvNmw/200w.webp?cid=ecf05e47p39nyu7uats6zp20o4b33s5lurrix6edduo5umbd&rid=200w.webp",
			"https://media4.giphy.com/media/Nydo55HzhyGqI/200.webp?cid=ecf05e474a6pl1xsgvqwrt0t6echxxljlgvm1anpwnpvy257&rid=200.webp",
			"https://media4.giphy.com/media/l2Je2M4Nfrit0L7sQ/200.webp?cid=ecf05e470yk9ilr6si89o97jm7y4c2bxohlgw3sr147tnx7w&rid=200.webp"
		]

		self.fuckyou_gifs = [
			"https://media4.giphy.com/media/x1kS7NRIcIigU/giphy.webp?cid=ecf05e474qmc9dxqdxniwhgsfhd0c5uifmisui6eaitekm6x&rid=giphy.webp",
			"https://media0.giphy.com/media/yV5xcSTmtVPBS/200.webp?cid=ecf05e474qmc9dxqdxniwhgsfhd0c5uifmisui6eaitekm6x&rid=200.webp",
			"https://media1.giphy.com/media/3o7btYc0vx0tTPYVLa/200w.webp?cid=ecf05e474qmc9dxqdxniwhgsfhd0c5uifmisui6eaitekm6x&rid=200w.webp",
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