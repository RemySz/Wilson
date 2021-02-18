import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import lib.math as math

bot = commands.Bot(
	command_prefix="::",  
	case_insensitive=True
)

bot.author_id = None # for now

@bot.event 
async def on_ready(): 
    print("I'm in")
    print(bot.user) 
	
@bot.group(pass_context=True)
async def variance(ctx):
	if ctx.invoked_subcommand is None:
		embed = discord.Embed(colour=discord.Colour.red())
		embed.add_field(name="Error", value="User failed to invoke subcommands!", inline=False)
		embed.add_field(name="Conclusion", value="Use \"::variance <population/sample> *args\"", inline=False)
		await ctx.send(embed=embed)


@variance.command()
async def population(ctx, *args):
	answer = math.calculate_variance_population_raw(False, [int(i) for i in args])
	embed = discord.Embed(colour=discord.Colour.green())
	embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	embed.add_field(name="Variance(Answer)", value=answer["answer"], inline=False)
	embed.add_field(name="Mean of Terms", value=answer["mean"], inline=False)
	embed.add_field(name="Number of Terms", value=answer["n"], inline=False)
	embed.add_field(name="Sum of Terms", value=answer["sum"], inline=False)
	await ctx.send(embed=embed)

@variance.command()
async def sample(ctx, *args):
	answer = math.calculate_variance_sample_raw(False, [int(i) for i in args])
	embed = discord.Embed(colour=discord.Colour.green())
	embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	embed.add_field(name="Variance(Answer)", value=answer["answer"], inline=False)
	embed.add_field(name="Mean of Terms", value=answer["mean"], inline=False)
	embed.add_field(name="Number of Terms", value=answer["n"], inline=False)
	embed.add_field(name="Sum of Terms", value=answer["sum"], inline=False)
	await ctx.send(embed=embed)
	
	

		


	
	



extensions = [
	"cogs.cog_dev"
]

if __name__ == '__main__':  
	for extension in extensions:
		bot.load_extension(extension)

keep_alive()  
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  