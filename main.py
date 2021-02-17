import os
from keep_alive import keep_alive
from discord.ext import commands
import lib.lib_math as math

bot = commands.Bot(
	command_prefix="::",  
	case_insensitive=True
)

bot.author_id = None # for now

@bot.event 
async def on_ready(): 
    print("I'm in")
    print(bot.user) 
	

@bot.command()
async def variance(ctx, *args):
	await ctx.send(math.calculate_variance_population(i for i in args))
	
	

		


	
	



extensions = [
	"cogs.cog_dev"
]

if __name__ == '__main__':  
	for extension in extensions:
		bot.load_extension(extension)

keep_alive()  
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  