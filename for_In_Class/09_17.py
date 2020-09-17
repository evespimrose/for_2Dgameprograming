from pico2d import *
from gobj import *
import raandom



class Boy:
    def __init__(self):
        self.x, self.y = set_canvas_width()
        self.x, self.y = random.randint(100,700), random.randint(100,500)
        self.image = load_image('.../.../res/run_animation.png')
        self.dx = random.random()
        self.fidx = random.randint(0,7)
    
    def draw(self):
        self.image.clip_draw(self.fidx * 100,0,100,100,self.x,self.y)
    
    def update(self):
        self.x += self.dx * 5
        self.fidx = (self.fidx + 1) % 8

        

class Grass:
    def __init__(self):
        self.image = load_image('.../.../res/grass.png')
        self.x, self.y = 400,30
        
    def draw(self):
        self.image.draw(self.x,self.y)
    

open_canvas()

team = [Boy() for i in range(11)]
    
boy = team[0]

gra = Grass()


running = True

while running:
    clear_canvas()
    
    gra.draw()
    
    for b in team:
        b.draw()
    
    update_canvas()

    for b in team:
        b.update()

    

    
    






    
