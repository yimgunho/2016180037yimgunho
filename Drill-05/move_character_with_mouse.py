from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 824
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')
hide_cursor()

play = True
frame = 0
now_x, now_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
default_x, default_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
dir_x = 0
mouse_button = 0
stop = 1


def handle_events():
    global play, default_x, default_y, now_x, now_y, dir_x, mouse_button

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            play = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                play = False
        elif event.type == SDL_MOUSEMOTION:
            now_x, now_y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_button += 1
            if default_x < event.x:
                dir_x += 1;
            elif default_x > event.x:
                dir_x -= 1;
            default_x = now_x
            default_y = now_y

        elif event.type == SDL_MOUSEBUTTONUP:
            mouse_button -= 1


while play:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if dir_x >= 0:
        character.clip_draw(100, 100 * 3, 100, 100, default_x, default_y)
    elif dir_x < 0:
        character.clip_draw(100, 100 * 2, 100, 100, default_x, default_y)

    if mouse_button > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, now_x, now_y)
    cursor.draw(now_x + 25, now_y - 26)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)

close_canvas()
