from numpy import True_
from pygame import *

w = 450 ; h = 300 ; c=0
win = display.set_mode((w,h))
black = (255,255,255)

def redraw():
    win.fill(black)
    display.update()

def main():
    run = True

    while run:
        for e in event.get():
            if e.type == QUIT:
                run == False
                quit()

