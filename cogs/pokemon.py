import discord, json
from discord.ext import commands
from data.stream import DataStructure

profile = {
	"id": 0,
	"pokemon": {},
}

class Instance:
	def __init__(self, name: str, channel: int):
		self.name = name  
		self.channel = channel 


class Pokemon(commands.Cog, name="Pokemon"):
	def __init__(self, bot):
		self.bot = bot
		self.active_pokemon = []
		self.stream = DataStructure()


	@commands.command(
		pass_context = True,
		name = "index",
		aliases = ["dex"]
	)
	async def index(self, ctx):
		# Search database for user's index
		# When found, return an embed listing all of them
		# If not found return error
		pass

	@commands.command(
		pass_context = True,
		name = "spawn",
	)
	async def spawn(self, ctx, name):
		embed = discord.Embed(colour=discord.Colour.random())

		pokemon = 0
		try:
			with open("pokemon/data/pokemon.json", 'r') as file:
				pokemon = json.load(file)
		except FileNotFoundError as e:
			embed.set_author(name="FileNotFoundError", icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error Message", value=str(e), inline=False)
			await ctx.send(embed=embed)
			return
		
		if pokemon != 0:
			try:
				pokemon = pokemon[name]
			except KeyError:
				embed.set_author(name=f"Pokemon \"{name}\" does not exist", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)
				return

			embed.set_author(name=f"A wild {name} appears!")
			embed.set_image(url=pokemon["image_path"])
			embed.set_footer(text=f"Spawned in by {ctx.author.name}", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			self.active_pokemon.append(Instance(name, ctx.channel))
			return
		
		else:
			embed.set_author(name="NullFileError", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			return

	@commands.command(
		pass_context = True,
		name = "catch"
	)
	async def catch(self, ctx, name):
		channel = ctx.channel 
		embed = discord.Embed(colour=discord.Colour.random())
		for pokemon in self.active_pokemon:
			if pokemon.channel == channel and pokemon.name == name:
				embed.set_author(
					name=f"{ctx.author.name} caught a wild {pokemon.name}",
					icon_url=ctx.author.avatar_url
				)
				embed.set_footer(text="The pokemon has been stored in your index (!index)")
				await ctx.send(embed=embed)
				print(self.active_pokemon)
				self.active_pokemon.remove(pokemon)
				# add pokemon to user's index
				with open("pokemon/data/pokemon.json", 'r') as file:
					poke = json.load(file)
				self.stream.load(ctx.author.id, "data/user/")
				self.stream.data["pokemon"][name] = {
					"level": 0,
					"health": poke[name]["health"],
					"attack": poke[name]["attack"],
					"defense": poke[name]["defense"],
					"agility": poke[name]["agility"],
				}
				self.stream.dump("data/user/")
				return
		embed.set_author(name="Pokemon could not be found!", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
		return
				

			
def setup(bot):
	bot.add_cog(Pokemon(bot))

	
		