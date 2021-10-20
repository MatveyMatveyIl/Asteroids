import pygame
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.game_object import GameObject


class Game:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((1200, 800))
        self.background = load_sprite('space_bg')
        self.fps = pygame.time.Clock()

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

    def _process_game_logic(self):
        pass

    def _draw_game(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        self.fps.tick(60)
