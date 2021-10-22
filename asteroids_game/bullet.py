from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite


class Bullet(GameObject):
    def __init__(self, position, velocity, screen_size):
        super().__init__(load_sprite('bullet'), position, velocity, screen_size)

    def move(self):
        self.position += self.velocity
