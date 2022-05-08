from pygame import *;from time import *;from math import *

grass = image.load("c:/users/mahmoud/desktop/learn/res/images/grass.png")
track = image.load("c:/users/mahmoud/desktop/learn/res/images/track.png")
track_border = image.load("c:/users/mahmoud/desktop/learn/res/images/track_border.png")
finish = image.load("c:/users/mahmoud/desktop/learn/res/images/finish.png")
red_car = image.load("c:/users/mahmoud/desktop/learn/res/images/red_car.png")
green_car = image.load("c:/users/mahmoud/desktop/learn/res/images/green_car.png")

w,h = track.get_width(),track.get_height()
win = display.set_mode((w,h))
title = display.set_caption("just a game")