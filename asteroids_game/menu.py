import pygame.locals
from asteroids_game.game import Game
from asteroids_game.src.image_for_sprites_loader import load_sprite
import select


def _init_pygame_menu():
    pygame.init()
    pygame.display.set_caption("Asteroids game")


class Menu:
    def __init__(self):
        _init_pygame_menu()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_size = self.screen.get_size()
        self.background = load_sprite('space_bg')
        self.menu_front = pygame.font.Font(f'assets/font/ARCADECLASSIC.TTF', 56)
    def button(self, x, y, w, h, text):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_obj = self.menu_front.render(text, True, (255, 255, 255))
        if x < pos[0] < x + w and y < pos[1] < y + h:
            pygame.draw.rect(self.screen, (80,80,80), (x, y, w, h))
            if click[0] == 1:
                if text == 'Start':
                    game = Game('level_1')
                    game.game_loop()
                if text == 'Level':
                    level = Level()
                    level.level_loop()
                if text == 'New Game':
                    game = Game('level_1')
                    game.game_loop()
                if text == 'Exit':
                    quit()
        else:
            pygame.draw.rect(self.screen, False, (x, y, w, h))
        self.screen.blit(text_obj, (x + w/2 - len(text) * 15, y))

    def menu_loop(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.button(450, 200, 300, 50, 'Start')
            self.button(450, 300, 300, 50, 'Level')
            self.button(440, 400, 330, 50, 'New Game')
            self.button(450, 500, 300, 50, ' Exit')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            pygame.display.update()


class Level:
    def __init__(self):
        _init_pygame_menu()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_size = self.screen.get_size()
        self.background = load_sprite('space_bg')
        self.menu_front = pygame.font.Font('freesansbold.ttf', 39)

    def button(self, x, y, w, h, text):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_obj = self.menu_front.render(text, True, (255, 164, 189))
        if x < pos[0] < x + w and y < pos[1] < y + h:

            if click[0] == 1:
                game = Game(text)
                game.game_loop()
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, w, h))
        self.screen.blit(text_obj, (x, y))

    def level_loop(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.button(200, 200, 400, 50, 'level_1')
            self.button(200, 300, 400, 50, 'level_2')
            self.button(200, 400, 400, 50, 'level_3')
            self.button(200, 500, 400, 50, 'level_4')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            pygame.display.update()
