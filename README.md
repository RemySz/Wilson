# Wilson discord bot

Basic bot used for discord servers. I haven't made the bot public so instead I've released the source code on GitHub.
Contributions are fine as long as they aren't intentially stupid request. make sure to remove files you do not want in the repository efore committing.

## Brainfuck Interpreter
On hold...
Wilson bot contains a simple brainfuck interpreter.
The interpreter contains multiple flags which allows the play to see the full affect of code.
I am also interested in building my own language the bot could compute on it's own. 

`::bf +++[>+++<-]>.`
`::brainfuck -[>+>+<<-.]>.>.`

## Data 
Allows users to store information and data.
Users will store data/information using `::Dataset` 

## Math 
Bot contains a basic math interpreter.

### Calculation (Interpreter)
Calculation command kick starts the math interpreter which accepts a string of mathmatical operators.

Example:
`::calculate "5 + (3 * 3)"`
`::cal "7 * (5 + 3)"`

Double quotes (") are required as the bot only accepts a single string argument.

### Variance
Users will be able to calculate the sample varience and population variance.
Command will accept both a dataset and raw arguments.

Example:
`::math variance population dataset_example`
`::math variance sample 10 10 10 10 20 30 40`
`::math variance sample dataset_example2`





