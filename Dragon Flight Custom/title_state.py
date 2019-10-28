import game_framework
from pico2d import *
import main_state


name = "TitleState"
background = None
character = None
name = None
start = None
feeling = None
custom = None
orange = None


def enter():
    global character, background, name, start, feeling, custom, orange
    background = load_image('title_background.png')
    character = load_image('title_character.png')
    name = load_image('title_name.png')
    start = load_image('title_start.png')
    feeling = load_image('title_feeling.png')
    custom = load_image('custom.png')
    orange = load_image('orange.png')


def exit():
    global character, background, name, start, feeling, custom, orange
    del character, background, name, start, feeling, custom, orange


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    background.draw(350, 420)
    character.draw(600, 400, 150, 300)
    start.draw(350, 200, 700, 150)
    name.draw(350, 620, 500, 300)
    orange.draw(400, 480, 250, 80)
    custom.draw(400, 480, 300, 80)
    feeling.draw(350, 420, 700, 840)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
