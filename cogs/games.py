import discord
import random
from discord_slash import cog_ext
from discord.ext import commands
import lib.queue as lib


class CoinFlip(commands.Cog, name="Coin Flip"):
    """
    Commands in which one throws a coin for the pleasure of knowing
    whether said coin lands on heads or tails.
    """
    def __init__(self, bot):
        self.bot = bot
        self.stack = lib.Stack()

    @commands.group(
        name="coinflip",
        pass_context=True,
        aliases=["cf"]
    )
    async def coin_flip(self, ctx):
        """
        Simple. Flips a coin.
        """
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(colour=discord.Colour.random())
            if random.randint(0, 1) == 0:
                embed.set_author(
                    name="Coin landed on heads!",
                    icon_url="https://pics.freeicons.io/uploads/icons/png/10346513851578289009-512.png"
                )
            else:
                embed.set_author(
                    name="Coin landed on tails!",
                    icon_url="https://pics.freeicons.io/uploads/icons/png/10346513851578289009-512.png"
                )
            await ctx.send(embed=embed)

    @coin_flip.group(
        name="bet",
        pass_context=True
    )
    async def coin_flip_bet(self, ctx, bet_id=None):
        if ctx.invoked_subcommand is None and bet_id is None:
            await ctx.send("Need subcommand soz bro")
        elif bet_id is not None:
            pass
            # Add bet to stack
        """
        ~ TODO ~
        1. Create bet stack
        2. Add author and amount to stack
        3. Set stack to active (allows challengers)
        4. Start timer
        5. Add challengers to stack 
        6. When timer runs out deactivate stack 
        7. Sort challengers 
        8. Output bet winner
        9. Add money to winner balance
        10. delete stack
        """

    @coin_flip_bet.command(
        name="start",
        pass_context=True
    )
    async def coin_flip_bet_start(self, ctx, bet_amount: int):
        self.stack.set_author(ctx.author.id)
        embed = discord.Embed(colour=discord.Colour.random())
        embed.set_author(
            name=f"{ctx.author.name} has started a bet!",
            icon_url="https://pics.freeicons.io/uploads/icons/png/10346513851578289009-512.png"
        )
        embed.add_field(name="Bet type", value="Coin flip (Heads or Tails)", inline=False)
        embed.add_field(
            name="Bet is live!",
            value=f"You have 60 seconds to submit your bet!\nYou can submit a bet using ::coinflip bet <amount>!"
        )
        await ctx.send(embed=embed)
        while self.stack.start_timer(seconds=60) == "Finished":
            await ctx.send("Bets are in.")





def setup(bot):
    bot.add_cog(CoinFlip(bot))