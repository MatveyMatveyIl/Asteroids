from pygame.math import Vector2


class GameObject:
    def __init__(self, sprite, position: Vector2, velocity: Vector2, screen_size=Vector2(0, 0)):
        self.sprite = sprite
        self.position = position
        self.velocity = velocity
        self.radius = sprite.get_width() / 2
        self.screen_size = screen_size

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

    def collision(self, other_object):
        dist = self.position.distance_to(other_object.position)
        return dist < self.radius + other_object.radius

    def draw(self, sprite):
        sprite.blit(self.sprite, self.position - Vector2(self.radius))
