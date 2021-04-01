import discord
import random
from main import slash
from discord.ext import commands
from lib.queue import *


class CoinFlip(commands.Cog, name="Coin Flip"):
    """
    Commands in which one throws a coin for the pleasure of knowing
    whether said coin lands on heads or tails.
    """
    def __init__(self, bot):
        self.bot = bot
        self.queue = Queue()

    @slash.slash(
        name="coinflip",
        description="Simple. Flips a coin."
    )
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

    @coin_flip.command(
        name="bet",
        pass_context=True
    )
    async def coin_flip_bet(self, ctx, starting_bet_amount: int):
        pass


def setup(bot):
    bot.add_cog(CoinFlip(bot))