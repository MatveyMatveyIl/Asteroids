import pygame
from pygame.math import Vector2
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.src.load_levels import load_levels
from asteroids_game.player_ship import PlayerShip
from asteroids_game.asteroid import Asteroid


class Game:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((1200, 800))
        self.background = load_sprite('space_bg')
        self.fps = pygame.time.Clock()
        self.player_ship = PlayerShip(Vector2(600, 400), self.screen.get_size())
        self.levels = load_levels()
        self.asteroids = []

    def game_loop(self):
        while True:
            self._process_input()
            self._process_game_logic()
            self._draw_game()

    def _init_pygame(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Asteroids game")

    def _process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_BACKSPACE:
                quit()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player_ship.rotate_ship(hourly=True)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player_ship.rotate_ship(hourly=False)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.player_ship.accelerate()

    def _process_game_logic(self):
        for game_obj in self._get_all_moving_obg():
            game_obj.move()

    def _draw_game(self):
        self.screen.blit(self.background, (0, 0))
        for game_obg in self._get_all_moving_obg():
            game_obg.draw(self.screen)
        pygame.display.flip()
        self.fps.tick(60)

    def _get_all_moving_obg(self):
        return [self.player_ship, *self.asteroids]
