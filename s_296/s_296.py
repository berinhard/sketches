from pathlib import Path

import py5

from be5.algorithms.wave_function_collapse import Tile, WaveFunctionCollapseGrid

grid = None


def setup():
    global grid
    py5.size(900, 900)

    images_dir = Path(__file__).parents[1] / "be5" / "algorithms" / "tiles" / "demo"
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
    grid = WaveFunctionCollapseGrid(dim=30, tiles=tiles)
    grid.start()


def draw():
    grid.collapse()
    grid.draw()

    if grid.complete:
        print("finished!")
        py5.save_frame("cover.png")
        py5.no_loop()


py5.run_sketch()
