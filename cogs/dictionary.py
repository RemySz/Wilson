import discord
from discord.ext import commands
import json
import requests

def request_information(word, language) -> dict:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/{language}/{word.lower()}"
    data = requests.get(url)
    data = json.dump(data.json())
    return data
    
def format_information(data) -> dict:
    output = {
        "word":data[0]["word"],
        "audio":data[0]["phonetics"][0]["audio"],
        "type":data[0]["meanings"]["partOfSpeach"],
        "definitions":data[0]["meanings"]["definitions"]
    }
    return output

class Dictionary(commands.Cog, name="Dictionary commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx: discord.Context, word):
        # Request data
        data = request_information(word, "en_GB")
        # Search/find/re-format data
        data = format_information(data)
        # Output data
        embed = discord.embed(colour=discord.Colour.random())
        embed.set_author(name=data["word"], icon_url=ctx.author.avatar_url)
        embed.add_field(name="Word type", value=data["type"], inline=False)
        for definition in data["definitions"]:
            embed.add_field(name="Definition", value=definition["definition"], inline=False)
            embed.add_field(name="Example", value=definition["example"], inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Dictionary(bot))