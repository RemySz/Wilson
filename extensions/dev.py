from discord.ext import commands
import discord

class Dev(commands.Cog, name="Dev"):
	def __init__(self, bot):
		self.bot = bot

	async def cog_check(self, ctx):  
		'''
		The default check for this cog whenever a command is used. Returns True if the command is allowed.
		'''
		return ctx.author.id == self.bot.author_id

	@commands.group(
		name="dev",
		aliases=[],
		pass_context = True
	)
	async def dev(self, ctx):
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error", value="Your commend required a subcommand. None was provided.", inline=True)
			await ctx.send(embed=embed)

	@dev.group(
		pass_context = True,
		name="cog"
	)
	async def cog(self, ctx):
		if ctx.invoked_subcommand is None:
    			embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
				embed.add_field(name="Error",value="Your command required a subcommand. None was provided.", inline=True)
				await ctx.send(embed=embed)


	@cog.command(  
		name='reload',  
		aliases=['rl']  
	)  
	async def reload(self, ctx, cog):
		'''
		Reloads a cog.
		'''
		extensions = self.bot.extensions  
		if cog == 'all':  
			for extension in extensions:
				self.bot.unload_extension(cog)
				self.bot.load_extension(cog)
			await ctx.send('Done')
		if cog in extensions:
			self.bot.unload_extension(cog) 
			self.bot.load_extension(cog)  
			await ctx.send('Done')  
		else:
			await ctx.send('Unknown Cog')  
	
	@cog.command(name="unload", aliases=['ul']) 
	async def unload(self, ctx, cog):
		'''
		Unload a cog.
		'''
		extensions = self.bot.extensions
		if cog not in extensions:
			await ctx.send("Cog is not loaded!")
			return
		self.bot.unload_extension(cog)
		await ctx.send(f"`{cog}` has successfully been unloaded.")
	
	@cog.command(name="load")
	async def load(self, ctx, cog):
		'''
		Loads a cog.
		'''
		try:

			self.bot.load_extension(cog)
			await ctx.send(f"`{cog}` has successfully been loaded.")

		except commands.errors.ExtensionNotFound:
			await ctx.send(f"`{cog}` does not exist!")

	@cog.command(name="listcogs", aliases=['lc'])
	async def listcogs(self, ctx):
		'''
		Returns a list of all enabled commands.
		'''
		base_string = "```css\n"  
		base_string += "\n".join([str(cog) for cog in self.bot.extensions])
		base_string += "\n```"
		await ctx.send(base_string)

def setup(bot):
	bot.add_cog(Dev(bot))

def terminate(bot):
	bot.remove_cog(Dev(bot))
	