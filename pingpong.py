from pygame import *

speed = 20
win_h = 700
win_w = 500
FPS = 60
clock = time.Clock()
display.set_caption('Пинг Понг')
window = display.set_mode((700, 500))
window.fill((255, 192, 203))
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()   
    clock.tick(FPS)