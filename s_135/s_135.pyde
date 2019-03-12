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
        num_angles = 8.0
        angle = TWO_PI / num_angles * int(random(num_angles))

        translate(half, half)
        rotate(angle)


        offset = 10
        min_value = offset - half
        max_value = half - offset
        v_range = [min_value, max_value]
        x1, y1 = min_value, random(*v_range)  # control point 1
        x2, y2 = random(*v_range), random(*v_range)  # anchor point 1
        x3, y3 = random(*v_range), random(*v_range)  # anchor point 2
        x4, y4 = max_value, 0  # control point 2
        noFill()
        bezier(x1, y1, x2, y2, x3, y3, x4, y4)


elem_size = 90.0
num_rows = 900 / elem_size + 1


def setup():
    size(900, 900)
    stroke(WHITE)
    strokeWeight(3)
    frameRate(24)

    for i in range(int(num_rows)):
        colors.append(choice([
            BLACK
        ]))


def draw():
    translate(10, 10)
    background(WHITE)
    grid = Grid(0, 0, num_rows, elem_size)
    grid.draw(bezier_line)

    saveFrame("#####.png")