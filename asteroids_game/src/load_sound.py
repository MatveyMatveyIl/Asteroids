from pygame.mixer import Sound


def load_sound(name):
    return Sound(f'assets/sounds/{name}.wav')