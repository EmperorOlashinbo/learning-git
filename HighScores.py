import json
import os


class HighScores:
    def __init__(self, filename="highscores11.json"):
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_score(self, name, score):
        self.scores[name] = max(score, self.scores.get(name, 0))
        with open(self.filename, "w") as file:
            json.dump(self.scores, file)

    def display(self):
        for name, score in sorted(
            self.scores.items(), key=lambda item: item[1], reverse=True
        ):
            print(f"{name}: {score}")
