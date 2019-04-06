# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice


BLACK = color(27, 27, 27)
RED = color(183, 15, 38, 1)
PURPLE = color(235, 0, 235, 1)
GOLD = color(235, 235, 0, 1)
CYAN = color(0, 235, 235, 1)
GREEN = color(51, 255, 51, 20)
WHITE = color(242, 242, 242)
#COLORS = [WHITE]
COLORS = get_color_palette()


WIDTH, HEIGTH = 800, 800
x_range = range(-WIDTH, WIDTH * 3, 120)
y_range = range(-HEIGTH, HEIGTH + 41, 40)

available_y = []

def init_sketch():
    global base_y, available_y, COLORS

    index = int(random(len(y_range) / 4.0)) + 1
    base_y = y_range[-index]
    available_y = y_range[index:-index]

    strokeWeight(16)
    strokeCap(PROJECT)
    print(frameCount)
    COLORS = get_color_palette()


def setup():
    size(WIDTH, HEIGTH)
    init_sketch()

def draw():
    background(WHITE)
    px = 0


    lines = []
    for i, x in enumerate(x_range):
        if not(i  % 2):
            y = base_y
        else:
            y = choice(available_y)
        lines.append((px, y, x, y))

        px = x

    for y in sorted(range(0, HEIGTH, 50), reverse=True):
        with pushMatrix():
            translate(y * 2, y * 2)
            stroke(choice(COLORS))
            for i, data in enumerate(lines[1:]):
                i += 1
                x1, y1, x2, y2 = data
                line(x1, y1, x2, y2)
                px1, py1, px2, py2 = lines[i - 1]
                line(x1, y1, px2, py2)

    print(len(lines))
    noLoop()

def keyPressed():
    if key == 'n':
        init_sketch()
        redraw()
    elif key == 's':
        saveFrame("########.png")