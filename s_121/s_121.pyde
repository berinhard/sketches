# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
import itertools
from random import choice
from copy import deepcopy, copy

from berin.save_frames import save_video_frames
from berin.grids import BaseGrid

WHITE = color(235)
BLACK = color(27, 27, 27)
COMPLEMENTARY = color(55,189,182)

class Cell(object):

    def __init__(self, grid_elem, live):
        self.x, self.y = grid_elem.x, grid_elem.y
        self.w, self.h = grid_elem.height, grid_elem.width
        self.live = live
        self.grid_elem = grid_elem

    def update_state(self, neighbors):
        """
        Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by overpopulation.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """
        live_neighbors = sum([1 for n in neighbors if n.live])
        if not self.live and live_neighbors == 3:
            self.live = True
        elif self.live:
            if live_neighbors < 2:
                self.live = False
            elif live_neighbors in [2, 3]:
                self.live = True
            else:
                self.live = False

        self.color = WHITE
        if live_neighbors == 3:
            self.color = COMPLEMENTARY

    def display(self):
        if self.live:
            fill(self.color)
        else:
            fill(BLACK)
        rect(self.x, self.y, self.w, self.h)


class GameOfLife(BaseGrid):

    def __init__(self, *args, **kwargs):
        super(GameOfLife, self).__init__(*args, **kwargs)
        self.cells = {}

    def initialize(self):
        for elem in self.get_grid_positions():
            key = (elem.i, elem.j)
            live = True if random(1) > 0.8 else False
            cell = Cell(elem, live)
            self.cells[key] = cell

    def get_neighbors(self, cell):
        i, j = cell.grid_elem.i, cell.grid_elem.j
        i_range = [new_i for new_i in [(i - 1) % self.num_rows, i, (i + 1) % self.num_rows]]
        j_range = [new_j for new_j in [(j - 1) % self.num_rows, j, (j + 1) % self.num_rows]]
        keys = [k for k in itertools.product(i_range, j_range) if not (k[0] == i and k[1] == j)]
        return [s for s in [self.cells[k] for k in keys]]

    def display(self):
        for cell in self.cells.values():
            cell.display()

    def new_generation(self):
        new_cells = {}

        for k, cell in self.cells.items():
            neighbors = self.get_neighbors(cell)
            new_cell = Cell(cell.grid_elem, cell.live)
            new_cell.update_state(neighbors)
            new_cells[k] = new_cell

        self.cells = new_cells


dimension = 900
row_size = 10.0
num_rows = dimension / row_size
conway = GameOfLife(0, 0, dimension / row_size, row_size)
conway.initialize()


def setup():
    size(dimension, dimension)
    noStroke()
#    frameRate(10)


def draw():
    background(BLACK)
    conway.new_generation()
    conway.display()
    #print(frameRate)

    save_video_frames(10, 30)
