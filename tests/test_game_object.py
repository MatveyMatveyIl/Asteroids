import pygame
import pytest
from asteroids_game.player_ship import PlayerShip
from pygame.math import Vector2
from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite


def test_game_object_move():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    sprite = load_sprite("player_ship")
    game_object = GameObject(sprite, Vector2(1, 1), Vector2(1, 1), screen.get_size())
    game_object.move()
    assert ((2, 2), game_object.position)


def test_game_object_deceleration():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    sprite = load_sprite("player_ship")
    game_object = GameObject(sprite, Vector2(1, 1), Vector2(1, 1), screen.get_size())
    game_object.deceleration()
    assert ((1, 1), game_object.position)
