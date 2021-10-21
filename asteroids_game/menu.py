import pygame.locals
from asteroids_game.game import *
import sys


def _init_pygame_menu():
    pygame.init()
    pygame.display.set_caption("Asteroids game")


class Menu:
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
                if text == 'Start':
                    game = Game()
                    game.game_loop()
                if text == 'Level':
                    level = Level()
                    level.level_loop()
                if text == 'New Game':
                    game = Game()
                    game.game_loop()
                if text == 'Exit':
                    pygame.quit()
                    quit()
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, w, h))
        self.screen.blit(text_obj, (x, y))

    def menu_loop(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.button(400, 200, 400, 50, 'Start')
            self.button(400, 300, 400, 50, 'Level')
            self.button(400, 400, 400, 50, 'New Game')
            self.button(400, 500, 400, 50, 'Exit')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


class Level:
    def __init__(self):
        _init_pygame_menu()
        self.screen = pygame.display.set_mode((800, 800))
        self.screen_size = self.screen.get_size()
        self.background = load_sprite('space_bg')
        self.menu_front = pygame.font.Font('freesansbold.ttf', 39)

    def button(self, x, y, w, h, text):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_obj = self.menu_front.render(text, True, (255, 164, 189))
        if x < pos[0] < x + w and y < pos[1] < y + h:
            if click[0] == 1:
                print(text)
                if text == 'Level 1':
                    game = Game()
                    game.game_loop()
                if text == 'Level 2':
                    game = Game()
                    game.game_loop()
                if text == 'Level 3':
                    game = Game()
                    game.game_loop()
                if text == 'Level 4':
                    game = Game()
                    game.game_loop()
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, w, h))
        self.screen.blit(text_obj, (x, y))

    def level_loop(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.button(200, 200, 400, 50, 'Level 1')
            self.button(200, 300, 400, 50, 'Level 2')
            self.button(200, 400, 400, 50, 'Level 3')
            self.button(200, 500, 400, 50, 'Level 4')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()