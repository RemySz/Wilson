import discord
from discord.ext import commands
from lib.brainfuck import interpreter_discord as bf

class Brainfuck(commands.Cogs, name="Brainfuck"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name = "brainfuck",
        aliases = ["bf"],
        pass_context = True
    )
    async def brainfuck(self, ctx):
        """
        Interprete brainfuck codeusing this command!
        """
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=ctx.author, icon_uirl=ctx.author.avatar_url)
            embed.set_field(name="Error", value="User failed to invoke subcommands.", inline=False)
            embed.set_field(name="Conclusion", value="Use \"bf raw <code> \"", inline=False)
            await ctx.send(embed=embed)


    @brainfuck.command(
        name = "raw",
        pass_context = True
    )
    async def raw(self, ctx, code: str):
        """
        Enter the brainfuck code using "bf raw ++[>+<-]>." for example.
        """
        bf.process(ctx, str(code))

        embed = discord.Embed(colour=discord.Colour.teal())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Input", value=str(code), inline=False)
        embed.add_field(name="Output", value=bf.output(), inline=False)
        await ctx.send(embed=embed)

    @brainfuck.command(
        name = "file",
        aliases = ['f'],
        pass_context = True
    )
    async def file(self, ctx):
        """
        Attach a file and use "bf file" to have that entire file interpreted!!
        """
        await ctx.send("Sorry, files aren't avaliable yet!")