# -*- coding: utf-8 -*-
"""
Voting system
"""
import discord 
from discord.ext import commands


emojis = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]

class Poll(commands.Cog, name="Voting"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def poll(self, ctx, poll_name, *fields):
		"""Creates a poll for people to vote on"""
		embed = discord.Embed(colour=discord.Colour.teal())
		if len(fields) > 9:
			embed.set_author(name="Too many poll items! Maximum is 10!", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			return
		embed.set_author(name=poll_name, icon_url=ctx.author.avatar_url)
		for i in range(len(fields)):
			embed.add_field(name=f"{fields[i]}", value=f"Vote using {emojis[i]}!", inline=False)
		msg = await ctx.send(embed=embed)
		for i in range(len(fields)):
			await msg.add_reaction(emojis[i])


def setup(bot):
	bot.add_cog(Poll(bot))