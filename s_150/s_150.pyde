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


shapes = []

def init_shapes():
    global shapes

    v1, v2 = sorted([random(100, 450), random(100, 450)])
    v3, v4 = sorted([random(450, 800), random(450, 800)])

    shape_1_vectors = [
        PVector(v1, 100),
        PVector(v2, 100),
        PVector(v4, 800),
        PVector(v3, 800),
    ]
    shape_2_vectors = [
        PVector(800, v4),
        PVector(800, v3),
        PVector(100, v1),
        PVector(100, v2),
    ][::-1]
    shapes = [
        ShapeWithInnerFilling(shape_1_vectors, line_color=color(242, 127, 12, 1)),
        ShapeWithInnerFilling(shape_2_vectors),
    ]


def setup():
    global grid
    size(900, 900)
    background(242)
    init_shapes()

def draw():
    for shape in shapes:
        shape.update()
        shape.display()

def keyPressed():
    if key == 's':
        saveFrame("########.png")
    elif key == 'n':
        init_shapes()
        background(242)
        redraw()