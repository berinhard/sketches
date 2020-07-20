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
    strokeWeight(5)
    strokeCap(ROUND)
    stroke(242)
    update_field()


def draw():
    background(27)
    cfg = [
        (0, 0, color(0)),
        (25, 25, color(217, 54, 63)),
        (50, 50, color(242))
    ]
    for bx, by, c in cfg:
        stroke(c)
        for i in range(cols-1):
            for j in range(rows-1):
                x = i * cell_size + bx
                y = j * cell_size + by

                off = cell_size * 0.5

                p1, p2, p3, p4 = fields[i][j], fields[i+1][j], fields[i+1][j+1], fields[i][j+1]

                off_a = (p1 + p2) / 2
                off_b = (p2 + p3) / 2
                off_c = (p3 + p4) / 2
                off_d = (p4 + p1) / 2

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

                if state == 1:
                    vline(c, d)
                elif state == 2:
                    vline(b, c)
                elif state == 3:
                  vline(b, d)
                elif state == 4:
                  vline(a, b)
                elif state == 5:
                  vline(a, d)
                  vline(b, c)
                elif state == 6:
                  vline(a, c)
                elif state == 7:
                  vline(a, d)
                elif state == 8:
                  vline(a, d)
                elif state == 9:
                  vline(a, c)
                elif state == 10:
                  vline(a, b)
                  vline(c, d)
                elif state == 11:
                  vline(a, b)
                elif state == 12:
                  vline(b, d)
                elif state == 13:
                  vline(b, c)
                elif state == 14:
                  vline(c, d)

    noLoop()


def update_field():
    global fields, cell_size, cols, rows

    cell_size = choice(range(50, 201, 50))
    cols  = 2 + width / cell_size
    rows  = 2 + height / cell_size

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

def vline(v1, v2):
    line(v1.x, v1.y, v2.x, v2.y)

def keyPressed():
    if key == 'n':
        update_field()
        loop()
    elif key == 's':
        saveFrame("#########.png")
