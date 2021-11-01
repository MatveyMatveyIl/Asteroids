import math
import unittest
from asteroids_game.asteroid import Asteroid
from asteroids_game.game import Game
from asteroids_game.game import PlayerShip
from asteroids_game.game_object import GameObject
from asteroids_game.bullet import Bullet
from pygame.math import Vector2
import pygame
from asteroids_game.src.image_for_sprites_loader import load_sprite
import os
import sys

#
# class TestPlayerShip(unittest.TestCase):
#
#     def test_rotate_left_ship(self):
#         pygame.init()
#         screen = pygame.display.set_mode((1200, 800))
#         bullet = []
#         ship = PlayerShip(Vector2(0, 0), screen.get_size(), bullet.append)
#         ship.rotate_ship(hourly=False)
#         self.assertEqual(0, ship.position)
#


class TestGameObject(unittest.TestCase):

    def test_move(self):
        pygame.init()
        screen = pygame.display.set_mode((1200, 800))
        sprite = (pygame.image.load('C:/Users/Администратор/OneDrive/Рабочий стол/Asteroids/assets/sprites/player_ship.png')).convert_alpha()
        game_object = GameObject(sprite, Vector2(1, 1), Vector2(1, 1), screen.get_size())
        game_object.move()
        self.assertEqual((2, 2), game_object.position)

    def test_deceleration(self):
        pygame.init()
        screen = pygame.display.set_mode((1200, 800))
        sprite = (pygame.image.load(
            'C:/Users/Администратор/OneDrive/Рабочий стол/Asteroids/assets/sprites/player_ship.png')).convert_alpha()
        game_object = GameObject(sprite, Vector2(1, 1), Vector2(1, 1), screen.get_size())
        game_object.deceleration()
        self.assertEqual((1, 1), game_object.position)



class TestGameLogic(unittest.TestCase):

    def test_collide_asteroids_with_ship(self):
        game = Game("leve_1")
        pygame.init()
        screen = pygame.display.set_mode((1200, 800))
        asteroids = []
        game.asteroids = Asteroid(Vector2(0, 0), screen.get_size(), 3, asteroids.append)
        bullet = []
        game.player_ship = PlayerShip(Vector2(0, 0), screen.get_size(), bullet.append)
        game._check_ship_and_asteroid_collisions()
        self.assertEqual(2, game.lives)

