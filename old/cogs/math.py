import discord
from discord.ext import commands

# TODO
# Add math intrepreter

class Stack:
	_NULL = 0x0
	def __init__(self):
		self.value1 = Stack._NULL
		self.value2 = Stack._NULL
		self.operator = Stack._NULL

	def input_value(self, value) -> None:
		if self.value1 == Stack._NULL:
			self.value1 = value
		else:
			self.value2 = value

	def input_operator(self, operator) -> None:
		self.operator = operator
	




class Token(object):
	NUMBER = 0
	MULTIPLY = 1
	ADD = 2
	MINUS = 3
	DIVIDE = 4

class Analyse:
	NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	# INPUT: a list of operators
	# PROCESS: Split up and format operators(DO LATER)
	# PROCESS: Assign operators a Token
	# OUTPUT: a list of sets (Token, Value) in order
	def __init__(self, operators: list = []):
		self.product: list = []
		for term in operators:
			if term in Analyse.NUMBERS:
				self.product.append(set(int(term), Token.NUMBER))
			elif term == '+':
				self.product.append(set(term, Token.ADD))
			elif term == '-':
				self.product.append(set(term, Token.MINUS))
			elif term == '*':
				self.product.append(set(term, Token.MULTIPLY))
			elif term == '/':
				self.product.append(set(term, Token.DIVIDE))
			else:
				pass
	
class Parser:
	# INPUT: list of sets(value, token)
	# PROCESS: Separate sets into expressions
	# PROCESS: Create Abstract Syntax Tree from list of expressions 
	# OUTPUT:
	def __init__(self, tokens: list = []):
		# Grammar rules:
		# EXPRESSION = VALUE OPERATOR VALUE  

		# Stack:
		pass
		
			


def calculate_variance_population_string(use_dataset: bool = False, data: list = []):
	if use_dataset:
		pass # TODO
	else: # data = [10, 10, 20]
		VAR_X = 0
		VAR_N = len(data) # N = 3
		VAR_SUM = 0
		for i in data:
			VAR_SUM += i # SUM = 40
		VAR_MEAN = VAR_SUM/VAR_N # MEAN = 40/3 = 13.33333334
		for i in data:
			term = i - VAR_MEAN # 10 - 13.333, 10 - 13.333, 20 - 13.333
			term = term ** 2
			VAR_X += term
		VAR_X /= VAR_N
		return (f"ANSWER = {VAR_X}\nN = {VAR_N}\nMEW = {VAR_MEAN}\nSUM = {VAR_SUM}")

def calculate_variance_population_raw(use_dataset: bool = False, data: list = []):
	if use_dataset:
		pass # TODO
	else: # data = [10, 10, 20]
		VAR_X = 0
		VAR_N = len(data) # N = 3
		VAR_SUM = 0
		for i in data:
			VAR_SUM += i # SUM = 40
		VAR_MEAN = VAR_SUM/VAR_N # MEAN = 40/3 = 13.33333334
		for i in data:
			term = i - VAR_MEAN # 10 - 13.333, 10 - 13.333, 20 - 13.333
			term = term ** 2
			VAR_X += term
		VAR_X /= VAR_N
		return {'answer':VAR_X,'n':VAR_N,"mean":VAR_MEAN,"sum":VAR_SUM}

def calculate_variance_sample_string(use_dataset: bool = False, *args):
	if use_dataset:
		pass # TODO
	else:
		dataset = [int(i) for i in args]
		VAR_X = 0
		VAR_N = len(dataset)
		VAR_SUM = 0
		for i in dataset:
			VAR_SUM += i
		VAR_MEAN = VAR_SUM/VAR_N
		for i in dataset:
			term = i - VAR_MEAN
		term = term ** 2
		VAR_X += term
		VAR_X /= VAR_N - 1
	return (f"ANSWER = {VAR_X}\nN = {VAR_N}\nMEW = {VAR_MEAN}\nSUM = {VAR_SUM}")

def calculate_variance_sample_raw(use_dataset: bool = False, data: list = []):
	if use_dataset:
		pass # TODO
	else:
		VAR_X = 0
		VAR_N = len(data)
		VAR_SUM = 0
		for i in data:
			VAR_SUM += i
		VAR_MEAN = VAR_SUM/VAR_N
		for i in data:
			term = i - VAR_MEAN
			term = term ** 2
			VAR_X += term
		VAR_X /= VAR_N - 1
	return {'answer':VAR_X,'n':VAR_N,"mean":VAR_MEAN,"sum":VAR_SUM} 

class Math(commands.Cog, name="Math"):
	def __init__(self, bot):
		self.bot = bot

	@commands.group(
		pass_context = True,
		name = "variance",
		aliases = ["variant"]
	)
	async def math_variance_command(self, ctx):
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name="Failed to invoke subcommand", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)

	@math_variance_command.command(
		pass_context = True,
		name = "population",
		aliases = ["pop"]
	)	
	async def math_variance_subcommand_population(self, ctx, data: list = []):
		await ctx.send(calculate_variance_population_raw(data))
		#embed = discord.Embed(colour=discord.Colour.random())
		#embed.set_author(name="Variance population calculation", icon_url=ctx.author.avatar_url)
		#embed.add_field(name="Variance (answer)", value=)
	
	@math_variance_command.command(
		pass_context = True,
		name = "sample",
		aliases = ["sam"]
	)	
	async def math_variance_subcommand_sample(self, ctx, data: list = []):
		await ctx.send(calculate_variance_sample_raw(data))


class Calculate(commands.Cog, name="Calculate"):
	def __init__(self, bot):
		self.bot = bot


def setup(bot):
	bot.add_cog(Math(bot))
	bot.add_cog(Calculate(bot))