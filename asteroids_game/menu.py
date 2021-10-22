import pygame.locals
from asteroids_game.game import Game
from asteroids_game.src.image_for_sprites_loader import load_sprite


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
        pygame.mouse.set_visible(True)
        click = pygame.mouse.get_pressed()
        text_obj = self.menu_front.render(text, True, (255, 255, 255))
        if x < pos[0] < x + w and y < pos[1] < y + h:
            pygame.draw.rect(self.screen, (80, 80, 80), (x, y, w, h))
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
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(self.screen, False, (x, y, w, h))
        self.screen.blit(text_obj, (x + w / 2 - len(text) * 15, y))

    def menu_loop(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.button(450, 200, 300, 50, 'Start')
            self.button(450, 300, 300, 50, 'Level')
            self.button(440, 400, 330, 50, 'New Game')
            self.button(450, 500, 300, 50, 'Exit')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()


class Level:
    def __init__(self):
        _init_pygame_menu()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_size = self.screen.get_size()
        self.background = load_sprite('menu_bg')
        self.menu_front = pygame.font.Font(f'assets/font/ARCADECLASSIC.TTF', 38)
        self.running = True

    def button(self, x, y, w, h, text):
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(True)
        click = pygame.mouse.get_pressed()
        text_obj = self.menu_front.render(text, True, (255, 255, 255))
        if x < pos[0] < x + w and y < pos[1] < y + h:
            pygame.draw.rect(self.screen, (80, 80, 80), (x, y, w, h))
            if click[0] == 1:
                text = text.replace(' ', '_')
                game = Game(text)
                game.game_loop()
        else:
            pygame.draw.rect(self.screen, False, (x, y, w, h))
        self.screen.blit(text_obj, (x + w / 2 - len(text) * 15, y))

    def level_loop(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for i in range(1, 11):
                self.button(50, i * 70, 400, 40, f'level {i}')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
            pygame.display.update()
