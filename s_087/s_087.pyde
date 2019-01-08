# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import regular_polygon


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27, 35)
RED = color(181, 32, 10, 70)


radius = 300


def setup():
    size(700, 700)
    background(WHITE)
    strokeWeight(2)
    noFill()


def draw():
    global radius

    if frameCount % 2:
        stroke(BLACK)
    else:
        stroke(RED)

    rate = 0.8
    x, y = width / 2, height / 2
    n_sides = 3
    angle_rate = rate
    angle_rotation = radians(frameCount * angle_rate)
    regular_polygon(x, y, radius, n_sides, angle_rotation=angle_rotation)

    radius -= rate

    if abs(radius) >= 300:
        noLoop()
        saveFrame("r{}-a{}.png".format(n_sides, angle_rate))