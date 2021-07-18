import discord
from discord.ext import commands
import json, os
import requests

def request_information(word, language) -> dict:
	url = f"https://api.dictionaryapi.dev/api/v2/entries/{language}/{word.lower()}"
	data = requests.get(url)
	return data.json()

    
def format_information(data) -> dict:
	output = {}
	output['word'] = data[0]['word']
	output["type"] = data[0]["meanings"][0]["partOfSpeech"]
	output["definitions"] = data[0]["meanings"][0]["definitions"]
	return output

class Dictionary(commands.Cog, name="Dictionary commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def define(self, ctx, word):
        # Request data
		data = request_information(word, "en_GB")
		try:
			if data["title"] == 'No Definitions Found':
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name=f"{word} couldn't be found!", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)
				return
		except: 
			pass
        # Search/find/re-format data
		print(data)
		data = format_information(data)
        # Output data
		embed = discord.Embed(colour=discord.Colour.random())
		embed.set_author(name=data["word"], icon_url=ctx.author.avatar_url)
		embed.add_field(name="Word type", value=data["type"], inline=False)
		try:
			for definition in data["definitions"]:
				embed.add_field(name="Definition", value=definition["definition"], inline=False)
				try:
					embed.add_field(name="Example", value=definition["example"], inline=False)
				except: pass
		except Exception as e:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=f"Input {word} caused the following error!", icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error", value=str(e))

		await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Dictionary(bot))