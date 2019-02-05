# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import regular_polygon
from random import choice
from collections import namedtuple


WHITE = color(228, 288, 288)
BLACK = color(27, 27, 27)

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


class VirtualGrid(object):

    def __init__(self, x, y, num_rows, grid_row_size):
        self.grid_x = x
        self.grid_y = y
        self.num_rows = num_rows
        self.grid_row_size = grid_row_size

    def get_grid_positions(self):
        grid_width_limit = self.grid_x + self.num_rows * self.grid_row_size
        grid_height_limit = self.grid_y + self.num_rows * self.grid_row_size
        x_positions = range(self.grid_x, grid_width_limit, self.grid_row_size)
        y_positions = range(self.grid_y, grid_height_limit, self.grid_row_size)

        for i, x in enumerate(x_positions):
            for j, y in enumerate(y_positions):
                yield GridRow(x, y, i, j)

    def draw(self, func, *f_args, **f_kwargs):
        for grid_row in self.get_grid_positions():
            with pushMatrix():
                translate(grid_row.x, grid_row.y)
                self.draw_row(grid_row, func, *f_args, **f_kwargs)

    def draw_row(self, grid_row, func, *f_args, **f_kwargs):
        func(*f_args, **f_kwargs)


class DiagonalsOnlyGrid(VirtualGrid):

    def draw_row(self, grid_row, func, *f_args, **f_kwargs):
        diff = abs(grid_row.i - grid_row.j)
        if not diff or grid_row.i + grid_row.j == self.num_rows - 1:
            func(*f_args, **f_kwargs)


class RandomPositioningGrid(VirtualGrid):

    def __init__(self, *args, **kwargs):
        self.percent = kwargs.pop('percent')
        super(RandomPositioningGrid, self).__init__(*args, **kwargs)

    def draw_row(self, grid_row, func, *f_args, **f_kwargs):
        if random(1) > self.percent:
            func(*f_args, **f_kwargs)


class OddLinesGrid(VirtualGrid):

    def draw_row(self, grid_row, func, *f_args, **f_kwargs):
        if grid_row.j % 2:
            func(*f_args, **f_kwargs)


class EvenColumnsGrid(VirtualGrid):

    def draw_row(self, grid_row, func, *f_args, **f_kwargs):
        if not grid_row.i % 2:
            func(*f_args, **f_kwargs)


def draw():
    background(BLACK)

    x, y = width / 4, height / 4
    num_rows = 10
    row_size = 50

    grid_1 = EvenColumnsGrid(x + row_size / 2, y + row_size / 2, num_rows / 2, row_size)
    grid_2 = RandomPositioningGrid(x, y, num_rows, row_size, percent=0.73)
    grid_3 = OddLinesGrid(width / 2, height / 2, 8, row_size)
    grid_4 = DiagonalsOnlyGrid(x + 250, y, 6, row_size)

    grid_1.draw(ellipse, 0, 0, 40, 40)
    stroke(0, 255, 255)
    grid_2.draw(rect, 0, 0, 40, 40)
    stroke(255, 0, 255)
    grid_3.draw(triangle, 10, 10, 40, 40, 10, 40)
    stroke(255, 255, 0)
    grid_4.draw(line, 10, 10, 40, 40)

    saveFrame("cover.png")
    noLoop()