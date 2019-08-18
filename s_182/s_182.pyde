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
    size(int(900*4.166),int(900*4.166))
    strokeWeight(10)

BACKGROUND = 27
COLORS = get_color_palette()
def draw():
    """
    This sketch is a study of Vasa Mihich's artwork "Painting #207"
    """

    scale(300/72.0);
    global COLORS
    background(BACKGROUND)
    spacing = 30
    vertical_lines = [
        (x, 0, x, height, choice(COLORS))
        for x in range(0, width + spacing, spacing)
    ]
    horizontal_lines = [
        (0, y, width, y, choice(COLORS))
        for y in range(0, height + spacing, spacing)
    ]

    lines_set_order = [
        vertical_lines[0::2],
        horizontal_lines[0::2],
        vertical_lines[1::2],
        horizontal_lines[1::2]
    ]

    for lines_set in lines_set_order:
        for x1, y1, x2, y2, c in lines_set:
            stroke(c)
            line(x1, y1, x2, y2)

    noLoop()

def keyPressed():
    global COLORS
    if key == 'n':
        redraw()
    if key == 'x':
        COLORS = ['#bdbf90', '#35352b', '#e7e9c4', '#ec6c2b', '#feae4b']
        redraw()
    if key == 'c':
        COLORS = ['#a1dbb2', '#fee5ad', '#faca66', '#f7a541', '#f45d4c']
        redraw()
    if key == 's':
        name = str(COLORS)
        print(name)
        saveFrame("#####{}.png".format(name))
