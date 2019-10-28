from pico2d import *
import random

WIDTH = 700
HEIGHT = 840


class Background:

    def __init__(self):
        self.image = load_image('background.jpg')
        self.frame = random.randint(0, 9)
        self.first = HEIGHT // 2
        self.second = HEIGHT // 2 + HEIGHT

    def update(self):
        if self.first <= -(HEIGHT // 2):
            self.first = HEIGHT // 2 + HEIGHT
        elif self.second <= -(HEIGHT // 2):
            self.second = HEIGHT // 2 + HEIGHT

        self.first -= 10
        self.second -= 10

    def draw(self):
        self.image.clip_draw(720 * self.frame, 0, 720, 1280, WIDTH // 2, self.first, WIDTH, HEIGHT)
        self.image.clip_draw(720 * self.frame, 0, 720, 1280, WIDTH // 2, self.second, WIDTH, HEIGHT)


class Character:

    def __init__(self):
        self.image = load_image('cha.png')
        self.frame = 0
        self.x = 350
        self.y = 100
        self.change_x = 0
        self.speed = 10

    def update(self):
        if 65 <= self.x and self.change_x < 0:
            self.x += self.change_x
        elif self.x <= 635 and self.change_x > 0:
            self.x += self.change_x
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(128 * self.frame, 0, 128, 128, self.x, self.y, 140, 140)


class Bullet:

    def __init__(self):
        self.image = load_image('bullet.png')
        self.x = None
        self.y = 100
        self.speed = 10

    def update(self):
        self.y += self.speed
        if self.y > 900:
            self.y = -100
        if self.y == 150:
            self.x = None

    def draw(self):
        if 900 >= self.y >= 150:
            self.image.draw(self.x, self.y, 105, 105)


class Dragon:

    def __init__(self):
        self.image = load_image('green_dragon.png')
        self.frame = 0
        self.x = 350
        self.y = 1000
        self.hit = 0

    def update(self):
        if self.y <= -70:
            self.y = 1000
            self.hit = 0

        self.y -= 10
        self.frame = (self.frame + 1) % 9

    def draw(self):
        if self.hit == 0:
            self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y, 130, 130)
