import pygame
import os
from asteroids_game.asteroid import Asteroid
from asteroids_game.score import Score
from pygame.math import Vector2

try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"


def test_asteroidCreation():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    position = Vector2(500, 500)
    screen_size = screen.get_size()
    asteroids = []
    func = asteroids.append
    asteroid = Asteroid(position, screen_size, 3, func)
    assert asteroid is not None


def test_asteroidMove():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    position = Vector2(500, 500)
    screen_size = screen.get_size()
    asteroids = []
    func = asteroids.append
    asteroid = Asteroid(position, screen_size, 3, func)
    for i in range(10):
        asteroid.move()
    assert asteroid.position != Vector2(500, 500)


def test_asteroidFault():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    position = Vector2(500, 500)
    screen_size = screen.get_size()
    asteroids = []
    func = asteroids.append
    asteroid = Asteroid(position, screen_size, 3, func)
    score = Score()
    asteroid.fault_asteroid(score)
    assert len(asteroids) != 0
