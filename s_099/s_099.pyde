# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import regular_polygon
from random import choice
from collections import namedtuple

WHITE = color(248, 248, 248)
BLACK = color(17, 17, 17)

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


def draw():
    background(BLACK)

    for grid_row in get_grid_positions(width / 4, height / 4, 10, 50):
        with pushMatrix():
            translate(grid_row.x, grid_row.y)
            rect(0, 0, 40, 40)

    for grid_row in get_grid_positions(0, 0, 8, 50):
        with pushMatrix():
            translate(grid_row.x, grid_row.y)
            ellipse(0, 0, 40, 40)


    for grid_row in get_grid_positions(width / 2, height / 2, 8, 50):
        with pushMatrix():
            translate(grid_row.x, grid_row.y)
            triangle(10, 10, 40, 40, 10, 40)

    saveFrame("cover.png")
    noLoop()