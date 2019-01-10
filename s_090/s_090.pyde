# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import draw_shape
from berin.coords import polar_coordinate

from random import shuffle, choice

WHITE = color(228)
BLACK = color(27, 27, 27)
RED = color(148, 22, 10)


GREEN = color(49, 114, 59)
WHITE = color(198)
RED = color(181, 12, 10)
BLACK = color(17, 17, 17)
GOLDEN = color(218, 145, 32)
COLORS = [
    WHITE,
    RED,
    BLACK,
    GOLDEN,
    GREEN,
]

class NestedSquares():

    def __init__(self, x, y, min_r, max_r, num_squares=3):
        self.x, self.y = x, y
        self.min_r, self.max_r = min_r, max_r
        self.num_squares = num_squares

    @property
    def interval(self):
        return int((self.max_r - self.min_r) / self.num_squares)


    def draw_squares(self):
        for r in sorted(range(self.min_r, self.max_r, self.interval), reverse=True):
            fill(choice(COLORS))
            angles = sorted([random(360) for i in range(6)])
            points = [
                polar_coordinate(self.x, self.y, r, radians(a)) for a in angles
            ]
            draw_shape(points, end_shape_mode=CLOSE, vertex_func=curveVertex)


nested_squares = []


def setup():
    size(900, 900)
    rectMode(CENTER)
    noFill()
    stroke(BLACK)
    strokeWeight(2.3)
    frameRate(0.2)


def draw():
    max_r = 90
    for x in range(0, width + max_r, max_r + 5):
        for y in range(0, height + max_r, max_r + 5):
            nested_squares.append(
                NestedSquares(x, y, 10, max_r, int(random(3, 9)))
            )

    background(RED)
    for square in nested_squares:
        square.draw_squares()

    #saveFrame("####.png")