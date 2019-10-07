## Running the game

From the root:

`python src/main.py`

## Running Tests

Each module under `src/logic` has corresponding tests of the format `**.ut.py` where applicable. Navigate to the module path and then run (for example):

`python card.ut.py`

### Rules

The game itself is memory. You have the option to choose from 2-4 players, and you can also choose how many cards to play with (provided it's an even number greater than or equal to twice the number of players). After that you will be prompted to enter player names, after which the game will begin.

You will first flip over a card by entering its corresponding number (found underneath the drawing of the card). This card will be highlighted in green text. You will then have the opportunity to flip another card. You will then have the chance to see both of your flipped over cards, after which you will either get another turn if you found a match, or it will be the next players turn. If you get a match, your matched cards will be highlighted in a custom color.

### Design Choices

The Card and Deck were Classes that I designed and implemented were fairly trivial. I utilized Enums for greater Code Readibility. The more complex logic comes with the colored ASCII drawing of the Card object.

To allow for fast lookup, I utilized dictionaries (hashmaps) to store player information (keyed by a player id). I then chose to use a set to keep track of the cards that were either actively selected or had already been matched. This way, to check if a card choice was valid, I could simply check if the choice index was in the invalid_cards set.

I chose to use Python for the ease of readability and the fact that it was better suited for writing command line applications than my preferred dev language, javascript.

### External Libs:
colorama and termcolor, used for colorized terminal output