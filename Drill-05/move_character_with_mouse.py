from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 824

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

play = True
frame = 0


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
    character.clip_draw(frame * 100, 100 * 1, 100, 100, 500, 500)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)

close_canvas()
