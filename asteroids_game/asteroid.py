import random
from pygame.math import Vector2
from pygame.transform import rotozoom
from asteroids_game.game_object import GameObject
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.src.load_sound import load_sound
from asteroids_game.src.create_random_way import create_random_velocity


class Asteroid(GameObject):
    def __init__(self, position, screen_size, asteroid_size, destruction_action):
        self.destruction_sound_small = load_sound('bangSmall')
        self.destruction_sound_medium = load_sound('bangMedium')
        self.destruction_sound_big = load_sound('bangLarge')
        self.asteroid_size = asteroid_size
        self.destruction_action = destruction_action
        self.screen_size = screen_size
        size_to_scale = {
            3: 1.5,
            2: 1,
            1: 0.5
        }
        scale = size_to_scale[self.asteroid_size]
        random_img = random.randint(1, 3)
        all_img = {
            1: 'asteroid1',
            2: 'asteroid2',
            3: 'asteroid3',
        }
        sprite = rotozoom(load_sprite(all_img[random_img]), random.randint(0, 90), scale)
        super().__init__(sprite, position, create_random_velocity(1, 4), screen_size)

    def fault_asteroid(self, score):
        if self.asteroid_size > 1:
            if self.asteroid_size == 3:
                score.update_score('big')
                self.destruction_sound_big.play()
            else:
                score.update_score('medium')
                self.destruction_sound_medium.play()
            for _ in range(random.randint(2, 3)):
                self.destruction_action(
                    Asteroid(self.position + Vector2(0, 0), self.screen_size, self.asteroid_size - 1,
                             self.destruction_action))
        else:
            score.update_score('small')
            self.destruction_sound_small.play()
