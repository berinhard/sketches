add_library('svg')
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

base = 300
pgDrawing = None

def setup():
    global pgDrawing
    size(900, 900)
    background(242)
    strokeWeight(2)
    stroke(0)
    rectMode(CENTER)
    #background(240)

def keyPressed():
    if key == 's':
        saveFrame('######.png')


def draw():
    pgDrawing = createGraphics(width, height, SVG, "out.svg")
    beginRecord(pgDrawing)
    translate(width / 2, height / 2)
    pgDrawing.strokeWeight(2)
    angle = 0
    i = 1
    while angle <= TWO_PI:
        angle = i * (TWO_PI / 16)
        rotate(angle)

        x, y = 0, 0
        s1, s2, s3, s4 = [
            PVector(x - base, y - base),
            PVector(x + base, y - base),
            PVector(x + base, y + base),
            PVector(x - base, y + base),
        ]

        i1, i2, i3, i4 = [
            PVector(x, y - base),
            PVector(x + base / 2, y),
            PVector(x, y + base),
            PVector(x - base / 2, y),
        ]

        noFill()
        draw_shape([s1, i1, s2, s3, i3, s4], end_shape_mode=CLOSE)  # BASE

        # CIRCLES
        ellipse(i4.x, i4.y, base, base)
        ellipse(i2.x, i2.y, base, base)

        # TOP TRIANGLES
        draw_shape([s1, i1, i4], end_shape_mode=CLOSE)  # left
        draw_shape([i1, i2, i4], end_shape_mode=CLOSE)  # center
        draw_shape([i1, i2, s2], end_shape_mode=CLOSE)  # right

        # BOTTOM TRIANGLES
        draw_shape([s4, i4, i3], end_shape_mode=CLOSE)  # left
        draw_shape([i3, i2, i4], end_shape_mode=CLOSE)  # center
        draw_shape([i3, i2, s3], end_shape_mode=CLOSE)  # right

        rotate(-angle)
        i += 1

    if angle > TWO_PI:
        blendMode(DIFFERENCE)
        fill(242)
        noStroke()
        ellipse(0, 0, 3 * base / 4,  3 * base / 4)
        saveFrame("cover.png")
        endRecord()
        noLoop()
