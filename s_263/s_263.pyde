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

from random import choice

GRID_SIZE = 30

def setup():
    size(900, 900)
    background(242)


def draw():
    x_range = range(0, width + 1, GRID_SIZE)
    y_range = range(0, height + 1, GRID_SIZE)

    points = []
    for i in range(3):
        points.append(PVector(choice(x_range), choice(y_range)))

    noFill()
    strokeWeight(2)
    stroke(24, 24, 24, 10)
    draw_shape(points, end_shape_mode=CLOSE)

def keyPressed():
    if key == 's':
        saveFrame("cover.png")