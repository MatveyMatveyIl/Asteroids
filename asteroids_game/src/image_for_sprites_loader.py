from pygame.image import load


def load_sprite(name):
    sprite = load(f'assets/sprites/{name}.png')
    return sprite.convert()
