import pygame.mixer
from pygame.mixer import Sound
import os


def load_sound(name):
    pygame.mixer.init()
    path = os.path.abspath(f'assets/sounds/{name}.wav')
    return Sound(path)
