from pico2d import *


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