# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import regular_polygon
from random import choice
from collections import namedtuple


WHITE = color(228, 288, 288)
BLACK = color(27, 27, 27)
RED = color(218, 32, 10)
GOLDEN = color(218, 185, 32, 140)
GREEN = color(32, 181, 10)

#WHITE = color(248, 248, 248)
#BLACK = color(17, 17, 17)

def setup():
    size(900, 900)
    strokeWeight(2)
    noFill()
    frameRate(2)
    rectMode(CENTER)
    stroke(WHITE)
    noFill()
    smooth()


GridRow = namedtuple("GridRow", "x, y, i, j")


def get_grid_positions(grid_x, grid_y, num_rows, grid_row_size):
    grid_width_limit = grid_x + num_rows * grid_row_size
    grid_height_limit = grid_y + num_rows * grid_row_size
    x_positions = range(grid_x, grid_width_limit, grid_row_size)
    y_positions = range(grid_y, grid_height_limit, grid_row_size)

    for i, x in enumerate(x_positions):
        for j, y in enumerate(y_positions):
            yield GridRow(x, y, i, j)


def draw_as_grid(grid_x, grid_y, num_rows, grid_row_size, func, *f_args, **f_kwargs):
    for grid_row in get_grid_positions(grid_x, grid_y, num_rows, grid_row_size):
        with pushMatrix():
            translate(grid_row.x, grid_row.y)
            func(*f_args, **f_kwargs)


def draw():
    background(BLACK)

    x, y = width / 4, height / 4
    num_rows = 10
    row_size = 50
    draw_as_grid(x + row_size / 2, y + row_size / 2, num_rows / 2, row_size, ellipse, 0, 0, 40, 40)
    draw_as_grid(x, y, num_rows, row_size, rect, 0, 0, 40, 40)
    draw_as_grid(width / 2, height / 2, 8, row_size, triangle, 10, 10, 40, 40, 10, 40)
    stroke(RED)
    draw_as_grid(x + 250, y, 6, row_size, line, 10, 10, 40, 40)

    saveFrame("cover.png")
    noLoop()