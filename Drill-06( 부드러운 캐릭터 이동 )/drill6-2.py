from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 824
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hide_cursor()

play = True
frame = 0
dir_x = 0
size = 10
pick = [(random.randint(21, 1259), random.randint(40, 78)) for i in range(size)]
now_x, now_y = pick[0]


def handle_events():
    global play

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            play = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                play = False


while play:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if dir_x >= 0:
        character.clip_draw(100 * frame, 100 * 1, 100, 100, now_x, now_y)
    elif dir_x < 0:
        character.clip_draw(100 * frame, 100 * 0, 100, 100, now_x, now_y)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)

close_canvas()
