from terminedia import Screen, pause
from random import random


def composition(scr, y, step):
    for x in range(0, 400, step):

        if random() > 0.5:
            scr.context.color = 1, 0, 0
            scr.high.draw.rect((x, y), (x + step + 5, y + 15))

        scr.context.color = 0, 0, 1
        scr.high.draw.line((x, y + 20), (x + step + 5, y + 20))


        scr.context.color = 0, 1, 0
        scr.high.draw.ellipse((x, y + 10), (x + step + 5, y + 30))



with Screen() as scr:

    step = 20
    for y in range(5, 80, 30):
        composition(scr, y, step)

    for x in range(0, 400, step):
        if random() > 0.5:
            scr.context.color = 1, 0, 0
            scr.high.draw.rect((x, y + 30), (x + step + 5, 30 + y + 15))

    pause()