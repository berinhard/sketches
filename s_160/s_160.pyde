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
WHITE = color(242, 242, 242, 1)
COLORS = [WHITE, GOLD, GOLD, GOLD]


WIDTH, HEIGTH = 800, 800
x_range = range(-20, WIDTH + 21, 20)
y_range = range(40, HEIGTH - 39, 40)

available_y = []

def init_sketch(draw_background=True):
    global base_y, available_y

    num_y = len(y_range)
    index = int(random(num_y / 3))
    base_y = y_range[index]
    available_y = y_range[index+1:]

    if draw_background:
        background(BLACK)
    stroke(WHITE)
    strokeWeight(2.5)
    print(frameCount)


def setup():
    size(WIDTH, HEIGTH)
    init_sketch()

def draw():
    px = 0

    lines = []
    for i, x in enumerate(x_range):
        if not(i  % 2):
            y = base_y
        else:
            y = choice(available_y)
        lines.append((px, y, x, y))

        px = x

    for i, data in enumerate(lines[1:]):
        if random(1) > 0.3:
            continue

        stroke(choice(COLORS))
        i += 1
        x1, y1, x2, y2 = data
        line(x1, y1, x2, y2)
        px1, py1, px2, py2 = lines[i - 1]
        line(x1, y1, px2, py2)

    init_sketch(draw_background=False)

def keyPressed():
    if key == 'n':
        init_sketch()
        redraw()
    elif key == 's':
        saveFrame("########.png")