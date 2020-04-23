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


def setup():
    size(400, 400)
    points = [
        (100, 50),
        (300, 100),
        (200, 300),
        (100, 300),
        (130, 210),
        (160, 130),
    ]

    beginShape()
    for x, y in points:
        ellipse(x, y, 10, 10)
        curveVertex(x, y)

    # add 3 first points to have a complete curved shape
    for x, y in points[:3]:
        curveVertex(x, y)
    endShape()

    saveFrame("cover.png")

def draw():
    pass
