class Intelligence:
    def __init__(self, level="medium"):
        self.level = level

    def should_roll_again(self, current_score, turn_score):
        if self.level == "easy":
            return turn_score < 15
        elif self.level == "medium":
            return turn_score < 20 or current_score + turn_score < 100
        else:
            risk_threshold = 25 if current_score + turn_score < 70 else 15
            return turn_score < risk_threshold
