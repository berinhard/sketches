# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import draw_shape
from berin.coords import polar_coordinate

from random import shuffle, choice

WHITE = color(228)
BLACK = color(27, 27, 27)
RED = color(148, 22, 10)

class NestedShapes():

    def __init__(self, x, y, min_r, max_r, num_shapes=3):
        self.x, self.y = x, y
        self.min_r, self.max_r = min_r, max_r
        self.num_shapes = num_shapes
        self.num_points = int(random(5, 11))

    @property
    def interval(self):
        return int((self.max_r - self.min_r) / self.num_shapes)


    def draw_shapes(self):
        angles = range(0, 360, 20)
        draw_radius = sorted(range(self.min_r, self.max_r, self.interval), reverse=True)
        weight_rate = 2.9 / len(draw_radius)

        with pushMatrix():
            translate(self.x, self.y)

            for i, r in enumerate(draw_radius):
                rotate(radians(random(360)))
                draw_angles = sorted([choice(angles) for x in range(self.num_points)])
                points = [
                    polar_coordinate(0, 0, r / 2, radians(a)) for a in draw_angles
                ]

                strokeWeight((i + 1) * weight_rate)
                draw_shape(points, vertex_func=curveVertex)


def setup():
    size(850, 850)
    noFill()
    stroke(WHITE)
    strokeWeight(2.3)
    frameRate(1)


def draw():
    nested_shapes = []

    max_r = 90
    for x in range(0, width + max_r, max_r + 5):
        for y in range(0, height + max_r, max_r + 5):
            nested_shapes.append(
                NestedShapes(x, y, 10, max_r, int(random(3, 9)))
            )

    background(BLACK)
    for shape in nested_shapes:
        shape.draw_shapes()

    #saveFrame("####.png")