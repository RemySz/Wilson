# Wilson discord bot

Basic bot used for discord servers. I haven't made the bot public so instead I've released the source code on GitHub.
Contributions are fine as long as they aren't intentially stupid request. make sure to remove files you do not want in the repository efore committing.

## Brainfuck Interpreter
Wilson bot contains a simple brainfuck interpreter.
The interpreter contains multiple flags which allows the play to see the full affect of code.
I am also interested in building my own language the bot could compute on it's own. 

## Database
Wilson bot contains a Json database...

### Guild configuration
When Wilson joins a server he will initialise which sets up a guild directory containing many json files
with information and configuration about the guild that the bot can use.

The config of a guild can be manipulated by the owner or anyone with Administrator.
This is explained more in the initialisation section.

### User logging
A user's profile in the database will not be created unless they interact with the bot (excluding basic commands).
This allows the bot to carry a user's profile across servers.

Don't worry! Little discord information is stored. Balance(£), XP, and other variables are contained within the profile.


## Math 
Bot contains a basic math interpreter.

### Commands
Calculation command kick starts the math interpreter which accepts a string of mathmatical operators.

Example:
`::calculate "5 + (3 * 3)"`
`::cal "7 * (5 + 3)"`

Double quotes (") are required as the bot only accepts a single string argument.

## Statistics
Wilson will record data about the guild and output them as a graph/chart.
This is NOT on by default. `::stats config enable=true` will enable statisistics.

Examples:
`::stats members_join_over_time graph=true` 
`::stats config -list` (Lists all config items)
`::stats config -list_stats` (Lists all stats being tracked)




