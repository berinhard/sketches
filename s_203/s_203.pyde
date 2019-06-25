# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from copy import deepcopy
from collections import namedtuple

grid = []
next_grid = []

dA = 1
dB = 0.5
feed = 0.065
kill = 0.042


class CellDist(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


def setup():
    size(300, 300)

    for x in range(width):
        grid.append([])
        for y in range(height):
            a, b = 1.0, 0.0
            grid[x].append(CellDist(a, b))

    for i in range(10):
        start_x = int(random(20, width - 20))
        start_y = int(random(20, height - 20))

        for x in range(start_x, start_x + 10):
            for y in range(start_y, start_y + 10):
                a, b = 1.0, 1.0
                grid[x][y] = CellDist(a, b)


def new_dist_for(i, j):
    spot = grid[i][j]

    a, b = spot.a, spot.b

    laplaceA = 0
    laplaceA += a * -1
    laplaceA += grid[i+1][j].a * 0.2
    laplaceA += grid[i-1][j].a * 0.2
    laplaceA += grid[i][j+1].a * 0.2
    laplaceA += grid[i][j-1].a * 0.2
    laplaceA += grid[i-1][j-1].a * 0.05
    laplaceA += grid[i+1][j-1].a * 0.05
    laplaceA += grid[i-1][j+1].a * 0.05
    laplaceA += grid[i+1][j+1].a * 0.05

    laplaceB = 0
    laplaceB += b * -1
    laplaceB += grid[i+1][j].b * 0.2
    laplaceB += grid[i-1][j].b * 0.2
    laplaceB += grid[i][j+1].b * 0.2
    laplaceB += grid[i][j-1].b * 0.2
    laplaceB += grid[i-1][j-1].b * 0.05
    laplaceB += grid[i+1][j-1].b * 0.05
    laplaceB += grid[i-1][j+1].b * 0.05
    laplaceB += grid[i+1][j+1].b * 0.05

    new_a = a + (dA*laplaceA - a*b*b + feed*(1-a))*1
    new_b = b + (dB*laplaceB + a*b*b - (kill+feed)*b)*1

    return constrain(new_a, 0, 1), constrain(new_b, 0, 1)


def draw():
    global grid

    new_grid = []
    for x in range(0, width):
        new_grid.append([])
        for y in range(0, height):
            border_conditions = [
                x == 0,
                x == width - 1,
                y == 0,
                y == height - 1,
            ]
            if any(border_conditions):
                spot = grid[x][y]
                a, b = spot.a, spot.b
            else:
                a, b = new_dist_for(x, y)
            new_grid[x].append(CellDist(a, b))

    grid = new_grid
    loadPixels()

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            cell = grid[x][y]
            a, b = cell.a, cell.b
            pos = x + y * width
            pixels[pos] = color((a-b) * 255)

    updatePixels()
    print(frameCount)