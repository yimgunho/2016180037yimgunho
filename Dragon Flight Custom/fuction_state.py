from pico2d import *
import random

WIDTH = 700
HEIGHT = 840


class Background:

    def __init__(self, a):
        self.image = load_image('background.jpg')
        self.frame = a
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
            self.x -= self.speed
        elif self.x <= 635 and self.change_x > 0:
            self.x += self.speed

        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(128 * self.frame, 0, 128, 128, self.x, self.y, 140, 140)


class Bullet:

    def __init__(self, x):
        self.image = load_image('bullet.png')
        self.x = x
        self.y = 100
        self.speed = 10
        self.atk = 20

    def update(self):
        self.y += self.speed

    def draw(self):
        self.image.draw(self.x, self.y, 105, 105)


class Dragon:

    def __init__(self, x):
        self.image = load_image('green_dragon.png')
        self.frame = 0
        self.x = x
        self.y = 1000
        self.hp = 40

    def update(self):
        self.y -= 10
        self.frame = (self.frame + 1) % 9

    def damage(self, atk):
        self.hp -= atk

    def draw(self):
        if self.hp > 0:
            self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y, 130, 130)


class Boom:
    def __init__(self, x, y):
        self.image = load_image('boom.png')
        self.frame = 0
        self.x = x
        self.y = y

    def update(self):
        self.frame = self.frame + 1

    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 140, self.x, self.y)
