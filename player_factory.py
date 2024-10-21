from player import HumanPlayer, ComputerPlayer

class PlayerFactory:
    @staticmethod
    def create_player(player_type, name):
        if player_type == 'human':
            return HumanPlayer(name)
        elif player_type == 'computer':
            return ComputerPlayer("Computer")
        else:
            raise ValueError("Invalid player type")