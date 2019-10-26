from terminedia import Screen, pause
from random import random


with Screen() as scr:

    step = 4
    context = scr.context
    line = scr.high.draw.line


    for x in range(0, 400, step):
        for y in range(0, 110, step):
            context.color = 0.5, random(), 0.7
            line((x, y), (x + step - 2, y))

    pause()
