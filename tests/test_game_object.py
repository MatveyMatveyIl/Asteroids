import pygame
import os
from pygame.math import Vector2
from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite

try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    os.environ['SDL_AUDIODRIVER'] = 'dsp'


def test_game_object_move():
    pygame.init()
    pygame.mixer.init()
    pygame.display.list_modes()
    screen = pygame.display.set_mode((1200, 800))
    sprite = load_sprite("player_ship")
    game_object = GameObject(sprite, Vector2(1, 1), Vector2(1, 1), screen.get_size())
    game_object.move()
    assert Vector2(2, 2) == game_object.position


def test_game_object_deceleration():
    pygame.init()
    pygame.display.list_modes()
    screen = pygame.display.set_mode((1200, 800))
    sprite = load_sprite("player_ship")
    game_object = GameObject(sprite, Vector2(1, 1), Vector2(1, 1), screen.get_size())
    game_object.deceleration()
    assert Vector2(1.5, 1.5) == game_object.position
