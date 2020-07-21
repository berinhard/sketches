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


n = 14
angle_rate = TWO_PI / n
angles = [i * angle_rate for i in range(n)]

def setup():
    size(900, 900)
    background(27)
    stroke(242)
    strokeCap(SQUARE)
    strokeWeight(2)
    noFill()

def draw():
    r = width / 4
    h = map(noise(frameCount * 0.0241), 0, 1, height / 4, height / 16)
    fill(27, 27, 27, 30)
    noStroke()
    rect(0, 0, width, height)
    noFill()
    translate(width/2, height/2)
    rotate(TWO_PI / 32 * frameCount / 24.0)
    for x in [0, angle_rate]:
        with pushMatrix():
            rotate(x)
            if (x):
                scale(-1, 1)
                stroke(217, 54, 63)
            else:
                stroke(232)
            for a in angles:
                with pushMatrix():
                    v1 = polar_coordinate(0, 0, r, a)
                    v2 = polar_coordinate(0, 0, r, a + angle_rate)
                    v3 = polar_coordinate(0, 0, h, a + angle_rate/2)
                    v4 = polar_coordinate(0, 0, r + h, a + angle_rate/2)
                    v6 = polar_coordinate(0, 0, r, a + 3*angle_rate/2)

                    triangle(v6.x, v6.y, v2.x, v2.y, v4.x, v4.y)

                    beginShape()
                    vertex(v2.x, v2.y)
                    vertex(v6.x, v6.y)
                    vertex(v3.x, v3.y)
                    endShape(CLOSE)

def keyPressed():
    if key == 's':
        saveFrame("cover.png")
