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

GRID_SIZE = 50
WIDTH, HEIGHT = 900, 900

x_range = range(GRID_SIZE * 2, WIDTH + 1 - GRID_SIZE * 2, GRID_SIZE)
y_range = range(GRID_SIZE * 2, HEIGHT + 1 - GRID_SIZE * 2, GRID_SIZE)
vertex_per_position = {(x, y): 0 for x, y in itertools.product(x_range, y_range)}
MAX_POINTS = 1
MAX_NUM_SHAPES = 5
SHAPE_POINTS = 3

def setup():
    size(WIDTH, HEIGHT)
    background(34)
    blendMode(EXCLUSION)


def draw():
    points = []
    num_points = SHAPE_POINTS
    for i in range(num_points):
        if len(vertex_per_position) < num_points:
            noLoop()

        key = choice(vertex_per_position.keys())
        print(key)
        x, y = key
        points.append(PVector(x, y))

        vertex_per_position[key] += 1
        if vertex_per_position[key] == MAX_POINTS:
            vertex_per_position.pop(key)

    if frameCount % 2:
        fill(242)
    else:
        fill(17 * 13, 17 * 4, 17)

    noStroke()
    strokeWeight(2)

    beginShape()
    for v in points:
        curveVertex(v.x,  v.y)
    for v in points:
        curveVertex(v.x,  v.y)
    endShape()

    print(len(vertex_per_position))

    if frameCount == MAX_NUM_SHAPES:
        noLoop()

def keyPressed():
    if key == 's':
        saveFrame("cover.png")