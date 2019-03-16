# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.grids import VirtualGrid
from berin.save_frames import save_video_frames
from random import choice


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
colors = []


class Grid(VirtualGrid):

    def draw_elem(self, grid_elem, func, *f_args, **f_kwargs):
        func(grid_elem.i, grid_elem.j, self.grid_elem_size)


elem_size = 90.0
s = elem_size / 2
diff = 1

def pattern(i, j, size):
    global s
    half = size / 2
    offset = 5

    ellipse(half, half, s, s)


elem_size = 90.0
num_rows = 900 / elem_size


def setup():
    size(900, 900)
    stroke(BLACK)
    noFill()
    strokeWeight(3)
    frameRate(24)


    for i in range(int(num_rows)):
        colors.append(choice([
            BLACK
        ]))


def draw():
    global s, diff

    background(WHITE)
    grid = Grid(0, 0, num_rows, elem_size)
    grid.draw(pattern)


    s += diff
    if s > 4 * elem_size or s < elem_size / 2:
        diff *= -1

    saveFrame("########.png")