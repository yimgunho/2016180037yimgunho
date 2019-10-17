from pico2d import *
import random

WIDTH = 700
HEIGHT = 840
open_canvas(WIDTH, HEIGHT)
character = load_image('cha.png')
background = load_image('background.jpg')

running = True
ctrl_check = False
same_check = True

character_frame = 0
background_frame = random.randint(0, 9)

background_first = HEIGHT // 2
background_second = HEIGHT // 2 + HEIGHT


def handle_events():
    global running, background_frame, ctrl_check, same_check
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
                        if background_frame != back_f:
                            background_frame = back_f
                            same_check = False
                    same_check = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LCTRL:
                ctrl_check = False


while running:
    clear_canvas()
    background.clip_draw(720 * background_frame, 0, 720, 1280, WIDTH // 2, background_first, WIDTH, HEIGHT)
    background.clip_draw(720 * background_frame, 0, 720, 1280, WIDTH // 2, background_second, WIDTH, HEIGHT)

    character.clip_draw(128 * character_frame, 0, 128, 128, 350, 100)
    character_frame = (character_frame + 1) % 6
    if background_first <= -(HEIGHT // 2):
        background_first = HEIGHT // 2 + HEIGHT
    elif background_second <= -(HEIGHT // 2):
        background_second = HEIGHT // 2 + HEIGHT

    background_first -= 10
    background_second -= 10

    update_canvas()
    delay(0.02)
    handle_events()

close_canvas()
