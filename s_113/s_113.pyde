# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
import math

WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)

def setup():
    size(600, 900)
    background(WHITE)
    stroke(BLACK)
    strokeWeight(3)


def recursive_rect_decomposition(x_start, x_end, y, step, num_divisions):
    if y < 0:
        return

    num_divisions += 1.0
    interval = (x_end - x_start) / num_divisions

    x = x_start

    while math.ceil(x) < x_end:
        if random(1) > 0.83:
            fill(RED)
        else:
            fill(WHITE)
        rect(x, y, interval, step)
        x += interval

    recursive_rect_decomposition(x_start, x_end, y - step, step, num_divisions)


def draw():
    offset = 200
    w = width - offset
    h = height - offset

    translate(offset / 2, offset / 2)
    rect(0, 0, w, h)
    step = 50
    recursive_rect_decomposition(0, w, h - step, step, 1)

    saveFrame("cover.png")
    noLoop()