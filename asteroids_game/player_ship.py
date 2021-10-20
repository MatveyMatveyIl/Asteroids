import pygame.transform
from pygame.math import Vector2
from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite


class PlayerShip(GameObject):

    def __init__(self, position, screen_size):
        super().__init__(load_sprite('player_ship'), position, Vector2(0, 0))
        self.rotate_angle = 5
        self.direction = Vector2(0, -1)
        self.default_direction = Vector2(0, -1)
        self.sign = {True: 1, False: -1}
        self.acceleration = 0.1
        self.screen_size = screen_size

    def rotate_ship(self, hourly):
        self.direction.rotate_ip(self.rotate_angle * self.sign[hourly])

    def draw(self, sprite):
        angle = self.direction.angle_to(self.default_direction)
        rotated_sprite = pygame.transform.rotozoom(self.sprite, angle, 1.0)
        new_rad = rotated_sprite.get_size()
        sprite.blit(rotated_sprite, self.position - Vector2(new_rad) * 0.5)

    def accelerate(self):
        if abs(self.velocity.x) < 5 and abs(self.velocity.y) < 5:
            self.velocity += self.direction * self.acceleration
        else:
            self.velocity = Vector2(self.velocity.x / 1.001, self.velocity.y / 1.001)

    def move(self):
        self.position += self.velocity
        if self.position.x < 0:
            self.position.x = self.screen_size[0]
        elif self.position.x > self.screen_size[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = self.screen_size[1]
        elif self.position.y > self.screen_size[1]:
            self.position.y = 0
