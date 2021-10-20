from pygame.math import Vector2
from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite


class Asteroid(GameObject):
    def __init__(self, position):
        super().__init__(load_sprite(''), position, Vector2(0, 0))

