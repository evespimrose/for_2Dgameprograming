import random
from pico2d import *
import gfw
import math
from gobj import *

MOVE_PPS = 300


class Player:
    image = None

    def __init__(self):
        targets = None
        global image, pos, delta
        pos = get_canvas_width() // 2, get_canvas_height() // 2
        target = None
        targets = []
        delta = 0, 0
        if Player.image is None:
            Player.image = gfw.iamge.load(RES_DIR + '/player.png')

    def draw(self):
        global pos, image
        gfw.image.draw(*pos)

    def update(self):
        global pos, delta_x, delta_y
        x, y = pos
        x += delta_x * MOVE_PPS * gfw.delta_time
        y += delta_y * MOVE_PPS * gfw.delta_time
        hw, hh = image.w // 2, image.h // 2
        x = clamp(hw, x, get_canvas_height() - hw)
        y = clamp(hh, y, get_canvas_width() - hh)

        pos = x, y

    def delta(self, target):
        dx, dy = target[0] - self.pos[0], target[1] - pos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0: return 0, 0
        return dx / distance, dy / distance

    def appendTarget(self, target):
        if target == self.pos: return
        for t in self.targets:
            if t == target: return

        self.delta = (0, 0) if target is None else delta(pos, target)

        self.targets.append(target)

    def handle_event(e):
        global delta_x, delta_y
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                delta_x -= 1
            elif e.key == SDLK_RIGHT:
                delta_x += 1
            if e.key == SDLK_DOWN:
                delta_y -= 1
            elif e.key == SDLK_UP:
                delta_y += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                delta_x += 1
            elif e.key == SDLK_RIGHT:
                delta_x -= 1
            if e.key == SDLK_DOWN:
                delta_y += 1
            elif e.key == SDLK_UP:
                delta_y -= 1
