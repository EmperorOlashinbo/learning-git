class Histogram:
    def __init__(self):
        self.data = {}

    def add(self, roll):
        self.data[roll] = self.data.get(roll, 0) + 1

    def display(self):
        for roll in sorted(self.data):
            print(f"{roll}: {'*' * self.data[roll]}")
