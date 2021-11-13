from pygame.image import load
import os


def load_sprite(name):
    path = os.path.abspath(f'assets/sprites/{name}.png')
    sprite = load(path)
    return sprite.convert_alpha()
