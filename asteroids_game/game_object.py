from pygame.math import Vector2
import pygame


class GameObject:
    def __init__(self, sprite, position: Vector2, velocity: Vector2, screen_size):
        self.sprite = sprite
        self.position = position
        self.velocity = velocity
        self.radius = sprite.get_width() / 2
        self.screen_size = screen_size
        self.fps = pygame.time.get_ticks() + 70

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

    def deceleration(self):
        for i in range(70, 0, -1):
            if pygame.time.get_ticks() >= self.fps:
                self.fps = pygame.time.get_ticks() + i
                self.move()

    def collision(self, other_object):
        dist = self.position.distance_to(other_object.position)
        return dist < self.radius + other_object.radius

    def draw(self, sprite):
        sprite.blit(self.sprite, self.position - Vector2(self.radius))
