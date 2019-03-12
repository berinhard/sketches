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


def bezier_line(i, j, size):
    half = size / 2
    offset = 5

    stroke(colors[j])
    with pushMatrix():
        angle = QUARTER_PI / 10 * i * j
        step = (frameCount + i * j) * 0.1
        angle += map(noise(step), 0, 1, 0, QUARTER_PI)
        w = map(angle, 0, HALF_PI, 1, 3)
        strokeWeight(w)
        #rotate(QUARTER_PI)
        translate(half, half)
        rotate(angle)
        line(offset * 2 - half, 0, offset * 2, 0)


elem_size = 50.0
num_rows = 900 / (elem_size - 1)


def setup():
    size(900, 900)
    stroke(WHITE)
    strokeWeight(2)
    frameRate(24)

    for i in range(int(num_rows) + 1):
        colors.append(choice([
            color(235, 235, 0),
            color(235, 0, 235),
            color(0, 235, 235),
            WHITE,
        ]))


def draw():
    background(BLACK)
    grid = Grid(0, 0, num_rows, elem_size)
    grid.draw(bezier_line)

    saveFrame("cover.png")
    #save_video_frames(24, 60)