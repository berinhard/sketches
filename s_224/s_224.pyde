# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice


def setup():
    size(900, 900)
    background(27)
    strokeWeight(3)

colors = []
def draw():
    col_width = width / 5
    x_pos = range(0, width + col_width, col_width)

    y_pos = []

    px = 0
    py = 0
    for x in x_pos:
        y = int(choice(range(0, height + 30, 30)))
        while y == py:
            y = int(choice(range(0, height + 30, 30)))

        if x == x_pos[0]:
            py = y

        line(px + 1, py, x - 1, y)
        stroke(240, 12, 240, 1)

        px, py = x, y

def keyPressed():
    if key == 's':
        saveFrame("cover.png")