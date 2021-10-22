import random

import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom
from asteroids_game.src.image_for_sprites_loader import load_sprite
from asteroids_game.src.load_levels import load_levels
from asteroids_game.src.create_random_way import create_random_position
from asteroids_game.player_ship import PlayerShip
from asteroids_game.asteroid import Asteroid
from asteroids_game.score import Score


class Game:
    def __init__(self, level):
        self._init_pygame()
        self.current_level = level
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_size = self.screen.get_size()
        self.background = load_sprite('space_bg')
        self.fps = pygame.time.Clock()
        self.bullets = []
        self.player_ship = PlayerShip(Vector2(600, 400), self.screen_size, self.bullets.append)
        self.levels = load_levels()
        self.asteroids = []
        self.lives = 3
        self.score = Score()

    def game_loop(self):
        self._create_asteroids()
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
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game = Game(self.current_level)
                game.game_loop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # menu
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.player_ship:
                self.player_ship.shoot()

        pressed_key = pygame.key.get_pressed()
        if self.player_ship:
            if pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]:
                self.player_ship.rotate_ship(hourly=True)
            if pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]:
                self.player_ship.rotate_ship(hourly=False)
            if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
                self.player_ship.accelerate()

    def _process_game_logic(self):
        for game_obj in self._get_all_moving_obg():
            game_obj.move()
        self._check_bullet_and_asteroid_collisions()
        self._check_ship_and_asteroid_collisions()
        self._delete_bullets_out_of_screen()

    def _draw_game(self):
        self.screen.blit(self.background, (0, 0))
        for game_obg in self._get_all_moving_obg():
            game_obg.draw(self.screen)
        self._draw_lives()
        self._draw_score()
        pygame.display.flip()
        self.fps.tick(60)

    def _draw_lives(self):
        for i in range(self.lives):
            img = rotozoom(load_sprite('player_ship'), 0, 0.75)
            img_rect = img.get_rect()
            img_rect.x, img_rect.y = self.screen_size[0] - 30 * i - 50, 10
            self.screen.blit(img, img_rect)

    def _draw_score(self):
        font = pygame.font.Font(f'assets/font/ARCADECLASSIC.TTF', 54)
        text = font.render(str(self.score.current_score), False, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x, text_rect.y = 50, 10
        self.screen.blit(text, text_rect)

    def _get_all_moving_obg(self):
        moving_obj = [*self.asteroids, *self.bullets]
        if self.player_ship is not None:
            moving_obj.append(self.player_ship)
        return moving_obj

    def _create_asteroids(self):
        for i, count in enumerate(self.levels[self.current_level]):
            self.asteroids += [Asteroid(create_random_position(
                self.screen.get_width(), self.screen.get_height(), random.randint(250, 350), self.player_ship.position
            ), self.screen_size, 3 - i, self.asteroids.append) for _ in range(count)]

    def _delete_bullets_out_of_screen(self):
        for bullet in self.bullets:
            if bullet.position.x < 0 or bullet.position.x > self.screen_size[0]:
                self.bullets.remove(bullet)
            elif bullet.position.y < 0 or bullet.position.y > self.screen_size[1]:
                self.bullets.remove(bullet)

    def _check_bullet_and_asteroid_collisions(self):
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if asteroid.collision(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.fault_asteroid(self.score)
                    break

    def _check_ship_and_asteroid_collisions(self):
        if self.player_ship is not None:
            for asteroid in self.asteroids:
                if self.player_ship.collision(asteroid):
                    self.asteroids.remove(asteroid)
                    self.lives -= 1
                    break
                if self.lives <= 0:
                    self.player_ship = None
                    break
