# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin repo: https://github.com/berinhard/berin
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice


COLORS = get_color_palette()


BACKGROUND = color(240)
WIDTH, HEIGHT = 900, 900
ROW_SIZE = 30
NUM_ROWS = WIDTH / ROW_SIZE + 1
grid = VirtualGrid(0, 0, NUM_ROWS, ROW_SIZE)


def pattern():
    w, h = ROW_SIZE, ROW_SIZE
    lines = [
        (0, 0, w, h),
        (w / 2, 0, w / 2, h),
        (0, h, w, 0),
        (0, h / 2, w, h / 2),
    ]
    strokeWeight(8)
    stroke(choice(COLORS))
    line(*choice(lines))


def setup():
    size(WIDTH, HEIGHT)
    background(BACKGROUND)
    strokeCap(PROJECT)


def draw():
    background(BACKGROUND)
    grid.draw(pattern)
    noLoop()

def keyPressed():
    if key == 'n':
        redraw()
    elif key == 'c':
        global COLORS
        COLORS = get_color_palette()
        redraw()
    elif key == 'b':
        global BACKGROUND
        if BACKGROUND == color(240):
            BACKGROUND = color(27)
        else:
            BACKGROUND = color(240)
        redraw()
    elif key == 's':
        saveFrame("#######.png")