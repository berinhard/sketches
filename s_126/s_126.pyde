# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from collections import namedtuple

WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)


def pattern():
    d = 100
    strokeWeight(2)
    stroke(BLACK)
    x1, y1 = width / 2 - d, d
    x2, y2 = d, height / 2 - 100
    line(x1, y1, x2, y2)



    fill(BLACK)
    rect(d, d, d, d)
    fill(RED)
    rect(width / 4, height / 4, 2 * d,  2 * d)


def setup():
    background(WHITE)
    stroke(BLACK)
    size(900, 900)


Quadrant = namedtuple('Quadrant', ['x', 'y', 'x_scale', 'y_scale'])


def draw():
    quadrants = [
        Quadrant(0, 0, 1, 1),
        Quadrant(width, 0, -1, 1),
        Quadrant(0, height, 1, -1),
        Quadrant(width, height, -1, -1),
    ]

    for q in quadrants:
        with pushMatrix():
            translate(q.x, q.y)
            scale(q.x_scale, q.y_scale)
            pattern()

    strokeWeight(1)
    w, h = width, height
    line(0, h / 2, w, h / 2)
    line(w / 2, 0, w / 2, h)

    noLoop()
    saveFrame("cover.png")