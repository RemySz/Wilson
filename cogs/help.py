from discord.ext import commands
import discord
import json


class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def get_category(category):
        with open("./data/help/help.json", 'r') as file:
            config = json.load(file)
            return config[category]

    @staticmethod
    def get_command(category, command):
        with open("./data/help/help.json", 'r') as file:
            config = json.load(file)
            for element in config:
                if element["name"] == command or element["command"] == command:
                    return element
        return

    @commands.command(name="help")
    async def help_command(self, ctx, category=None):
        embed = discord.Embed(colour=discord.Colour.random())
        if category is None:
            embed.set_author(name="Help menu")
            embed.add_field(name="Games", value="To see the games commands use: '::help games'")
            embed.add_field(name="Economy", value="To see the economy commands use: '::help economy'")
        else:
            embed.set_author(name=f"Help: {category.lower()} commands")
            for game in self.get_category(category.lower()):
                string = "Commands: "
                for i in range(game["commands"]):
                    string += game["commands"][i]
                string += f"\n\n{game['description']}"
                embed.add_field(name=game["name"], value=string, inline=False)
        await ctx.send(embed=embed)
        return





def setup(bot):
    bot.add_cog(Help(bot))

