from terminedia import Screen, pause
from random import random, choice


with Screen() as scr:

    step = 2
    context = scr.context
    line = scr.high.draw.line

    x_range = range(0, 400, step)
    y_range = range(0, 110, step)
    for i in range(20):
        x1, y1 = choice(x_range), choice(y_range)
        x2, y2 = choice(x_range), choice(y_range)

        context.color = choice([
            (1, 0, 0),
            (0.8, 0, 0),
            (0.6, 0, 0),
            (0, 0, 0),
        ])
        line((x1, y1), (x2, y2))

    pause()
