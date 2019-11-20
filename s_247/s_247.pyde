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

def collatz(n):
    if not n % 2:
        return n / 2
    else:
        return 3 * n + 1

def setup():
    size(900, 900)
    background(27)


def draw():
    translate(width / 2, height / 2)
    l = 15

    stroke(240, 80)
    strokeWeight(6)
    with pushMatrix():
        angle = PI / 12
        for i in range(1, 700):
            px, py = 0, 0
            while i != 1:
                i = collatz(i)

                line(0, 0, 0, l)
                translate(0, l)
                if i % 2:
                    rotate(angle)
                else:
                    rotate(-angle)

    for i in range(1, 700):
        px, py = 0, 0
        while i != 1:
            print(i)
            i = collatz(i)

            line(0, 0, 0, l)
            translate(0, l)
            if i % 2:
                rotate(-angle)
            else:
                rotate(angle)

    saveFrame("cover.png")
    noLoop()