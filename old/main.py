import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
from cogs.__init__ import AccessLevel
from data.stream import DataStructure

intents = discord.Intents.all()
bot = commands.Bot(
	command_prefix="::",  
	case_insensitive=True,
	intents=intents
)

bot.author_id = None # for now

@bot.event 
async def on_ready():
	stream = DataStructure()
	print("I'm in")
	print(bot.user)
	"""for guild in bot.guilds: 
		for member in guild.members:
			struct_data = {
				"name": member.name + '#' + member.discriminator, 
				"id": member.id,
				"access_level": AccessLevel.Member,
				"active_access_level": AccessLevel.Member,
				"pokemon": {}
			}
			stream.clear() 
			if stream.load(member.id, "data/user/") != Exception:
				pass
			stream.data = struct_data 
			stream.user_id = member.id
			stream.dump("data/user/")
			print(f"LOGGED {member.id}")"""

	del stream

try:
	with open("./config/cogs.txt",'r') as f:
		cogs_config = f.readlines()
except Exception as e:
	raise e

extensions = [line.replace('\n','') for line in cogs_config]

if __name__ == '__main__':
	i = 0
	for extension in extensions:
		bot.load_extension(extension)
		i += 1
		print(f"Loaded {extension}: Total cogs loaded: {i}")
	del i
	print("Loaded all cogs in config")

keep_alive()  
token = os.environ.get("DISCORD_BOT_SECRET") 
#Thread.start_new_thread(terminal.main)
bot.run(token)   
try:
	os.remove("./__pycache__")
	os.remove("./data/__pycache__")
	os.remove("./cogs/__pycahce__")
except: pass