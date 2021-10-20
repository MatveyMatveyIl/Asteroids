from pygame.math import Vector2
from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.src.create_random_way import create_random_velocity


class Asteroid(GameObject):
    def __init__(self, position, screen_size):
        super().__init__(load_sprite('2'), position, create_random_velocity(1, 4), screen_size)
