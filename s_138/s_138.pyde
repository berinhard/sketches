# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from berin.palettes import get_color_palette

rects_to_draw = []
WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
COLORS = get_color_palette()


def setup():
    size(900, 900)
    rects_to_draw.append((0, 0, 900, 900))
    fill(WHITE)
    stroke(BLACK)
    strokeWeight(2)
    frameRate(5)


def draw():
    next_rects = []

    if not rects_to_draw:
        saveFrame("#######.png")
        noLoop()

    while rects_to_draw:
        x, y, w, h = rects_to_draw.pop()

        if w < 10 or h < 10:
            continue

        fill(choice(COLORS))
        rect(x, y, w, h)

        w_r = range(int(3 * w / 4), int(w), 5)
        h_r = range(int(3 * h / 4), int(h), 5)

        new_w, new_h = choice(w_r), choice(h_r)
        new_x, new_y = x, y


        if new_w < 10 or new_h < 10:
            continue

        next_rects.append((new_x, new_y, new_w, new_h))

        v1, v2, v3, v4 = [
            PVector(x, y), # v1
            PVector(x + new_w, y), # v2
            PVector(x, y + new_h), # v3
            PVector(x + new_w, y + new_h), # v4
        ]

        index = choice([0.1 * i for i in range(1, 10)])
        p = PVector.lerp(v2, v4, index)

        sub_w = w - new_w
        sub_h = y + new_h - p.y
        if sub_w >=10 and sub_h >= 10:
            next_rects.append((p.x, p.y, sub_w, sub_h))

        fill(choice(COLORS))
        rect(p.x, v2.y, w - new_w, p.y - y)

        index = choice([0.1 * i for i in range(1, 10)])
        p = PVector.lerp(v3, v4, index)
        sub_w = w - p.x - x
        sub_h = h - new_h
        if sub_w >=10 and sub_h >= 10:
            next_rects.append((p.x, p.y, sub_w, sub_h))

        fill(choice(COLORS))
        rect(v3.x, v3.y, p.x - x, h - new_h)

    for x in next_rects:
        rects_to_draw.append(x)


def keyPressed():
    if key == 'n':
        global COLORS, rects_to_draw

        rects_to_draw = [(0, 0, width, height)]
        COLORS = get_color_palette()

        loop()
        redraw()