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
X0, Y0 = WIDTH / 2, HEIGHT / 2
R = 420

COLORS = get_color_palette()
ITER_COLORS = itertools.cycle(COLORS)


class Point(object):

    def __init__(self, angle=None):
        self.r = R
        self.angle = angle

    @property
    def pos(self):
        return polar_coordinate(X0, Y0, self.r, self.angle)


    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def update(self):
        self.r -= 30

    def display(self):
        pass


points = []
points_to_move = None


def setup():
    global points_to_move

    size(WIDTH, HEIGHT)
    frameRate(10)

    num_points = 6
    rate = TWO_PI / num_points
    for i in range(num_points):
        points.append(Point(angle=rate * i))

    points_to_move = itertools.cycle(points)

    background(250)

def draw():
    for p in points:
        p.display()

    p = next(points_to_move)
    p.update()

    noFill()
    noStroke()
    c = next(ITER_COLORS)
    fill(c)
    noStroke()

    if p.r >= 0:
        draw_shape(points, end_shape_mode=CLOSE)
    else:
        saveFrame("######.png")
        noLoop()