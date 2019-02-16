# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
import itertools
from random import choice

from berin.save_frames import save_video_frames
from berin.grids import BaseGrid

WHITE = color(235)
BLACK = color(27, 27, 27)
COMPLEMENTARY = color(55,189,182)

class MovingSquare(object):

    def __init__(self, grid_elem):
        self.update(grid_elem)

    def update(self, grid_elem, moved=False, color=WHITE):
        self.grid_elem = grid_elem
        self.x, self.y = grid_elem.x, grid_elem.y
        self.w, self.h = grid_elem.height, grid_elem.width
        self.moved = moved
        if not self.moved:
            self.color = WHITE
        else:
            self.color = color

    def display(self):
        fill(self.color)
        rect(self.x, self.y, self.w, self.h)

    def switch_with(self, other_square):
        grid_elem = self.grid_elem
        self.update(other_square.grid_elem, moved=True, color=BLACK)
        other_square.update(grid_elem, moved=True, color=COMPLEMENTARY)


class MyGrid(BaseGrid):

    def __init__(self, *args, **kwargs):
        super(MyGrid, self).__init__(*args, **kwargs)
        self.squares = {}
        self.ready_to_move = True
        self.not_moved = []

    def populate_squares(self):
        for elem in grid.get_grid_positions():
            key = (elem.i, elem.j)
            square = MovingSquare(elem)
            self.squares[key] = square
            self.not_moved.append(square)

    def get_neighbors(self, square):
        i, j = square.grid_elem.i, square.grid_elem.j
        i_range = [new_i for new_i in [i - 1, i, i + 1] if 0 <= new_i < self.num_rows]
        j_range = [new_j for new_j in [j - 1, j, j + 0] if 0 <= new_j < self.num_rows]
        keys = [k for k in itertools.product(i_range, j_range) if not (k[0] == i and k[1] == j)]
        return [s for s in [self.squares[k] for k in keys] if not s.moved]

    def switch_squares(self):
        square = choice(self.not_moved)
        neighbors = self.get_neighbors(square)
        if neighbors:
            to_switch = choice(neighbors)
            square.switch_with(to_switch)
            self.not_moved.remove(square)
            self.not_moved.remove(to_switch)

    def display(self):
        for square in self.squares.values():
            square.display()


dimension = 900
row_size = 20.0
grid = MyGrid(0, 0, dimension / row_size, row_size)
grid.populate_squares()


def setup():
    size(dimension, dimension)
    background(WHITE)
    stroke(BLACK)
    strokeWeight(2)


def draw():
    grid.display()
    grid.switch_squares()

