import pygame
from pygame.math import Vector2
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.player_ship import PlayerShip


class Game:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((1200, 800))
        self.background = load_sprite('space_bg')
        self.fps = pygame.time.Clock()
        self.player_ship = PlayerShip(Vector2(600, 400), self.screen.get_size())

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
            self.player_ship.rotate_ship(True)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player_ship.rotate_ship(False)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.player_ship.accelerate()

    def _process_game_logic(self):
        self.player_ship.move()

    def _draw_game(self):
        self.screen.blit(self.background, (0, 0))
        self.player_ship.draw(self.screen)
        pygame.display.flip()
        self.fps.tick(60)
