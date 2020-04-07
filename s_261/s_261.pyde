#!/usr/bin/env python
# Author: Berin
# Sketchet repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

import itertools
from random import choice

r = 800
pgDrawing = None


def setup():
    size(900, 900)
    background(242)
    strokeWeight(3)
    stroke(0)
    frameRate(24)


def draw():
    r = int(map(noise(frameCount * 0.0137), 0, 1, 425, 850))
    r2 = int(map(noise((frameCount + 1041231) * 0.0142), 0, 1, 425, 850))

    translate(width / 2, height / 2)
    angle = 0
    i = 0
    background(242)
    while angle <= TWO_PI:
        angle = i * (TWO_PI / 32)
        rotate(angle)
        noFill()

        if i % 2:
            stroke(42, 42, 42, 180)
        else:
            stroke(212, 12, 0, 210)
        ellipse(0, 0, r - i * 25, r2)

        rotate(-angle)
        i += 1
