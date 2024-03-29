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
        self.x = character.x
        self.y = 100
        self.speed = 10

    def update(self):
        self.y += self.speed
        if self.y > 900:
            self.y = -100
        if self.y == 150:
            self.x = character.x

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


open_canvas(WIDTH, HEIGHT)

character = Character()
background = Background()

bullet = [Bullet() for m in range(20)]
count = 1
for bul in bullet:
    bul.y = 150 - 50 * count
    count += 1

dragon = [Dragon() for n in range(5)]
count = 1
for monster in dragon:
    monster.x = count * 140 - 70
    count += 1

running = True
ctrl_check = False
same_check = True


def handle_events():
    global running, background, ctrl_check, same_check, character
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LCTRL:
                ctrl_check = True
            elif event.key == SDLK_1:
                if ctrl_check:
                    while same_check:
                        back_f = random.randint(0, 9)
                        if background.frame != back_f:
                            background.frame = back_f
                            same_check = False
                    same_check = True
            elif event.key == SDLK_LEFT:
                character.change_x -= character.speed
            elif event.key == SDLK_RIGHT:
                character.change_x += character.speed

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LCTRL:
                ctrl_check = False
            elif event.key == SDLK_LEFT:
                character.change_x += character.speed
            elif event.key == SDLK_RIGHT:
                character.change_x -= character.speed


while running:
    clear_canvas()

    background.update()
    background.draw()

    for monster in dragon:
        monster.update()
        for bul in bullet:
            if monster.x - 110 < bul.x < monster.x + 110 and monster.y - 110 < bul.y < monster.y + 110:
                monster.hit = 1
        monster.draw()

    for bul in bullet:
        bul.update()
        bul.draw()

    character.update()
    character.draw()

    update_canvas()
    delay(0.02)
    handle_events()

close_canvas()
