import random
from collections import deque
from dataclasses import dataclass
from functools import cached_property
from itertools import product
from pathlib import Path

import py5

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

@dataclass
class Tile:
    edges: list
    filename: Path = ""
    p5_image: py5.Image = None

    @cached_property
    def image(self):
        if not self.p5_image:
            self.p5_image = py5.load_image(str(self.filename.resolve()))
        return self.p5_image

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

    def rotate(self, counter):
        """
        Rotate the image and edges by counter times and return an equivalent new Tile
        """
        w = self.image.width
        h = self.image.height

        new_image = py5.create_graphics(w, h)
        new_image.begin_draw()
        new_image.image_mode(py5.CENTER)
        new_image.translate(w // 2, h // 2)
        new_image.rotate(py5.HALF_PI * counter)
        new_image.image(self.image, 0, 0)
        new_image.end_draw()

        edges = deque(self.edges)
        edges.rotate(counter)

        return Tile(p5_image=new_image, edges=edges)
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

    images_dir = Path.home() / "envs" / "sketches" / "be5" / "algorithms" / "tiles" / "demo"
    blank = Tile(filename=images_dir / "0.png", edges=[0, 0, 0, 0])
    ptr_1 = Tile(filename=images_dir / "1.png", edges=[0, 1, 1, 1])
    ptr_2 = Tile(filename=images_dir / "2.png", edges=[0, 1, 0, 1])

    tiles = [
        blank,
        ptr_1,
        ptr_1.rotate(1),
        ptr_1.rotate(2),
        ptr_1.rotate(3),
        ptr_2,
        ptr_2.rotate(1),
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
