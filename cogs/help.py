from discord.ext import commands
import discord


class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
        self.commands = [
            {
                "name": "coinflip",
                "description": "Simple. Slips a coin."
            }
        ]

    @commands.group(
        name="help",
        pass_context=True,
        aliases=["?"]
    )
    async def help(self, ctx, command=None):
        if ctx.invoked_subcommand is None:
            if command is not None:
                embed = discord.Embed(colour=discord.Colour.random())
                embed.set_author(
                    name="So you need some help? huh?!",
                    icon_url="https://cdn4.iconfinder.com/data/icons/ballicons-2-new-generation-of-flat-icons/100/help-512.png"
                )
                for term in self.commands:
                    if term["name"] == command:
                        embed.add_field(name=term["name"], value=term["description"], inline=False)
                await ctx.send(embed=embed)
            else:
                pass
                # Show help categories (e.g. games, economy, fun, etc)



def setup(bot):
    bot.add_cog(Help(bot))

