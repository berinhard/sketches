import os
import math
from terminedia import Screen, pause
from random import random, choice, randrange


def polar_coordinate(x0, y0, r, angle):
    x = x0 + r * math.cos(angle)
    y = y0 + r * math.sin(angle)
    return int(x), int(y)


def shape(scr, x, y):
    context = scr.context
    line = scr.high.draw.line


    rate = 120
    angle_inc = 2 * math.pi / rate

    for r in range(10, 55, 3):
        for i in range(rate):
            angle = angle_inc * i
            x, y = polar_coordinate(center_x, center_y, r + randrange(-2, 2), angle)

            context.color = choice([
                (1, 0, 1),
                (1, 1, 0),
                (0, 1, 1),
            ])
            line((x, y), (x, y))


with Screen() as scr:
    term = os.get_terminal_size()
    max_x = term.columns * 2
    max_y = term.lines * 2

    center_x, center_y = max_x // 2, max_y // 2
    shape(scr, center_x, center_y)

    center_x, center_y = 3 * max_x // 4, max_y // 2
    shape(scr, center_x, center_y)

    center_x, center_y = max_x // 4, max_y // 2
    shape(scr, center_x, center_y)

    pause()
