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


img = None
block_size = 5

def mean(l):
    return sum(l) / len(l)

def get_avg_color(x, y, block_size):
    r, g, b = [], [], []
    for x in range(x, x + block_size, 1):
        for y in range(y, y + block_size, 1):
            c = img.get(x, y)
            r.append(red(c))
            g.append(green(c))
            b.append(blue(c))

    return color(mean(r), mean(g), mean(b))


def setup():
    global img
    img = loadImage('out.jpeg')
    size(1400, 1400)


def draw():
    noStroke()
    for x in reverse(range(0, width + block_size, block_size)):
        for y in reverse(range(0, height + block_size, block_size)):
            fill(img.get(10, 10))
            rect(x, y, block_size, block_size)


            c = img.get(x, y)
            #c = get_avg_color(x, y, block_size)
            r, g, b = red(c), green(c), blue(c)
            #if r < 210:
                #off = 10
                #r += random(-off, off)
                #g += random(-off, off)
                #b += random(-off, off)
            fill(color(r, g, b))
            off = random(20)
            rect(x, y, block_size + off, block_size + off)

    saveFrame("cover.png")
    noLoop()