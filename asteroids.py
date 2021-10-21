from asteroids_game.game import Game
from asteroids_game.menu import Menu


def run_game():
    game = Menu()
    game.menu_loop()


if __name__ == '__main__':
    run_game()
