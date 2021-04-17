from discord.ext import commands
import discord
from lib.giphy import GiphyAPIWrapper


class Gifs(commands.Cog, name="Gifs!"):
    """
    Create calls to giphy API and get cool gifs :sunglasses:
    """

    def __init__(self, bot):
        self.bot = bot
        self.giphy = GiphyAPIWrapper()

    @staticmethod
    def create_gif_embed(ctx, member, gif):
        """
        This just stops repeated code within each function.
        It creates a custom embed message. This makes the actual gif command code very readable.
        """
        embed = discord.Embed(colour=discord.Colour.random())
        killer = f"{(ctx.author.nick if ctx.author.nick is not None else ctx.author.name)}"
        member = f"{(member.nick if member.nick is not None else member.name)}"
        embed.set_author(name=f"{killer} just killed {member}!", icon_url=ctx.author.avatar_url)
        embed.set_image(url=gif)
        return embed

    @commands.command(name="kill")
    async def kill_gif_command(self, ctx, member: discord.Member):
        """
        Kill gif command -> returns a kill message and gif.
        """
        await ctx.send(embed=self.create_gif_embed(ctx, member, self.giphy.search("kill")))

    @commands.command(name="kiss")
    async def kiss_gif_command(self, ctx, member: discord.Member):
        """
        Kiss gif command -> returns a Kiss message and gif.
        """
        await ctx.send(embed=self.create_gif_embed(ctx, member, self.giphy.search("kiss")))

    @commands.command(name="hug")
    async def hug_gif_command(self, ctx, member: discord.Member):
        """
        Hug gif command -> returns a hug message and gif.
        """
        await ctx.send(embed=self.create_gif_embed(ctx, member, self.giphy.search("hug")))

    @commands.command(name="boo")
    async def boo_gif_command(self, ctx, member: discord.Member):
        """
        Boo gif command -> returns a boo message and gif.
        """
        await ctx.send(embed=self.create_gif_embed(ctx, member, self.giphy.search("boo")))


def setup(bot):
    bot.add_cog(Gifs(bot))
