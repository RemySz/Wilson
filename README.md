# Complete rewrite

After the last implementation I tested the code. This resulted in a large number of bugs to be shown. The number of bugs was too overwhelming and I had to cut off a number of cogs and libraries into to get the bot working. Even then many of the bots commands would not be detected.

Due to the points listed above I've decided it makes the most sence to rewrite the bot from the ground up. This time, plan everything out and describe exactly what everything does to the very last detail. This will stop me from running away with code and ending up with large quantities of useless buggy code.

## Rewrite specifics

Firstly, a design phase, looking at exactly what I want the bot to be able to do and design and model around those ideas.
I do thing stretching out some of the features into their own library is a good idea. However, I do need to be careful of over abstraction.
### Cog ideas

Event Cog: Handles all events for the bot. For example on_member_join.
Dev Cog: Handles cog loading, reloading and other dev specific commands (virtual console)
Math Cog: Handles a wide range of mathmatical functions
Reddit Cog: Handles Reddit requests such as memes from r/memes and more
GitHub Cog: Handles GitHub notifications and management
Admin Cog: Handles administration commands such as bans and server management
Games Cog: Handles a small set of fun games to play
WilsonScript Cog: Handles all interaction with WilsonScript
### Library ideas:

Cog libraries: libraries which directly relate to a Cog; Math, Reddit, GitHub, Games, WilsonScript.
Guild initialisation: Different guilds can be initialised with different commands
WilsonScript discord API: Allows the addition of commands/Event triggers through WilsonScript

 ## WilsonScript

A small, high level programming language which can be used to interact with the bot on a more advanced level.
I LOVE this idea and think it could go very far. I would love a module system with a public library and more!

This idea definitely needs some advanced research and planning. It is approprate to assume the language would use an interpreter. However, given Python's performance it may be best to write the interpreter in another, more performant, language. My ideal choice would be C++ but I've never written an interpretator in it before so it may take some time.
Datatypes

bool
int
string
decimal
hex
Modules

$import "library_example"
$import "another_library_example"
Functions

func hello() {
output "hello";
}
Arrays

array animals: string = {"dog", "cat"};
multiarray numbers = {"1", 2, 3.0, true};
output animal[0];
Logical and arithmetric operators

            / ** () %
            && || !

Module system

The ability to create public libraries which are accessable to anyone.

Standard library ideas:

    libio : basic input and output
    libmath : basic math library
    libgraph : basic graph library
    libjson : basic json library
    libdb : basic database library
    libguild : basic discord guild library
    libuser : basic discord user library
