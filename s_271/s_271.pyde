#!/usr/bin/env python
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Python implementation from Daniel Shiffman's Coding in the Cabana 5: Marching Squares
# https://www.youtube.com/watch?v=0ZONMNUKTfU
from itertools import cycle
from random import choice, randint, shuffle
from collections import defaultdict


fields = []
cell_size, cols, rows = 0, [], []


def setup():
    size(900, 900)
    #fullScreen()
    strokeWeight(5)
    strokeCap(RECT)
    stroke(242)
    update_field()


curr_color = None


def draw():
    global curr_color
    background(27)
    cfg = [
        (0, 0, color(0)),
        (25, 25, color(217, 54, 63)),
        (50, 50, color(242))
    ]
    for counter, c in enumerate(cfg):
        bx, by, curr_color = c
        stroke(curr_color)
        for i in range(cols-1):
            for j in range(rows-1):
                x = (i - 1) * cell_size + bx
                y = (j - 1) * cell_size + by

                off = cell_size * 0.5

                p1, p2, p3, p4 = fields[i][j], fields[i+1][j], fields[i+1][j+1], fields[i][j+1]

                off_a = (p1 + p2) / 2 * cell_size
                off_b = (p2 + p3) / 2 * cell_size
                off_c = (p3 + p4) / 2 * cell_size
                off_d = (p4 + p1) / 2 * cell_size

                a = PVector(x + off_a, y)
                b = PVector(x + cell_size, y + off_b)
                c = PVector(x + off_c, y + cell_size)
                d = PVector(x, y + off_d)

                state = get_state(
                    get_value(i, j),
                    get_value(i+1, j),
                    get_value(i+1, j+1),
                    get_value(i, j+1),
                )

                pbx, pby = None, None
                if counter > 0:
                    cfg_i = counter - 1
                    pbx, pby = cfg[cfg_i][0] - bx, cfg[cfg_i][1] - by

                if state == 1:
                    vline(c, d, pbx, pby)
                elif state == 2:
                    vline(b, c, pbx, pby)
                elif state == 3:
                  vline(b, d, pbx, pby)
                elif state == 4:
                  vline(a, b, pbx, pby)
                elif state == 5:
                  vline(a, d, pbx, pby)
                  vline(b, c, pbx, pby)
                elif state == 6:
                  vline(a, c, pbx, pby)
                elif state == 7:
                  vline(a, d, pbx, pby)
                elif state == 8:
                  vline(a, d, pbx, pby)
                elif state == 9:
                  vline(a, c, pbx, pby)
                elif state == 10:
                  vline(a, b, pbx, pby)
                  vline(c, d, pbx, pby)
                elif state == 11:
                  vline(a, b, pbx, pby)
                elif state == 12:
                  vline(b, d, pbx, pby)
                elif state == 13:
                  vline(b, c, pbx, pby)
                elif state == 14:
                  vline(c, d, pbx, pby)

    noLoop()


def update_field():
    global fields, cell_size, cols, rows

    cell_size = choice(range(50, 201, 50))
    cols  = 3 + width / cell_size
    rows  = 3 + height / cell_size

    fields = [
        [random(1) for y in range(rows)]
        for i in range(cols)
    ]

def get_value(i, j):
    v = fields[i][j]
    return 0 if v < 0.5 else 1

def get_state(a, b, c, d):
    """
    Binary number as 0110 (a=0, b=1, c=1, d=10)
    """
    return a * 8 + b * 4 + c * 2 + d * 1

def vline(v1, v2, prev_x=0, prev_y=0):
    strokeWeight(5)
    line(v1.x, v1.y, v2.x, v2.y)

    if prev_x and prev_y:
        pv1 = PVector(v1.x + prev_x, v1.y + prev_y)
        pv2 = PVector(v2.x + prev_x, v2.y + prev_y)
        r, g, b = red(curr_color), green(curr_color), blue(curr_color)

        for i in [25, 50, 75]:
            i = i / 100.0
            a = 200 * i
            strokeWeight(int(5 * i))
            stroke(color(r, g, b, a))
            vline(PVector.lerp(pv2, v2, i), PVector.lerp(pv1, v1, i))


def keyPressed():
    if key == 'n':
        update_field()
        loop()
    elif key == 's':
        saveFrame("#########.png")
