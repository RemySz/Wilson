import discord
from discord.ext import commands

bot = discord.Client()
bot = commands.Bot(command_prefix="!!", description="Wilson bot")

# Load core
core = ["tictactoe"]
for member in core:
    bot.load_extension(f"core.{member}")

# Load extenstions

try:
    with open(".token", 'r') as f:
        bot.run(f.read())
except FileNotFoundError:
    print(".token was not found")
    print("Please generate a bot token and place it inside a .token file")
    exit(1)
