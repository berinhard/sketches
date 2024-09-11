import random
from dataclasses import dataclass
from functools import cached_property
from itertools import product
from pathlib import Path

import py5

IMAGES = sorted(list(Path("/home/bernardo/envs/sketches/be5/algorithms/tiles").glob("*.png")))
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

@dataclass
class Tile:
    filename: Path
    edges: list

    @cached_property
    def image(self):
        return py5.load_image(str(self.filename.resolve()))

    @property
    def up(self):
        return self.edges[UP]

    @property
    def down(self):
        return self.edges[DOWN]

    @property
    def left(self):
        return self.edges[LEFT]

    @property
    def right(self):
        return self.edges[RIGHT]
@dataclass
class Cell:
    i: int
    j: int
    options: list
    tile: Tile = None

    @property
    def collapsed(self):
        return self.tile is not None

    def collapse(self):
        self.tile = random.choice(self.options)

    @property
    def entrophy(self):
        return len(self.options)

    def update_options(self, collapsed_cell):
        ref_tile = collapsed_cell.tile
        if self.i == collapsed_cell.i:
            if self.j > collapsed_cell.j:
                cond = lambda tile: tile.up == ref_tile.down
            else:
                cond = lambda tile: tile.down == ref_tile.up
        else:
            if self.i > collapsed_cell.i:
                cond = lambda tile: tile.left == ref_tile.right
            else:
                cond = lambda tile: tile.right == ref_tile.left
        self.options = list(filter(cond, self.options))

@dataclass
class WaveFunctionCollapseGrid:
    tiles: list
    dim: int

    @property
    def w(self):
        return py5.width // self.dim

    @property
    def h(self):
        return py5.height // self.dim

    @cached_property
    def cells(self):
        return [
            Cell(i=i, j=j, options=self.tiles[:])
            for i, j in product(range(0, py5.width // self.w), range(0,  py5.height // self.h))
        ]

    def start(self):
        cell = random.choice(self.cells)
        self.collapse_cell(cell)

    def collapse_cell(self, cell):
        cell.collapse()
        for neighbor_cell in self.get_neighbors(cell):
            neighbor_cell.update_options(collapsed_cell=cell)
    def get_neighbors(self, cell):
        i, j = cell.i, cell.j
        positions = [
            (i, j - 1),
            (i, j + 1),
            (i - 1, j),
            (i + 1, j),
        ]
        return [c for c in self.pending_cells if (c.i, c.j) in positions]

    @property
    def pending_cells(self):
        return [c for c in self.cells if not c.collapsed]

    @property
    def complete(self):
        return not self.pending_cells

    def collapse(self):
        next_cell = next(iter(sorted(grid.pending_cells, key=lambda c: c.entrophy)))
        grid.collapse_cell(next_cell)

    def draw(self):
        for cell in self.cells:
            if cell.collapsed:
                py5.image(cell.tile.image, cell.i * self.w, cell.j * self.h, self.w, self.h)
            else:
                py5.fill(0)
                py5.stroke(100)
                py5.rect(cell.i * self.w, cell.j * self.h, self.w, self.h)

grid = None
def setup():
    global grid
    py5.size(800, 800)
    tiles = [
        Tile(filename=IMAGES[0], edges=[0, 0, 0, 0]),  # blank
        Tile(filename=IMAGES[1], edges=[0, 1, 1, 1]),  # down
        Tile(filename=IMAGES[2], edges=[1, 0, 1, 1]),  # left
        Tile(filename=IMAGES[3], edges=[1, 1, 1, 0]),  # right
        Tile(filename=IMAGES[4], edges=[1, 1, 0, 1]),  # up
        Tile(filename=IMAGES[5], edges=[0, 1, 0, 1]),  # horizontal
        Tile(filename=IMAGES[6], edges=[1, 0, 1, 0]),  # vertical
    ]
    grid = WaveFunctionCollapseGrid(dim=20, tiles=tiles)
    grid.start()

def draw():
    grid.collapse()
    grid.draw()

    if grid.complete:
        print("finished!")
        py5.no_loop()

py5.run_sketch()
