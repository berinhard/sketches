# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice

import itertools

WIDTH, HEIGHT = 900, 900
CELL_SIZE = 60
R = 40

COLORS = get_color_palette()

class Square(object):

    def __init__(self, x, y, r_inc=-1, c=None, r=R, direction=None):
        self.r = r
        self.pos = PVector(x, y)
        self.dir = direction or PVector(1, 1)
        self.r_inc = r_inc
        self.color = c or color(255, 255, 0, 1)

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def update(self):
        self.r += self.r_inc
        self.pos.add(self.dir)

        if abs(self.r) == R:
            self.r_inc *= -1

    def display(self):
        noFill()
        strokeWeight(4)
        stroke(self.color)
        rect(self.x, self.y, self.r, self.r)


squares = []

def setup():
    size(WIDTH, HEIGHT)

    num_points = 4
    rate = TWO_PI / num_points
    for x in range(0, WIDTH + CELL_SIZE, CELL_SIZE):
        for y in range(0, HEIGHT + CELL_SIZE, CELL_SIZE):
                squares.append(Square(x, y, r_inc=1, r=-R, direction=PVector(-1, -1)))

    background(42)

def draw():
    for s in squares:
        s.update()
        s.display()

def keyPressed():
    if key == 's':
        saveFrame("########.png")