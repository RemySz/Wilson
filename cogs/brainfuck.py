import discord
from discord.ext import commands
from lib.brainfuck import interpreter as bf

class Brainfuck(commands.Cogs, name="Brainfuck"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name = "brainfuck",
        aliases = ["bf"],
        pass_context = True
    )
    async def brainfuck(self, ctx):
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
        bf.process(str(code))
        with open("output.txt", 'r') as f:
            output = f.read()

        embed = discord.Embed(colour=discord.Colour.teal())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Input", value=str(code), inline=False)
        embed.add_field(name="Output", value=output, inline=False)
        await ctx.send(embed=embed)



    @brainfuck.command(
        name = "file",
        aliases = ['f'],
        pass_context = True
    )
    async def file(self, ctx):
        await ctx.send("Sorry, files aren't avaliable yet!")