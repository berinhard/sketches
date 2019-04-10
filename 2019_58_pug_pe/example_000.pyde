# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import uniform

def setup():
    size(800, 800)


def draw():
    # drawing a rectangle
    x, y, w, h = 10, 20, 100, 200
    fill(color(255, 0, 0))
    rect(x, y, w, h)

    # drawing a circle
    x, y, w, h = 300, 500, 200, 200
    fill(color(0, 255, 0))
    ellipse(x, y, w, h)

    # drawing a line
    x1, y1 = width / 2, height / 2
    x2, y2 = width, height
    line(x1, y1, x2, y2)

    # using python
    for x in range(width / 2, width, 20):
        y = 50
        y_offset = uniform(50, 200)
        line(x, y, x, y + y_offset)

    noLoop()