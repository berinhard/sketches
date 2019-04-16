# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
import itertools
from random import choice

from berin.grids import BaseGrid

WHITE = color(241)
BLACK = color(27)
COMPLEMENTARY = color(55, 132, 223)

class CellCross(object):

    def __init__(self, grid_elem):
        self.grid_elem = grid_elem
        self.x, self.y = grid_elem.x, grid_elem.y
        self.w, self.h = grid_elem.width, grid_elem.height

        u_w, b_w = self.w / 2, self.w / 2
        l_h, r_h = self.h / 2, self.h / 2

        lerp_ranges = [i / 10.0 for i in range(2, 9)]

        if random(1) > 0.5:
            u_w = lerp(0, self.w, choice(lerp_ranges))
            b_w = lerp(0, self.w, choice(lerp_ranges))
        if random(1) > 0.5:
            l_h = lerp(0, self.h, choice(lerp_ranges))
            r_h = lerp(0, self.h, choice(lerp_ranges))

        self.u = PVector(u_w, 0)
        self.b = PVector(b_w, self.h)
        self.l = PVector(0, l_h)
        self.r = PVector(self.w, r_h)

    def display(self):
        no_distortion = all([
            self.u.x == self.w / 2,
            self.b.x == self.w / 2,
            self.l.y == self.h / 2,
            self.r.y == self.h / 2,
        ])

        if no_distortion:
            stroke(BLACK)
        else:
            stroke(COMPLEMENTARY)

        with pushMatrix():
            translate(self.x, self.y)
            line(self.l.x, self.l.y, self.r.x, self.r.y)
            line(self.u.x, self.u.y, self.b.x, self.b.y)

    def connect_with_left(self, other_cross):
        self.l.y = other_cross.r.y

    def connect_with_up(self, other_cross):
        self.u.x = other_cross.b.x


class MyGrid(BaseGrid):

    def __init__(self, *args, **kwargs):
        super(MyGrid, self).__init__(*args, **kwargs)
        self.squares = {}
        self.ready_to_move = True

    def populate_squares(self):
        for elem in grid.get_grid_positions():
            key = (elem.i, elem.j)
            square = CellCross(elem)
            self.squares[key] = square


        for square in self.squares.values():
            upper_neighbor = self.get_upper_neighbor(square)
            if upper_neighbor:
                square.connect_with_up(upper_neighbor)
            left_neighbor = self.get_left_neighbor(square)
            if left_neighbor:
                square.connect_with_left(left_neighbor)

    def get_upper_neighbor(self, square):
        i, j = square.grid_elem.i, square.grid_elem.j
        if j == 0:
            return None
        k = (i, j - 1)
        return self.squares[k]

    def get_left_neighbor(self, square):
        i, j = square.grid_elem.i, square.grid_elem.j
        if i == 0:
            return None
        k = (i - 1, j)
        return self.squares[k]

    def display(self):
        for square in self.squares.values():
            square.display()


dimension = 900
row_size = 30.0
grid = MyGrid(0, 0, dimension / row_size, row_size)
grid.populate_squares()


def setup():
    size(dimension, dimension)
    background(WHITE)
    strokeWeight(4)


def draw():
    grid.display()
    saveFrame("cover.png")
    noLoop()