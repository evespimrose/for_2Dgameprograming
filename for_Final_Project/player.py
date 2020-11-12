import random
from pico2d import *
import gfw
from gobj import *


class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT): -1,
        (SDL_KEYDOWN, SDLK_RIGHT): 1,
        (SDL_KEYUP, SDLK_LEFT): 1,
        (SDL_KEYUP, SDLK_RIGHT): -1,
        (SDL_KEYDOWN, SDLK_DOWN): -1,
        (SDL_KEYDOWN, SDLK_UP): 1,
        (SDL_KEYUP, SDLK_DOWN): 1,
        (SDL_KEYUP, SDLK_UP): -1,
    }
    KEY_DOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    def __init__(self, rand_pos=False):
        if rand_pos:
            self.pos = (200, 200)
            self.action = random.randint(0, 3)
        else:
            self.pos = get_canvas_width() // 2, get_canvas_height() // 2
            self.action = 3
        self.data = 0, 0
        self.fidx = random.randint(0, 7)
        self.target = None
        self.targets = []
        self.speed = 0
        if Player.image is None:
            Player.image = gfw.iamge.load(RES_DIR + '/player.png')

    def draw(self):
        sx = self.fidx * 100
        sy = self.action * 100
        self.image.clip_draw(sx, sy, 100, 100, *self.pos)

    def update(self):
        self.x += self.dx * self.speed * gfw.delta_time

