import discord 
from discord.ext import commands

class RockPaperScissors(commands.Cog, name="Rock Paper Scissors"):
	def __init__(self, bot):
		self.bot = bot
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
				
	@rock_paper_scissor.command(
		pass_context = True,
		aliases=["fight"],
		name="challenge"
	)
	async def challenge(self, ctx, user):
		challenger = self.bot.get_user(ctx.author.id)
		reciever = self.bot.get_user(user)
		embed = discord.Embed(colour=discord.Colour.yellow())
		embed.set_author(name="Rock! Paper! Scissors!", icon_url=ctx.author.avatar_url)
		embed.add_field(
			name=f"{ctx.author.name} challenged you to rock paper scissors!",
			value="Respond with 'rock', 'paper' or 'scissors'! You can also submit 'decline' to decline the match."
		)
		embed.add_field(
			name="How do I respond?",
			value="Click on the emoji which you want your answer to be. If you don't want to respond click on the red X."
		)
		_embed = discord.Embed(colour=discord.Colour.purple())
		_embed.set_author(name="Rock! Paper! Scissors!", icon_url=ctx.author.avatar_url)
		_embed.add_field(
			name=f"You challenged {reciever.name} to rock paper scissors!",
			value="Respond with 'rock', 'paper' or 'scissors'! You can also submit 'decline' to decline the match."
		)
		_embed.add_field(
			name="How do I respond?",
			value="Click on the emoji which you want your answer to be. If you don't want to respond click on the red X."
		)
		msg = await challenger.send(embed=_embed)
		_msg = await reciever.send(embed=embed)
		for emoji in self.emojis:
			await msg.add_reaction(emoji)
			await _msg.add_reaction(emoji)

def setup(bot):
	bot.add_cog(RockPaperScissors(bot))