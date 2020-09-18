from pico2d import *

open_canvas()

boy = load_image('C:/Users/Jang/Desktop/gitupload/for_In_Class/run_animation.png')
gra = load_image('C:/Users/Jang/Desktop/gitupload/for_In_Class/grass.png')

x = 0
frame = 0
while (x<800):
    clear_canvas()
    
    gra.draw(400,30)
    boy.clip_draw(frame*100,0,100,100,x,90)
    
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()
    





delay(5)
close_canvas()
