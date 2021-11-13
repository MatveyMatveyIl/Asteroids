from pygame.mixer import Sound
import os


def load_sound(name):
    path = os.path.abspath(f'assets/sounds/{name}.wav')
    return Sound(path)
