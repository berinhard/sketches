# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from collections import namedtuple
from berin.grids import VirtualGrid


WHITE = color(235, 235, 235)
BLACK = color(42)
RED = color(181, 32, 42)

OFFSET = 2


def pattern(w, h):
    w -= OFFSET
    h -= OFFSET
    v1, v2, v3, v4 = PVector(0, 0), PVector(w, 0), PVector(0, h), PVector(w, h)

    # margin rect
    strokeWeight(0.5)
    stroke(27, 27, 27, 130)
    noFill()
    rect(0, 0, w, h)

    # internal arc
    x = 7 * w / 11
    y = 7 * h / 11
    noStroke()
    fill(RED)
    arc(x, y, 3*w/4, 3*h/4, 0,  HALF_PI)

    # first set of red lines
    x_pos = [PVector.lerp(v1, v2, 0.1 * i) for i in range(2, 6)]
    y_pos = [PVector.lerp(v1, v3, 0.1 * i) for i in range(2, 6)]

    strokeWeight(2)
    stroke(RED)
    for vx, vy in zip(x_pos, y_pos):
        line(vx.x, vx.y, vy.x, vy.y)


    # second set of red lines
    x_pos = [PVector.lerp(v1, v2, 0.1 * i) for i in range(7, 10)]
    y_pos = [PVector.lerp(v1, v3, 0.1 * i) for i in range(7, 10)]

    stroke(RED)
    for vx, vy in zip(x_pos, y_pos):
        line(vx.x, vx.y, vy.x, vy.y)

    # minor black starts from last line from second set and goes borders
    last_x, last_y = x_pos[-1], y_pos[-1]
    pos = [PVector.lerp(last_x, last_y, 0.1 * i) for i in range(3, 5)]
    stroke(BLACK)
    for v in pos:
        line(v.x, v.y, v.x, h)

    pos = [PVector.lerp(last_x, last_y, 0.1 * i) for i in range(6, 8)]
    stroke(BLACK)
    for v in pos:
        line(v.x, v.y, w, v.y)



def tiled_pattern(w, h, pattern):
    quadrants = [
        SymmetricQuadrant(0, 0, 1, 1),
        SymmetricQuadrant(w, 0, -1, 1),
        SymmetricQuadrant(0, h, 1, -1),
        SymmetricQuadrant(w, h, -1, -1),
    ]

    for quadrant in quadrants:
        with quadrant:
            pattern(w / 2, h / 2)


def setup():
    background(WHITE)
    stroke(BLACK)
    strokeWeight(2)
    size(900, 900)


class SymmetricQuadrant(object):

    def __init__(self, x, y, x_scale, y_scale):
        self.x, self.y = x, y
        self.x_scale, self.y_scale = x_scale, y_scale

    def place(self):
        pushMatrix()
        translate(self.x, self.y)
        scale(self.x_scale, self.y_scale)

    def release(self):
        popMatrix()

    def __enter__(self, *args, **kwargs):
        self.place()

    def __exit__(self, *args, **kwargs):
        self.release()


def draw():
    num_rows = 5
    elem_size = width / num_rows
    grid = VirtualGrid(0, 0, num_rows, elem_size)
    grid.draw(tiled_pattern, elem_size - OFFSET, elem_size - OFFSET, pattern)

    #tiled_pattern(width / 2, height / 2, pattern)

    fill(WHITE)
    #rect(0, 0, width, 180)
    #rect(0, height - 180, width, height)

    noLoop()
    saveFrame("cover.png")