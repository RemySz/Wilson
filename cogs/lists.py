from discord.ext import commands
import discord

class Lists(commands.Cog, name="Lists"):
	def __init__(self, bot):
		self.bot = bot  
	
	@commands.group(
		pass_context = True,
		aliases = ["list"]
	)
	async def list_command_group(self, ctx):
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error", value="Invoked subcommand was not found in command group context")
			await ctx.send(embed=embed)

	@list_command_group.command(
		pass_context = True,
		aliases = ["create", "new"]
	)
	async def new_subcommand(self, ctx, name: str, status: str = "public"):
		with open(f"./data/lists/{name.lower()}.txt", 'w') as f:
			string = f"# Owner: {ctx.author.id} ({ctx.author.name})\n"
			string += f"# List name: {name.lower()}\n"
			string += f"# Status: {status}\n"
			f.write(string)
			del string
		await ctx.send(f"Created new list: {name}")


	@list_command_group.command(
		pass_context = True,
		aliases = ["get","contents"]
	)
	async def contents_subcommand(self, ctx, name: str):
		with open(f"./data/lists/{name}.txt", 'r') as f:
			await ctx.send(f"```css\n{f.read()}```")


	@list_command_group.command(
		pass_context = True,
		aliases = ["add"]
	)
	async def add_subcommand(self, ctx, name: str, item: str):
		embed = discord.Embed(colour=discord.Colour.random())
		elements = []
		try:
			with open(f"./data/lists/{name}.txt", 'r') as f:
				for line in f.readlines():
					if line.startswith("#"):
						pass
					elif line == " " or line == "\n":
						pass
					else:
						elements.append(line)

			with open(f"./data/lists/{name}.txt", 'a') as f:
				f.write(f"{len(elements)}. {item}\n")

			embed.set_author(name=f"Added {item} to {name}", icon_url=ctx.author.avatar_url)
			embed.add_field(name=f"Index of {len(elements)}", value="You can use the index to reference your item later one.", inline=False)
			del elements

		except Exception as e:
			print(e)
			embed.colour = discord.Colour.red()
			embed.set_author(name="Error", icon_url=ctx.author.avatar_url)
			embed.add_field(name="Console", value=str(e), inline=False)

		finally:
			await ctx.send(embed=embed)
			del embed

	@list_command_group.command(
		pass_context = True,
		aliases = ["remove", "rm"]
	)
	async def remove_subcommand(self, ctx, name: str, index: int):
		embed = discord.Embed(colour=discord.Colour.random())
		elements = []
		try:
			with open(f"./data/lists/{name}.txt", 'r') as f:
				for line in f.readlines():
					if line.startswith("#"):
						pass
					elif line == " " or line == "\n":
						pass
					else:
						elements.append(line)

			with open(f"./data/lists/{name}.txt", 'w') as f:
				i = 0
				for element in elements:
					if elements[index] == element:
						elements.remove(element)
					else:
						elements.remove(element)
						element = element.split(".", 1)[1]
						elements.append(f"{i}. {element}")
					i+=1
				f.writelines(elements)



			embed.set_author(name=f"removed {elements[index]} from {name}", icon_url=ctx.author.avatar_url)
			embed.add_field(name="Updated index", value="The index has been shifted due to a removed item.", inline=False)
			del elements

		except Exception as e:
			embed.colour = discord.Colour.red()
			embed.set_author(name="Error", icon_url=ctx.author.avatar_url)
			embed.add_field(name="Console", value=str(e), inline=False)

		finally:
			await ctx.send(embed=embed)
			del embed

def setup(bot):
	bot.add_cog(Lists(bot))
	


	
			
				


