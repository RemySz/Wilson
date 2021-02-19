import discord
from discord.ext import commands
import lib.math as math

class Math(commands.Cog, name="Math"):
	def __init__(self, bot):
		self.bot = bot

@commands.group(
	pass_context=True,
	aliases=["var","variant"]
)
async def variance(ctx):
	if ctx.invoked_subcommand is None:
		embed = discord.Embed(colour=discord.Colour.red())
		embed.add_field(name="Error", value="User failed to invoke subcommands!", inline=False)
		embed.add_field(name="Conclusion", value="Use \"::variance <population/sample> *args\"", inline=False)
		await ctx.send(embed=embed)


@variance.command(
	pass_context = True,
	aliases=["pop"]
)
async def population(ctx, *args):
	answer = math.calculate_variance_population(False, [int(i) for i in args])
	embed = discord.Embed(colour=discord.Colour.green())
	embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	embed.add_field(name="Variance(Answer)", value=answer["variance"], inline=False)
	embed.add_field(name="Standard Deviation", value=answer["deviation"], inline=False)
	embed.add_field(name="Mean of Terms", value=answer["mean"], inline=False)
	embed.add_field(name="Number of Terms", value=answer["length"], inline=False)
	embed.add_field(name="Sum of Terms", value=answer["sum"], inline=False)
	await ctx.send(embed=embed)

@variance.command(
	pass_context = True,
	aliases=["sam"]
)
async def sample(ctx, *args):
	answer = math.calculate_variance_sample(False, [int(i) for i in args])
	embed = discord.Embed(colour=discord.Colour.green())
	embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	embed.add_field(name="Variance(Answer)", value=answer["variance"], inline=False)
	embed.add_field(name="Standard Deviation", value=answer["deviation"], inline=False)
	embed.add_field(name="Mean of Terms", value=answer["mean"], inline=False)
	embed.add_field(name="Number of Terms", value=answer["length"], inline=False)
	embed.add_field(name="Sum of Terms", value=answer["sum"], inline=False)
	await ctx.send(embed=embed)

@commands.command(
	pass_context = True,
	aliases=[]
)
async def mean(ctx, *args):
	answer = math.calculate_mean(False, [int(i) for i in args])
	embed = discord.Embed(colour=discord.Colour.green())
	embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	embed.add_field(name="Mean(answer)", value=answer["mean"], inline=False)
	embed.add_field(name="Number of Terms", value=answer["length"], inline=False)
	embed.add_field(name="Sum of Terms", value=answer["sum"], inline=False)
	await ctx.send(embed=embed)

@commands.command(
	pass_context = True,
	aliases=["med"]
)
async def median(ctx, *args):
	answer = math.calculate_median(False, [int(i) for i in args])
	embed = discord.Embed(colour=discord.Colour.green())
	embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	embed.add_field(name="Median(answer)", value=answer["median"], inline=False)
	embed.add_field(name="Number of Terms", value=answer["length"], inline=False)
	embed.add_field(name="Middle Term", value=answer["middle"], inline=False)
	await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Math(bot))
