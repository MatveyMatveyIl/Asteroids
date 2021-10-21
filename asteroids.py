from asteroids_game.game import Game


def run_game():
    game = Game('level_1')
    game.game_loop()


if __name__ == '__main__':
    run_game()
