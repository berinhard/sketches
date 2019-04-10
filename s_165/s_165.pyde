# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice, shuffle

WHITE = color(240, 240, 240)
BLACK = color(27, 27, 27)

x_range = range(0, 901, 10)
y_range = range(0, 901, 10)
sizes = range(5, 406, 10)

def setup():
    size(900, 900)
    background(WHITE)
    stroke(BLACK)
    strokeWeight(2)
    strokeCap(SQUARE)


def recursive_interpolate_line(p1, p2, depth):
    w = map(depth, 5, 0, 4, 12)
    a = map(depth, 5, 0, 255, 10)
    strokeWeight(w)
    stroke(color(27, 27, 27, a))

    line(p1.x, p1.y, p2.x, p2.y)
    if not depth:
        return

    horizontal_line = False
    if int(p1.x) == int(p2.x):
        horizontal_line = True

    percents = [i / float(10) for i in range(2, 9)]
    shuffle(percents)
    for i in range(1 + int(random(len(percents)))):
        percent = percents.pop()

        p1 = PVector.lerp(p1, p2, percent)
        size = choice(sizes)
        if random(1) > 0.5:
            size *= -1

        if horizontal_line:
            p2 = PVector(int(p1.x + size), int(p1.y))
        else:
            p2 = PVector(int(p1.x), int(p1.y + size))

        recursive_interpolate_line(p1, p2, depth - 1)


def draw():
    background(WHITE)

    x = choice(x_range)
    y = choice(y_range)
    size = choice(sizes[len(sizes) / 2:])
    x, y = 100, height / 2
    p1 = PVector(x, y)
    p2 = PVector(x + size, y)

    recursive_interpolate_line(p1, p2, 5)

    noLoop()


def keyPressed():
    if key == 'n':
        redraw()
    if key == 's':
        saveFrame("####.png")