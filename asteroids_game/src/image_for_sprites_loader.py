from pygame.image import load
import os


def load_sprite(name):
    sprite = load(os.path.join('assets/sprites/', f'{name}.png'))
    return sprite.convert_alpha()
