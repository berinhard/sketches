#!/usr/bin/env python
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

import itertools
from random import choice


heights = []
line_size = 40
W, H = 1400, 600
x_offset = W / line_size


COLORS = None
iters = 0


def new_canvas():
    global COLORS, iters
    COLORS = itertools.cycle(get_color_palette()[::-1])
    iters = 0


def setup():
    size(W, H)
    strokeWeight(3)
    new_canvas()

def draw():
    global iters
    if iters == 0:
        background(27)

    iters += 1
    stroke(COLORS.next())
    y_range = range(line_size, H, line_size)

    x_values = range(0, W, x_offset)
    y_values = [choice(y_range) for i in x_values]
    y_values[0] = H / 2
    y_values[-1] = H / 2

    py = None
    for x, y in zip(x_values, y_values):
        if py is not None:
            line(x, py, x, y)
        xf = x + x_offset
        line(x, y, xf, y)
        py = y

    if iters > 5:
        noLoop()


def keyPressed():
    if key == 'n':
        new_canvas()
        loop()
    elif key == 's':
        saveFrame("#######.png")
