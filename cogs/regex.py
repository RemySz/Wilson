from discord.ext import commands
import re as regex


class Regex(commands.Cog, name="Regex"):
    """
    Regular Expressions library:
        Can search strings, used in lex analysis.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="RegEx Find",
        aliases=["find"],
        pass_content=True
    )
    async def regex_find(self, ctx, sub_string: str, string: str):
        """
        Finds all matches to the sub_string in string and returns the first result
        """
        try:
            result = regex.findall(f"{sub_string}", string)
            await ctx.send(result[0])
            return
        except Exception as e:
            await ctx.send(str(e))
            return

    @commands.command(
        name="RegEx Sub",
        aliases=["sub"],
        pass_content=True
    )
    async def regex_sub(self, ctx, find_string: str, sub_string: str, main_string: str):
        """
        Substitutes all find_string for sub_string in main_string. Returns a modified main_string.
        """
        try:
            result = regex.sub(find_string, sub_string, main_string)
            await ctx.send(result)
            return
        except Exception as e:
            await ctx.send(str(e))
            return

    @commands.command(
        name="RegEx Find All",
        aliases=["findall"],
        pass_content=True
    )
    async def regex_find_all(self, ctx, sub_string: str, string: str):
        """
        Finds all matches to the sub_string in string and returns all the matches.
        """
        try:
            result = regex.findall(sub_string, string)
            await ctx.send(result)
            return
        except Exception as e:
            await ctx.send(str(e))
            return

    @commands.command(
        name="RegEx Remove",
        aliases=["remove"],
        pass_content=True
    )
    async def regex_remove(self, ctx, sub_string: str, string: str):
        """
        Removes all instances of sub_string in string. Returns a modified string.
        """
        try:
            result = regex.sub(sub_string, "", string)
            await ctx.send(result)
        except Exception as e:
            await ctx.send(str(e))
        return


def setup(bot):
    bot.add_cog(Regex(bot))
