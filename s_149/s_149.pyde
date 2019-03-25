# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from shape import ShapeWithInnerFilling, BLACK


elem_size = 90.0


class ShapesGrid(VirtualGrid):

    def __init__(self, *args, **kwargs):
        super(ShapesGrid, self).__init__(*args, **kwargs)
        self.shapes = {}
        for pos in self.get_grid_positions():
            key = (pos.i, pos.j)
            r = (elem_size - 3) / 2
            n_sides = int(random(3, 10))
            self.shapes[key] = ShapeWithInnerFilling.random_shape(r, r, r, n_sides)

    def draw_elem(self, grid_elem, *f_args, **f_kwargs):
        key = (grid_elem.i, grid_elem.j)
        shape = self.shapes[key]
        shape.update()
        shape.display()
        print(len(shape.vertices))

grid = None
def setup():
    global grid
    size(900, 900)
    background(BLACK)
    grid = ShapesGrid(0, 0, 900 / elem_size, elem_size)


def draw():
    global grid
    grid.draw("")

def keyPressed():
    if key == 's':
        saveFrame("########.png")
    elif key == 'n':
        global grid
        grid = ShapesGrid(0, 0, 900 / elem_size, elem_size)
        background(BLACK)
        redraw()