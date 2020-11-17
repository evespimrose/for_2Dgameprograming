import gfw
from pico2d import *
from player import Player

canvas_width = 800
canvas_height = 600


def enter():
    gfw.world.init(['bg', 'enemy', 'bullet', 'player', 'ui'])
    center = get_canvas_width() // 2, get_canvas_height() // 2

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)


def update():
    gfw.world.update()


def draw():
    gfw.world.draw()


def handle_events(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    player.handle_event(e)


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
