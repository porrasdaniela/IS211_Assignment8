import time

from game import Game

class TimedGameProxy(Game):
    def __init__(self, player1, player2, time_limit=60):
        super().__init__(player1, player2)
        self.time_limit = time_limit
        self.start_time = time.time()

    def play_turn(self):
        current_time = time.time()
        if current_time - self.start_time > self.time_limit:
            print("Time is up!")
            self.determine_winner()
            return False

        super().play_turn()
        return True

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins with {self.player1.score} points!")
        elif self.player2.score > self.player1.score:
            print(f"{self.player2.name} wins with {self.player2.score} points!")
        else:
            print("The game is a tie!")