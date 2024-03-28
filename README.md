# learning-git

Pig Dice Game https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Pass_the_pigs_dice.jpg/330px-Pass_the_pigs_dice.jpg
Welcome!
Greetings from the development team! We're thrilled to introduce our latest project, the Pig Dice Game, a Python-based rendition of the classic dice game. This project represents our collective effort to bring the fun and strategy of Pig into the digital realm, accessible right from your terminal.


Let's Get Started
Before You Begin
You'll need Python 3.6 or newer to play our game.

.   Set Up
First, clone our project repository:

git clone https://github.com/EmperorOlashinbo/pig-dice-game.git
cd pig-dice-game

Then, create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Don't forget to install the required dependencies:

pip install -r requirements.txt

.   Dive Into the Game https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Two_red_dice_01.svg/1007px-Two_red_dice_01.svg.png
Launching the game is simple:

python dice_game1.py
Just follow the prompts to kick things off and enjoy the game with your friends or against our AI.

.   How We Play
The essence of the Pig Dice Game is risk management. Roll the dice to accumulate points, but be cautious—rolling a '1' resets your turn's score! You can choose to 'hold' at any point to secure your points. The game includes:

A single-player mode to challenge our crafty computer opponent.
A two-player mode for epic face-offs.
A high-score tracker to immortalize your victories.

.   Behind the Scenes
Collaborate With Us
We're always on the lookout for new ideas, improvements, or bug fixes. Feel free to dive into our code and contribute! Check out CONTRIBUTING.md for more on how to submit your contributions.

.   Test Like a Pro
We believe in the power of testing. Run the unit tests to ensure everything's in order:

python -m unittest

.   Style Matters
We adhere to PEP 8 standards for a clean, readable codebase. Use flake8 for style checks and black for automatic formatting:

flake8
black .

.   Docs and Diagrams
Feeling curious about the internals? Generate the documentation and UML diagrams:

make doc
make uml
Graphviz needs to be set up for generating UML diagrams.

.   A Note on Licensing
Our project is open under the MIT License. See LICENSE.md for the full text.


