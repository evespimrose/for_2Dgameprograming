import gfw
from pico2d import *

canvas_width = 800
canvas_height = 600

def enter():
    gfw.world.init(['bg', 'enemy', 'bullet', 'player', 'ui'])
    center = get_canvas_width() // 2, get_canvas_height() // 2