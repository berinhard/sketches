# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
# Copied from Daniel Shiffman's Coding Challenge #13
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from copy import deepcopy
from collections import namedtuple

grid = {}
prev = {}

dA = 1
dB = 0.5
feed = 0.055
kill = 0.062


class CellDist(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


def setup():
    size(200, 200)

    for x in xrange(width):
        for y in xrange(height):
            a, b = 1.0, 0.0
            grid[(x, y)] = CellDist(a, b)
            prev[(x, y)] = CellDist(a, b)

    for i in xrange(10):
        start_x = int(random(20, width - 20))
        start_y = int(random(20, height - 20))

        for x in xrange(start_x, start_x + 10):
            for y in xrange(start_y, start_y + 10):
                a, b = 1.0, 1.0
                grid[(x, y)] = CellDist(a, b)
                prev[(x, y)] = CellDist(a, b)

def draw():
    global prev

    for x in xrange(0, width):
        for y in xrange(0, height):
            k = (x, y)
            spot = prev[k]
            a, b = spot.a, spot.b
            if not any([
                x == 0,
                x == width - 1,
                y == 0,
                y == height - 1,
            ]):
                a, b = spot.a, spot.b
                i, j = x, y

                laplaceA = 0
                laplaceA += a * -1
                laplaceA += prev[(i+1, j)].a * 0.2
                laplaceA += prev[(i-1, j)].a * 0.2
                laplaceA += prev[(i, j+1)].a * 0.2
                laplaceA += prev[(i, j-1)].a * 0.2
                laplaceA += prev[(i-1, j-1)].a * 0.05
                laplaceA += prev[(i+1, j-1)].a * 0.05
                laplaceA += prev[(i-1, j+1)].a * 0.05
                laplaceA += prev[(i+1, j+1)].a * 0.05

                laplaceB = 0
                laplaceB += b * -1
                laplaceB += prev[(i+1, j)].b * 0.2
                laplaceB += prev[(i-1, j)].b * 0.2
                laplaceB += prev[(i, j+1)].b * 0.2
                laplaceB += prev[(i, j-1)].b * 0.2
                laplaceB += prev[(i-1, j-1)].b * 0.05
                laplaceB += prev[(i+1, j-1)].b * 0.05
                laplaceB += prev[(i-1, j+1)].b * 0.05
                laplaceB += prev[(i+1, j+1)].b * 0.05

                new_a = a + (dA*laplaceA - a*b*b + feed*(1-a))*1
                new_b = b + (dB*laplaceB + a*b*b - (kill+feed)*b)*1

                a, b = constrain(new_a, 0, 1), constrain(new_b, 0, 1)
            grid[k].a = a
            grid[k].b = b

    prev = grid

    loadPixels()
    for x in xrange(1, width - 1):
        for y in xrange(1, height - 1):
            cell = grid[(x, y)]
            a, b = cell.a, cell.b
            pos = x + y * width
            pixels[pos] = color((a-b) * 255)

    updatePixels()