import discord
from discord.ext import commands


class Output(commands.Cog, name='Mathmatical Commands'):
	'''Commands relating to the built in math functions'''

	def __init__(self, bot):
		self.bot = bot

	@commands.command(  
		name='variance',  
		aliases=['variance']  
	)  
	async def calculate_variance(self, ctx, dataset):
		'''
		Calculates variance with given dataset
		'''
		pass

		

		
	



def setup(bot):
	bot.add_cog(Output(bot))