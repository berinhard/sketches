# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Live demo: https://berinhard.github.io/sketches/s_195/
# Created with https://github.com/berinhard/pyp5js
from pyp5js import *
from random import choice


square_size = 100
squares_map = {}


def lines_intersection(p1, p2, p3, p4):
    """
    p1 and p2 are points from line 1 while p3 and p4 are points from line 2
    """
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    x3, y3 = p3.x, p3.y
    x4, y4 = p4.x, p4.y

    try:
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) // ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) // ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
    except ZeroDivisionError:
        return

    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return

    x = x1 + uA * (x2 - x1)
    y = y1 + uA * (y2- y1)

    return createVector(x, y)


class Square:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.possible_coords = [
            (self.x, self.y + self.size, self.x, self.y, self.x + self.size, self.y + self.size),
            (self.x + self.size, self.y, self.x, self.y, self.x + self.size, self.y + self.size),
            (self.x, self.y, self.x, self.y + self.size, self.x + self.size, self.y),
            (self.x + self.size, self.y + self.size, self.x, self.y + self.size, self.x + self.size, self.y),
        ]
        self.coords = choice(self.possible_coords)

    def display(self):
        noStroke()
        fill(27)
        triangle(*self.coords)

        v1 = createVector(self.coords[0], self.coords[1])
        v2 = createVector(self.coords[2], self.coords[3])
        v3 = createVector(self.coords[4], self.coords[5])

        start = v1
        if random(1) > 0.5:
            end = v2
        else:
            end = v3

        inc = 0.1
        step = inc
        while step < 1:
            pos = createVector(
                lerp(start.x, end.x, step),
                lerp(start.y, end.y, step),
            )

            intersection = None
            if end == v2:
                intersection = lines_intersection(v2, v3, pos, createVector(v3.x, pos.y))
            else:
                intersection = lines_intersection(v2, v3, pos, createVector(pos.x, v2.y))

            stroke(240)
            if intersection:
                line(pos.x, pos.y, intersection.x, intersection.y)

            step += inc

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if self._alpha + value < 255:
            self._alpha += value


def setup():
    pixelDensity(displayDensity())
    w, h = window.innerWidth, window.innerHeight
    createCanvas(w, h)
    for x in range(0, w, square_size):
        for y in range(0, h, square_size):
            squares_map[(x, y)] = Square(x, y, square_size)


def draw():
    background(240)

    for square in squares_map.values():
        square.display()

    noLoop()
