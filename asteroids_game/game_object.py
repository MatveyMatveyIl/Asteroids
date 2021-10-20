from pygame.math import Vector2


class GameObject:
    def __init__(self, sprite, position: Vector2, velocity: Vector2):
        self.sprite = sprite
        self.position = position
        self.velocity = velocity
        self.radius = sprite.get_width() / 2

    def move(self):
        self.position += self.velocity

    def collision(self, other_object):
        dist = self.position.distance_to(other_object.position)
        return dist < self.radius + other_object.radius

    def draw(self, sprite):
        sprite.blit(self.sprite, self.position - Vector2(self.radius))
