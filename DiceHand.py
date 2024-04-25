class DiceHand:
    def __init__(self):
        self.rolls = []

    def add_roll(self, roll):
        self.rolls.append(roll)

    def total(self):
        return sum(self.rolls)

    def reset(self):
        self.rolls = []
