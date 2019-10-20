# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import BaseGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice




class Grid(BaseGrid):

    def draw(self, *f_args, **f_kwargs):
        for grid_elem in self.get_grid_positions():
            with pushMatrix():
                translate(grid_elem.x, grid_elem.y)
                self.draw_elem(grid_elem, *f_args, **f_kwargs)

    def draw_elem(self, grid_elem, *f_args, **f_kwargs):
        x, y = grid_elem.x, grid_elem.y
        i, j = grid_elem.i, grid_elem.j

        if i == j:
            return
        elif i > j:
            rect(x, y, 10 * (sqrt(i + 1)), 10 * j)
        else:
            rect(x, y, 10 * i, 10 * (sqrt(j + 1)), )



def setup():
    size(900, 900)
    noFill()
    background(240)
    stroke(27, 27, 27, 45)
    strokeWeight(2)


def draw():
    grid = Grid(0, 0, width / 10, 10)
    grid.draw()
    saveFrame("cover.png")
    noLoop()