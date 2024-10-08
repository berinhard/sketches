from pathlib import Path

import py5

from be5.algorithms.wave_function_collapse import Tile, WaveFunctionCollapseGrid

grid = None


def setup():
    global grid
    py5.size(1000, 1000)

    images_dir = Path(__file__).parents[1] / "be5" / "algorithms" / "tiles" / "polka"
    images_dir = Path(__file__).parent / "polka"
    blank = Tile.from_file(images_dir / "0.png", edges=[0, 0, 0, 0])
    ptr_1 = Tile.from_file(images_dir / "1.png", edges=[0, 1, 1, 1])
    ptr_2 = Tile.from_file(images_dir / "2.png", edges=[0, 1, 0, 1])
    ptr_3 = Tile.from_file(images_dir / "3.png", edges=[0, 1, 0, 0])

    tiles = [
        blank,
        ptr_1,
        ptr_1.rotate(1),
        ptr_1.rotate(2),
        ptr_1.rotate(3),
        ptr_2,
        ptr_2.rotate(1),
        ptr_3,
        ptr_3.rotate(1),
        ptr_3.rotate(3),
    ]
    grid = WaveFunctionCollapseGrid(dim=40, tiles=tiles)
    grid.start()


def draw():
    grid.collapse()
    grid.draw()

    py5.save_frame(f"{py5.frame_count:05d}.png")

    if grid.complete:
        print("finished!")
        py5.no_loop()


py5.run_sketch()
