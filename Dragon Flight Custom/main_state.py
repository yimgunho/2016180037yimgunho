import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
from fuction_state import Background

name = "MainState"

background = None



def enter():
    global background
    background = Background()


def exit():
    global background
    del background


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)



def update():
    background.update()



def draw():
    clear_canvas()
    background.draw()
    delay(0.01)
    update_canvas()
