import random

from pygame.math import Vector2


def create_random_velocity(min_speed, max_speed):
    angle = random.randint(0, 360)
    speed = random.randint(min_speed, max_speed)
    return Vector2(speed, 0).rotate_ip(angle)


def create_random_position(width, height, dist_to_ship, ship_pos):
    while True:
        position = Vector2(random.randint(0, width), random.randint(0, height))
        if position.distance_to(ship_pos) > dist_to_ship:
            return position
