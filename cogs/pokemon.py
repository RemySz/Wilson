from discord.ext import commands


class PokemonDev(commands.Cog, name="Pokemon (Dev only)"):
    """
    Pokemon commands which are limited to only developers.
    This allows the developers to test things such as summoning pokemon,
    spawn rates and etc
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="summon",
        pass_contect=True
    )
    async def summon_pokemon(self, pokemon_name):
        """
        TODO
        Search database for pokemon_name TODO (Make a move and pokemon index (database) )
        Create an active pokemon object TODO (Finish pokemon object and loading from json data)
        Send pokemon information to channel
        Log message id to pokemon object
        Start despawn timer
        When despawn timer ends
        Remove message from channel
        Remove and delete pokemon object
        """
        pass
