import pytest
from asteroids_game.player_ship import PlayerShip
from pygame.math import Vector2


def test_shipCreation():
    position = Vector2(500, 500)
    screen_size = [1200, 800]
    func = screen_size.append
    ship = PlayerShip(position, screen_size, func)
    assert ship is not None
