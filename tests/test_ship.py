import pygame
import pytest
from asteroids_game.player_ship import PlayerShip
from pygame.math import Vector2


def test_shipCreation():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    position = Vector2(500, 500)
    screen_size = screen.get_size()
    func = set
    ship = PlayerShip(position, screen_size, func)
    assert ship is not None

def test_ShipShooting():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    position = Vector2(500, 500)
    screen_size = screen.get_size()
    bullets = []
    func = bullets.append
    ship = PlayerShip(position, screen_size, func)
    ship.shoot()
    assert len(bullets) != 0