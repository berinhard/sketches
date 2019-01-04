# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)


def setup():
    size(1000, 1000)
    background(WHITE)
    stroke(BLACK)
    strokeWeight(2)


def draw():
    step = 30
    for j, y in enumerate(range(-height, height, step)):
        x = 0
        i = 0

        while x < height:
            if i % 2:
                angle = 90
            else:
                angle = 180

            a = radians(angle)
            r = choice([10, 20, 30, 50, 80])#]), 130])#, 210])
            new_x = x + abs(cos(a)) * r
            new_y = y + abs(sin(a)) * r

            line(x, y, new_x, new_y)
            x = new_x
            y = new_y
            i += 1

    noLoop()


def keyPressed():
    if key == 's':
        saveFrame("####.png")