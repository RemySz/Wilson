import discord
from discord.ext import commands


class BrainfuckInterpreter(commands.Cog, name='Brainfuck Interpreter Commands'):
	'''Commands relating to the built in Brainfuck interprefer'''

	def __init__(self, bot):
		self.bot = bot

	@commands.command(  
		name='interprete',  
		aliases=['bf']  
	)  
	async def interprete(self, ctx, cog, code):
		'''
		Interpretes the brainfuck code supplied by the user. 
		'''

		# TODO

		
	



def setup(bot):
	bot.add_cog(BrainfuckInterpreter(bot))