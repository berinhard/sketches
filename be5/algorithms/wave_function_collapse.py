import random
from collections import deque
from dataclasses import dataclass, field
from functools import cached_property
from itertools import product
from pathlib import Path

import py5


@dataclass
class Tile:
    """
    This class represents a tile py5 image with its edge of possible connections.
    The edges list represents what are the possible type of connection between this tile and their
    neighbors. The position of the connection in edges list indicates the orientation of them.
    """

    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3  # neighbors indexes for the edges list

    edges: list
    image: py5.Image

    def __post_init__(self):
        if not len(self.edges) == 4:
            raise ValueError(f"Edges must be a list with 4 elements, got {len(self.edges)}")

    @classmethod
    def from_file(cls, filename, **kwargs):
        kwargs["image"] = py5.load_image(str(filename.resolve()))
        return cls(**kwargs)

    @property
    def up(self):
        return self.edges[self.UP]

    @property
    def down(self):
        return self.edges[self.DOWN]

    @property
    def left(self):
        return self.edges[self.LEFT]

    @property
    def right(self):
        return self.edges[self.RIGHT]

    def rotate(self, counter):
        """
        Rotate the image and edges by counter times and return an equivalent new Tile with this data
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

        return Tile(image=new_image, edges=edges)


@dataclass
class Cell:
    """
    A cell represents an area from the grid that will have a tile addressed to it. The i, j are the
    cell indexes within the grid and the tile attribute will be populated once this cell is
    collapsed. The options list holds all the possible tiles that can be assigned for the cell.
    """

    i: int
    j: int
    options: list
    tile: Tile = field(default=None, init=False)

    @property
    def collapsed(self):
        return self.tile is not None

    def collapse(self):
        self.tile = random.choice(self.options)

    @property
    def entropy(self):
        """
        The entropy is the number of possible options which are still open for this cell
        """
        if self.collapsed:
            return 0
        return len(self.options)

    def update_options(self, collapsed_cell):
        """
        Considering the collapsed cell, this method will determine the neighborhood orientation
        between them and, accordingly to that, limit down the options considering the collapsed
        adjacency rules.
        """
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
    """
    Class to represent a grid which will be populated by collapsing their cells.
    """

    tiles: list
    dim: int
    pending_cells: list[Cell] = field(default=list, init=False)

    def __post_init__(self):
        self.pending_cells = self.cells[:]  # copy of cells, so we can know which aren't collapsed
        random.shuffle(self.pending_cells)

    @property
    def w(self):
        return py5.width // self.dim

    @property
    def h(self):
        return py5.height // self.dim

    @cached_property
    def cells(self):
        return [
            Cell(i=i, j=j, options=self.tiles[:])  # cells initialized with all tiles as possibles
            for i, j in product(range(0, py5.width // self.w), range(0, py5.height // self.h))
        ]

    def start(self):
        """
        To start the algorithm, we pick any random cell and collapse it since all of them have the
        same set of possible tiles.
        """
        cell = random.choice(self.cells)
        self.collapse_cell(cell)

    def collapse_cell(self, cell):
        # defines the cell tile among their options
        cell.collapse()
        # remove the collapsed cell from the pending ones list
        self.pending_cells.remove(cell)
        # update all the neighbors cells options considering the collapse operation
        for neighbor_cell in self.get_neighbors(cell):
            neighbor_cell.update_options(collapsed_cell=cell)

    def get_neighbors(self, cell):
        """
        Given a cell, return its list of neighbors which still weren't collapsed.
        """
        i, j = cell.i, cell.j
        positions = [
            (i, j - 1),
            (i, j + 1),
            (i - 1, j),
            (i + 1, j),
        ]

        return [
            c for c in self.pending_cells if all(((c.i == i or c.j == j), (c.i, c.j) in positions))
        ]

    @property
    def complete(self):
        return not self.pending_cells

    def collapse(self):
        """
        Gets the next pending cell with the lowes entropy and collapses it
        """
        next_cell = sorted(grid.pending_cells, key=lambda c: c.entropy)[0]
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
    blank = Tile.from_file(images_dir / "0.png", edges=[0, 0, 0, 0])
    ptr_1 = Tile.from_file(images_dir / "1.png", edges=[0, 1, 1, 1])
    ptr_2 = Tile.from_file(images_dir / "2.png", edges=[0, 1, 0, 1])

    tiles = [
        blank,
        ptr_1,
        ptr_1.rotate(1),
        ptr_1.rotate(2),
        ptr_1.rotate(3),
        ptr_2,
        ptr_2.rotate(1),
    ]
    grid = WaveFunctionCollapseGrid(dim=40, tiles=tiles)
    grid.start()


def draw():
    grid.collapse()
    grid.draw()

    if grid.complete:
        print("finished!")
        py5.no_loop()


py5.run_sketch()
