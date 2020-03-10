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

img = None


def setup():
    global img
    size(960, 1280)
    img = loadImage('img.jpg')

    offset_range = 30
    loadPixels()
    for x in range(width):
        offset = int(random(-offset_range, offset_range))
        for y in range(height):
            new_y = y + offset
            if new_y >= height:
                new_y = new_y - height

            pos = new_y * width + x
            pixels[pos] = img.get(x, y)

    updatePixels()


def draw():
    saveFrame("cover.png")
    noLoop()
