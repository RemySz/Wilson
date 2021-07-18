from discord.ext import commands

class Ping(commands.Cog, name="Ping"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency)}ms")

    


def setup(bot):
    bot.add_cog(Ping(bot))

