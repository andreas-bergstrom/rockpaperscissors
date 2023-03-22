import random


class Choice:
    def __init__(self, name, defeats):
        self.name = name
        self.defeats = defeats

    def __str__(self):
        return self.name

    def wins_against(self, other):
        return other.name in self.defeats


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose(self, choices):
        print(f"{self.name}, choose your weapon:")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        choice_num = int(input("Enter your choice (1-3): "))
        return choices[choice_num - 1]

    def increase_score(self):
        self.score += 1

    def __str__(self):
        return f"{self.name} ({self.score})"


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer")

    def choose(self, choices):
        choice = random.choice(choices)
        return choice
