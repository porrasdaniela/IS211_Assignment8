import argparse
from player_factory import PlayerFactory
from game import Game
from timed_game_proxy import TimedGameProxy

def main():
    parser = argparse.ArgumentParser(description="Play the game of Pig.")
    parser.add_argument('--player1', choices=['human', 'computer'], required=True, help="Type of Player 1")
    parser.add_argument('--player2', choices=['human', 'computer'], required=True, help="Type of Player 2")
    parser.add_argument('--timed', action='store_true', help="Enable timed mode")

    args = parser.parse_args()

    # Create players
    player1 = PlayerFactory.create_player(args.player1, "Player 1")
    player2 = PlayerFactory.create_player(args.player2, "Player 2")

    # Start game
    if args.timed:
        game = TimedGameProxy(player1, player2)
    else:
        game = Game(player1, player2)

    while not game.is_game_over():
        if not game.play_turn():
            break

    game.display_winner()

if __name__ == "__main__":
    main()