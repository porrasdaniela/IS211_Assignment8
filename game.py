from player import HumanPlayer


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    def switch_turns(self):
        self.turn = self.player2 if self.turn == self.player1 else self.player1

    def play_turn(self):
        print(f"{self.turn.name}'s turn!")
        current_turn_score = 0

        while True:
            if isinstance(self.turn, HumanPlayer):
                action = input("Do you want to 'roll' or 'hold'? ").strip().lower()
            else:
                action = self.turn.decide()
                print(f"DEBUG: Computer {self.turn.name} decides to {action}.")

            if action == 'roll':
                roll= self.turn.roll_die()
                print(f"{self.turn.name} rolled a {roll}.")
                if roll == 1:
                    print(f"{self.turn.name} loses all points this turn!")
                    current_turn_score = 0
                    break
                else:
                    current_turn_score += roll
                    print(f"{self.turn.name} now has {self.turn.score + current_turn_score} points (this turn: {current_turn_score}).")
            elif action == 'hold':
                self.turn.score += current_turn_score
                print(f"{self.turn.name} holds. Total score is now {self.turn.score}.")
                break
        self.switch_turns()

        if not self.is_game_over():
            self.play_turn()

    def is_game_over(self):
        return self.player1.score >= 100 or self.player2.score >= 100

    def display_winner(self):
        if self.player1.score >= 100:
            print(f"{self.player1.name} wins with {self.player1.score} points!")
        elif self.player2.score >= 100:
            print(f"{self.player2.name} wins with {self.player2.score} points!")
