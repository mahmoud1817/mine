from pygame import *
from neat import *
from time import *
from os import *
from random import *

bird = [transform.scale2x(image.load("C:/users/mahmoud/desktop/learn/res/images/bird1.png")),
transform.scale2x(image.load("C:/users/mahmoud/desktop/learn/res/images/bird2.png"))]

pipe = transform.scale2x(image.load("C:/users/mahmoud/desktop/learn/res/images/pipe.png"))
base = transform.scale2x(image.load("C:/users/mahmoud/desktop/learn/res/images/base.png"))
bg = transform.scale2x(image.load("C:/users/mahmoud/desktop/learn/res/images/bg.png"))

