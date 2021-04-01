import discord
import random
from discord.ext import commands

class CoinFlip(commands.Cog, name="Coin Flip"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name="coinflip",
        pass_context=True,
        aliases=["cf"]
    )
    async def coin_flip(self, ctx):
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

def setup(bot):
    bot.add_cog(CoinFlip(bot))