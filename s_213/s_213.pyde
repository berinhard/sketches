# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from itertools import cycle
from random import choice

max_r = 450
min_r = 10
angles = []
colors = cycle(get_color_palette())
nested_shapes = None


def init_angles(count):
    global angles, colors, nested_shapes

    colors = cycle(get_color_palette())
    nested_shapes = NestedShapes(count)
    frameRate(12)


class NestedShapes(object):

    def __init__(self, num_angles):
        self.angles = [random(TWO_PI) for i in range(num_angles)]
        #self.angles.sort()
        self.shapes_points = []
        self.saved = False

    def update(self):
        self.shapes_points = []

        for r in range(max_r, min_r, -15):
            points = []

            for i, angle in enumerate(self.angles):
                p = polar_coordinate(0, 0, r, angle)
                points.append(p)

            self.shapes_points.append((points, r))

    def display(self):
        display_min_r = min_r #* 10

        for points, r in self.shapes_points:
            if r <= display_min_r:
                return

            noFill()
            w = map(r, max_r, display_min_r, 7, 1)
            a = map(r, max_r, display_min_r, 10, 200)
            strokeWeight(w)
            stroke(242, 242, 242, a)
            draw_shape(points + points[:3], vertex_func=curveVertex)

        if not self.saved:
            #saveFrame("###########.png")
            self.saved = True

def setup():
    size(1200, 1200)
    init_angles(7)
    strokeWeight(4)


def draw():
    background(27)

    with draw_at_center():
        nested_shapes.update()
        nested_shapes.display()


def keyPressed():
    if key == 'n':
        init_angles(int(random(5, 14)))