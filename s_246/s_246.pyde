# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from itertools import combinations
from random import choice


def setup():
    size(1000, 1000)
    frameRate(1)


def draw():
    offset = 100
    size = 30
    x_range = range(offset, width - offset, size)
    y_range = range(offset, height - offset, size)

    num_points = 10
    pos = []
    curr_pos = None

    while not curr_pos and len(pos) < num_points:
        curr_pos = (choice(x_range), choice(y_range))
        if curr_pos not in pos:
            pos.append(curr_pos)

        curr_pos = None

    COLORS = get_color_palette()
    back_color = choice(COLORS)
    background(back_color)
    strokeWeight(3.5)
    strokeJoin(ROUND)
    stroke(27)

    for comb in combinations(pos, 4):
        shape_color = choice(COLORS)
        if shape_color == back_color:
            continue

        fill(shape_color)
        beginShape()
        comb = list(comb)
        for x, y in comb:
            print(x, y)
            curveVertex(x, y)
        endShape(CLOSE)