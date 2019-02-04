# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Reference: https://generativeartistry.com/tutorials/circle-packing/
from random import choice, shuffle
from berin.coords import polar_coordinate
from berin.shapes import draw_shape



WHITE = color(228, 288, 288)
BLACK = color(27, 27, 27)
RED = color(218, 32, 10)
GOLDEN = color(218, 185, 32, 140)
GREEN = color(32, 181, 10)

MIN_RADIUS = 5
MAX_RADIUS = 130
CIRCLES = []


class PackedCircle():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.num_points = int(random(5, 11))


    def display(self):
        min_r = 10
        max_r = self.r * 2
        interval = 15
        angles = range(0, 360, 20)
        draw_radius = sorted(range(min_r, max_r, interval), reverse=True)

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


    def is_colliding(self, circles):
        if self.x + self.r >= width or self.x - self.r < 0:
            return True
        if self.y + self.r >= height or self.y - self.r < 0:
            return True

        for circle in circles:
            center_dist = self.r + circle.r
            x_diff = self.x - circle.x
            y_diff = self.y - circle.y

            if center_dist >= sqrt(x_diff ** 2 + y_diff ** 2):
                return True
        return False

    def shrink(self, rate=1):
        self.r -= rate

    @property
    def too_small(self):
        return self.r < 10


def setup():
    background(WHITE)
    noFill()
    stroke(BLACK)
    strokeWeight(2)
    size(1000, 1000)


def draw():
    attempts = 500

    while attempts:
        x, y = random(width), random(height)
        new_circle = PackedCircle(x, y, MAX_RADIUS)

        while not new_circle.too_small and new_circle.is_colliding(CIRCLES):
            new_circle.shrink()

        if not new_circle.too_small:
            new_circle.display()
            CIRCLES.append(new_circle)
            attempts = 0
        else:
            attempts -= 1

    print frameCount


def keyPressed():
    if key == 's':
        saveFrame("#######.png")