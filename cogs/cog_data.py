import discord
from discord.ext import commands

dataset = {}
# Format: user.name + user.id :{
#	 "sets": [1, 2, 3],
#		1: [], 2: [], 3: []
#	 }


class Data(commands.Cog, name='Data/dataset Commands'):
	'''Commands relating to the built in dataset functions'''

	def __init__(self, bot):
		self.bot = bot

	@commands.group(  
		name='dataset',  
		aliases=['ds'],
		pass_context=True,  
	)  
	async def dataset(self, ctx):
		if ctx.invoked_subcommand is None:
			pass
	
	@dataset.command(
		pass_context=True,
	 	name="new"
	 )
	async def new(self, ctx, *args):
			for key, value in dataset:
				if key == str(ctx.author):
						length = len(dataset[key]["sets"])
						dataset[key]["sets"].append(length + 1)
						dataset[key][length+1] = [i for i in args]
						return 0
			dataset[str(ctx.author)] = {"sets":[1], 1:[i for i in args]}

	@dataset.command(
		pass_context=True,
		name="remove",
		aliases=["rm"]
	)
	async def remove(self, ctx, dataset_id):
		for key, value in dataset:
			if key == str(ctx.author):
				for i in range(len(dataset[key]["sets"])):
					if dataset_id == i:
						dataset[key].remove(i)
						await ctx.send(f"Dataset {i} has been removed.")
						return 0
				await ctx.send(f"Dataset {i} doesn't exist")
				return 0
		await ctx.send(f"{ctx.author}, you do not own a dataset. Use `::dataset new` to create a new one.")


	@dataset.command(
		pass_context=True,
		name="list"
	)
	async def list(self, ctx):
		for key, value in dataset:
			if key == str(ctx.author):
				for i in range(len(dataset[key]["sets"])):
					await ctx.send(f"Set[{i}]: {dataset[key][i]}")
				return 0
	
	@dataset.command(
		pass_context=True,
		name="rename"
	)
	async def rename(self, ctx, dataset_id, new_name):
		for key, value in dataset:
			if key == str(ctx.author):
				try:
					dataset[key][new_name] = dataset[key].pop(dataset_id)
					await ctx.send(f"Dataset {dataset_id} has been renamed to {newname}")
				except:
					await ctx.send("Error occured while trying to rename!")

			
					



		

		
	



def setup(bot):
	bot.add_cog(Data(bot))