import pygame
import pytest
from asteroids_game.player_ship import PlayerShip
from pygame.math import Vector2
from asteroids_game.game import Game
from asteroids_game.asteroid import Asteroid
from asteroids_game.bullet import Bullet


def test_collide_asteroids_with_ship():
    game = Game("level_1")
    screen = pygame.display.set_mode((1200, 800))
    func = []
    game.player_ship = PlayerShip(Vector2(10, 10), screen.get_size(), func.append)
    game.asteroids.append(Asteroid(Vector2(10, 10), screen.get_size(), 3, func.append))
    game._check_ship_and_asteroid_collisions()
    assert (2 == game.lives)


def test_collide_bullet_with_asteroid():
    game = Game("level_1")
    asteroids = len(game.asteroids)
    screen = pygame.display.set_mode((1200, 800))
    func = []
    game.bullets.append(Bullet(Vector2(10, 10), Vector2(0, 0), screen.get_size()))
    game.asteroids.append(Asteroid(Vector2(10, 10), screen.get_size(), 1, func.append))
    game._check_bullet_and_asteroid_collisions()
    assert (asteroids == len(game.asteroids))


def test_create_new_level():
    game = Game("level_1")
    game.win = False
    game.asteroids.clear()
    game._decide_win()
    assert ('level_2' == game.current_level)


def test_delete_bullet():
    game = Game("level_1")
    screen = pygame.display.set_mode((1200, 800))
    game.bullets.append(Bullet(Vector2(10, 10), Vector2(0, 0), screen.get_size()))
    game.bullets.append(Bullet(Vector2(11, 11), Vector2(0, 0), screen.get_size()))
    game.bullets.append(Bullet(Vector2(1300, 900), Vector2(0, 0), screen.get_size()))
    game._delete_bullets_out_of_screen()
    assert (len(game.bullets) == 2)


def test_create_asteroids():
    game = Game("level_1")
    assert (len(game.asteroids) == 3)


def test_create_moving_object():
    game = Game("level_1")
    obj = game._get_all_moving_obg()
    assert (len(obj) == 4)