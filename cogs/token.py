from discord.ext import commands
import lib.basicTokeniser as bax

class Token(commands.Cog, name="Tokeniser"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="lex",
        aliases=["analyse"],
        pass_content=True
    )
    async def lexer(self, ctx, code: str):
        output = ""
        loki = bax.Lexer(code)
        for item in loki.analyse():
            output += item.__repr__()
        await ctx.send(output)
        return



def setup(bot):
    bot.add_cog(Token(bot))
