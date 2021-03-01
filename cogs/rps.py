import discord 
from discord.ext import commands
import random as r

class RockPaperScissors(commands.Cog, name="Rock Paper Scissors"):
	def __init__(self, bot):
		self.bot = bot
		self.raw_emojis = ["rock","paper","scissors"]
		self.emojis = ["🪨","📄","✂️","❌"]
				
	@commands.group(pass_context = True, name="Rock Paper Scissors", aliases=["rps"])
	async def rock_paper_scissor(self, ctx):
		if ctx.invoked_subcommand is None:
			error = discord.Embed(colour=discord.Colour.red())
			error.set_author(name="Error!", icon_url=ctx.author.avatar_url)
			error.add_field(
				name = "Failed to invoke subcommand", 
				value="The command you used requires the subcommand 'challenge'"
				)
			await ctx.send(embed=error)
	
	@rock_paper_scissor.command()
	async def wilson(self, ctx, user_choice):
		user_choice = user_choice.lower()
		bot_choice = r.choice(self.raw_emojis)
		embed = discord.Embed(colour=discord.Colour.blue())
		result: int
		if user_choice in self.raw_emojis:
			if user_choice == bot_choice:
				result = 2

			if user_choice == "rock":
				if bot_choice == "paper":
					result = 1
				elif bot_choice == "scissors":
					result = 3

			elif user_choice == "paper":
				if bot_choice == "rock":
					result = 1
				elif bot_choice == "scissors":
					result = 3

			elif user_choice == "scissors":
				if bot_choice == "rock":
					result = 1
				elif bot_choice == "paper":
					result = 3
			else:
				embed.set_author(name=f"{user_choice} is not an option!", icon_url=ctx.author.avatar_url)
		
		if result == 2:
			embed.set_author(name="It's a DRAW!", icon_url=ctx.author.avatar_url)
			embed.add_field(name=f"{ctx.author.name} played {user_choice}!", value=f"This caused {ctx.author.name} to draw with Wilson.", inline=False)
			embed.add_field(name=f"Wilson played {bot_choice}!", value=f"This caused Wilson to draw with {ctx.author.name}.", inline=False)
		elif result == 1:
			embed.set_author(name=f"{ctx.author.name} lost!", icon_url=ctx.author.avatar_url)
			embed.add_field(name=f"{ctx.author.name} played {user_choice}!", value=f"This caused {ctx.author.name} to lose against Wilson.", inline=False)
			embed.add_field(name=f"Wilson played {bot_choice}!", value=f"This caused Wilson to win against {ctx.author.name}.", inline=False)
		elif result == 3:
			embed.set_author(name=f"{ctx.author.name} won!", icon_url=ctx.author.avatar_url)
			embed.add_field(name=f"{ctx.author.name} played {user_choice}!", value=f"This caused {ctx.author.name} to win against Wilson.", inline=False)
			embed.add_field(name=f"Wilson played {bot_choice}!", value=f"This caused Wilson to lose against {ctx.author.name}.", inline=False)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(RockPaperScissors(bot))