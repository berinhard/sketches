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
MAX_NUM_SHAPES = 8
SHAPE_POINTS = 4
counter = 0


def refresh():
    global vertex_per_position, counter, MAX_NUM_SHAPES, SHAPE_POINTS
    MAX_NUM_SHAPES = int(random(3, 10))
    SHAPE_POINTS = int(random(3, 7))
    vertex_per_position = {(x, y): 0 for x, y in itertools.product(x_range, y_range)}
    counter = 0


def setup():
    size(WIDTH, HEIGHT)
    blendMode(EXCLUSION)
    refresh()
    background(34)


def draw():
    global counter

    if counter == 0:
        background(30)

    points = []
    num_points = SHAPE_POINTS
    for i in range(num_points):
        key = choice(vertex_per_position.keys())
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
        vertex(v.x,  v.y)
    endShape()

    counter += 1
    if counter == MAX_NUM_SHAPES:
        print("stoped")
        noLoop()

def keyPressed():
    if key == 's':
        saveFrame("##########.png")
    if key == 'n':
        refresh()
        loop()
