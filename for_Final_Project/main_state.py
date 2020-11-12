import gfw
from pico2d import *

canvas_width = 800
canvas_height = 600


def enter():
    gfw.world.init(['bg', 'enemy', 'bullet', 'player', 'ui'])
    center = get_canvas_width() // 2, get_canvas_height() // 2

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)


def update():
    pass


def draw():
    pass


def handle_events():
    pass


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
