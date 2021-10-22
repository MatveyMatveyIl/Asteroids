import pygame.transform
from pygame.math import Vector2
from asteroids_game.game_object import GameObject
from asteroids_game.bullet import Bullet
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.src.load_sound import load_sound


class PlayerShip(GameObject):
    def __init__(self, position, screen_size, create_bullet):
        super().__init__(load_sprite('player_ship'), position, Vector2(0, -1), screen_size)
        self.shoot_sound = load_sound('fire')
        self.move_sound = load_sound('thrust')
        self.rotate_angle = 5
        self.direction = Vector2(0, -1)
        self.default_direction = Vector2(0, -1)
        self.sign = {True: 1, False: -1}
        self.acceleration = 0.1
        self.bullet_speed = 7
        self.create_bullet = create_bullet
        self.screen_size = screen_size

    def rotate_ship(self, hourly):
        self.direction.rotate_ip(self.rotate_angle * self.sign[hourly])

    def draw(self, sprite):
        angle = self.direction.angle_to(self.default_direction)
        rotated_sprite = pygame.transform.rotozoom(self.sprite, angle, 1.0)
        new_rad = rotated_sprite.get_size()
        sprite.blit(rotated_sprite, self.position - Vector2(new_rad) * 0.5)

    def accelerate(self):
        if abs(self.velocity.x) < 4 and abs(self.velocity.y) < 4:
            self.velocity += self.direction * self.acceleration
            self.move_sound.play()
        else:
            self.velocity = Vector2(self.velocity.x / 1.001, self.velocity.y / 1.001)
            self.move_sound.play()

    def shoot(self):
        bullet_velocity = self.direction * self.bullet_speed + self.velocity
        bullet = Bullet(self.position + Vector2(0, 0), bullet_velocity, self.screen_size)
        self.create_bullet(bullet)
        self.shoot_sound.play()
