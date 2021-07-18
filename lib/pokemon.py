"""
 - Pokemon -
 Although this is "Pokemon" it's not.
 This is like Pokemon but more of similar styled game with my own unique
 pokemon with inside jokes and all.
 It is called Pokemon internally because it is easier for people to see "Pokemon"
 and understand instantly what something does than a long explanation on that
 it actually is. Regardless, an explain is provided for each class.

 - Brief Explanation -
 There are four base types: fire, water, air, and earth.
 (More types will likely be added in the future)
 Each pokemon has up to 4 moves and a health bar.
 These are not specified in the Pokemon class because
 the Pokemon class is more of a base class for every other Pokemon.

 For example, a "Dude" Pokemon may inherit the Pokemon class and
 then that class will contains the stats like health, moves, etc.

 Types:
    Water:
        Weak against: Earth
        Strong against: Fire, air
    Fire:
        Weak against: Water, air
        Strong against: Earth
    Earth:
        Weak against: Fire
        Strong against: Air, Water
    Air:
        Weak against: Water
        Strong against: Fire
        (Neutral against Earth)

 - Pokemon stats -
 Pokemon contain a set of stats explaining their features and what they are good at.
 Example:
    Wilson:
        Type: Fire
        Health: 10
        Moves: [ Punch, Rage, Intimidate, Sleep ]
        Strength: 2, 5%
        Damage: 2

- What does these mean? -
"Type" is the type of the Pokemon. This means some Pokemon may be stronger against others simply
because they are a different (counter) type. There are also moves which are specific to just that
type.

"Health" as you can guess; this is how much health the Pokemon has. When health drops to nothing
the Pokemon will fall unconscious.

"Moves" these are the moves the Pokemon currently has. All Pokemon have a maximum of 4 moves.
There are special, Pokemon specifics, and Type specific moves. All moves come from the move
index. The move index contains all the information about a move; base damage, level required, etc.
Moves have an individual damage setting meaning when a Pokemon attacks another Pokemon it will
calculate (Damage + Strength + Move Damage) - Enemy health.

"Damage" this is how much health will be taken away from the opponent's Pokemon's health.
This is a base stat before move and strength. This means when a Pokemon attacks with a
damage of 1 it will always do at least a damage of 1. Moves and strength will increase how
much damage is done.

"Strength" this is a bonus to the damage. It contains two stats, the strength bonus damage and the
chances of that bonus damage happening. For example a Pokemon could have a Strength of (100, 0.0001%)
which means it has a 0.0001% chance of dealing an additional 100 bonus Damage points to an enemy.

- Training -
A Pokemon can be taught new moves. This is done by hiring a trainer. Depending on the move and the
trainer there will be a price for how much training that Pokemon will be. There is also a time cost.

Manual training:
There are sites such as Cloud city, Mountain district, Flower fields, and Ocean monument which
all allow Pokemon owners to train by battling wild Pokemon.
A Pokemon will gradually level as it battles other Pokemon.

A Pokemon can also level up while fighting another Player's Pokemon
"""
# Packages
import random


class PokemonType:
    """
    This just simply contains the different types of Pokemon available.
    """
    NULL = -1
    FIRE = 0
    WATER = 2
    AIR = 3
    EARTH = 4

    def __init__(self):
        self.type = PokemonType.NULL
        self.types = [
            PokemonType.FIRE, PokemonType.WATER,
            PokemonType.AIR, PokemonType.EARTH
        ]

    def __repr__(self):
        if self.type == PokemonType.NULL:
            return "NULL"
        elif self.type == PokemonType.FIRE:
            return "FIRE"
        elif self.type == PokemonType.WATER:
            return "WATER"
        elif self.type == PokemonType.AIR:
            return "AIR"
        elif self.type == PokemonType.EARTH:
            return "EARTH"
        else:
            return "UNKNOWN"

    def random(self):
        self.type = random.choice(self.types)
        return

    def set(self, type_):
        self.type = (type_ if type_ in self.types else self.type)
        return self.type


class Pokemon:
    """
    - Pokemon Class -
    This is the base class that all Pokemon inherit from.
    This class contains all the basic information for a Pokemon
    such as health, exp, level, and type.
    NOTE this information is not initialised.
    """
    sex = ["male", "female"]

    def __init__(self):
        self.name: str = "Unresolved"
        self.type = PokemonType()
        self.sex = random.choice(Pokemon.sex)
        self.age: int = 0
        self.health = 0
        self.min_health = 0
        self.max_health = 0
        self.base_health = 0
        self.active_moves = []
        self.move_index = []
        self.exp = 0
        self.level = 0

    def __repr__(self):
        return f"Pokemon: \"{self.name}\", {self.age*12} months, {self.sex}, {self.type}"

    def __dict__(self):
        return {
            "name": self.name,
            "type": repr(self.type),
            "sex": self.sex,
            "age": self.age,
            "health": {
                "min": self.min_health,
                "max": self.max_health,
                "base": self.base_health
            },
            "moves": self.active_moves,
            "move_index": self.move_index,
            "level": self.level,
            "exp": self.exp
        }

    def __str__(self):
        return f"Pokemon: \"{self.name}\", {self.age*12} months, {self.sex}, {self.type}"


"""
All moves are stored in data/pokemon/moves.
The move index will be stored in an sqlite database fir simplicity.
The table will include; 
    move database id,  
    move name, 
    type specific (None for all types),
    pokemon specific (None for all Pokemon),
    base damage

When a Pokemon is created it will be randomly given starter moves
from the move index.

If the Pokemon needs to be stored (e.g. it is caught) it will be stored
in a separate sqlite database containing the owner and a few more bits 
of information. 
The database id for this Pokemon will then be stored in the Player's user data.

"""
