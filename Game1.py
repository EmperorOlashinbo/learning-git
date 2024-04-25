from Dice import Dice
from Player import Player
from DiceHand import DiceHand
from Histogram import Histogram
from Intelligence import Intelligence
from HighScores import HighScores


class Game:

    def __init__(self):
        self.dice = Dice()
        self.players = self.setup_players()
        self.current_player_index = 0
        self.high_scores = HighScores()
        self.histogram = Histogram()
        self.ai = None

    def setup_players(self):
        players = []
        number_of_players = int(
            input(
                "Enter the number of human players (1 fr single player, 2 or more for multiplayer): "
            )
        )
        for i in range(number_of_players):
            name = input(f"Enter player {i + 1} name: ")
            players.append(Player(name))

        if number_of_players == 1:
            include_computer = (
                input("Do you want to include a computer opponent? (y/n): ")
                .strip()
                .lower()
                == "y"
            )
            if include_computer:
                ai_difficulty = (
                    input("Select AI difficulty (easy, medium, hard): ").strip().lower()
                )
                self.ai = Intelligence(level=ai_difficulty)
                players.append(Player("Computer"))

        return players

    def play_turn(self, player):
        turn_score = 0
        dice_hand = DiceHand()

        while True:
            roll = self.dice.roll()
            dice_hand.add_roll(roll)
            self.histogram.add(roll)

            print(f"{player.name} rolled a {roll}")
            if roll == 1:
                print("Oops! Rolled a 1. No points this.")
                break
            else:
                turn_score += roll
                print(
                    f"Turn score: {turn_score}, Total score if held: {player.score + turn_score}"
                )

                if player.name == "Computer" and self.ai:
                    if not self.ai.should_roll_again(player.score, turn_score):
                        print("Computer decides to hold.")
                        break
                else:
                    choice = input("Roll again? (y/n): ").strip().lower()
                    if choice != "y":
                        break

        player.update_score(turn_score)

    def play_game(self):
        print("Welcome to the Pig Dice Game!")
        while True:
            current_player = self.players[self.current_player_index]
            print(
                f"\n{current_player.name}'s turn. Current score: {current_player.score}"
            )
            self.play_turn(current_player)

            if current_player.score >= 100:
                print(
                    f"\n{current_player.name} wins with a score of {current_player.score}!"
                )
                self.high_scores.save_score(current_player.name, current_player.score)
                break

            self.current_player_index = (self.current_player_index + 1) % len(
                self.players
            )

        print("\nHigh Scores:")
        self.high_scores.display()

        print("\nDice Roll Histogram:")
        self.histogram.display()


if __name__ == "__main__":
    game = Game()
    game.play_game()
