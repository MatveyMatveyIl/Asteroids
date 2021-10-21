from pygame.math import Vector2
from pygame.transform import rotozoom
from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.src.create_random_way import create_random_velocity


class Asteroid(GameObject):
    def __init__(self, position, screen_size, asteroids_size):
        size_to_scale = {
            'big': 1.5,
            'medium': 1,
            'small': 0.5
        }
        scale = size_to_scale[asteroids_size]
        sprite = rotozoom(load_sprite('2'), 0, scale)
        super().__init__(sprite, position, create_random_velocity(1, 3), screen_size)
