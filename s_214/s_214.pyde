# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings


def setup():
    size(700, 280)
    colorMode(HSB, 255)

def draw():
    num_rects = 7
    rect_height = height / num_rects
    y_positions = range(0, height, rect_height)

    for y in y_positions:
        color_pos = map(y, 0, height, 0, 255)  # not Python's map
        fill(color_pos, 210, 210)
        stroke(27)
        strokeWeight(2)
        rect(0, y, width, y + rect_height)

    #saveFrame("cover.png")