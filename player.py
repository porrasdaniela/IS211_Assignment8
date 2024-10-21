import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def reset_score(self):
        self.score = 0

    def roll_die(self):
        return random.randint(1, 6)

    def hold(self):
        pass

class HumanPlayer(Player):
    def hold(self):
        print(f"{self.name} holds with a score of {self.score}.")

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def roll_die(self):
        return random.randint(1,6)

    def decide(self):
        # Computer strategy: roll until score is 25 or greater
        if self.score >= 25:
            return 'hold'
        return 'roll'

    def hold(self):
        print(f"Computer {self.name} holds with a score of {self.score}.")

