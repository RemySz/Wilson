import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="::",
    case_insensitive=True,
    intents=intents
)

@bot.event
async def on_ready():
    print(bot.user)
    print("Readying up")

extensions = [
    "cogs.games"
]

if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)
        print(f"Loaded {extension}")

_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(_TOKEN)