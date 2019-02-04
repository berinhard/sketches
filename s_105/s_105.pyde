# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Reference: https://generativeartistry.com/tutorials/circle-packing/
from random import choice, shuffle
from berin.coords import polar_coordinate
from berin.shapes import draw_shape, regular_polygon


WHITE = color(230, 230, 230)
BLACK = color(27, 27, 27, 35)
RED = color(181, 32, 10, 70)

MIN_RADIUS = 5
MAX_RADIUS = 400
CIRCLES = []


class PackedCircle():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.radius = r
        self.n_sides = int(random(4, 9))


    def display(self):
        if abs(self.radius) > self.r:
            return

        if frameCount % 2:
            stroke(BLACK)
        else:
            stroke(RED)

        rate = 0.8
        x, y = self.x, self.y
        angle_rate = rate
        angle_rotation = radians(frameCount * angle_rate)
        regular_polygon(x, y, self.radius, self.n_sides, angle_rotation=angle_rotation, end_shape_mode=CLOSE)

        self.radius -= rate


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
        self.radius = self.r

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

    while attempts and len(CIRCLES) < 270:
        x, y = random(width), random(height)
        new_circle = PackedCircle(x, y, MAX_RADIUS)

        while not new_circle.too_small and new_circle.is_colliding(CIRCLES):
            new_circle.shrink()

        if not new_circle.too_small:
            CIRCLES.append(new_circle)
            attempts = 0
        else:
            attempts -= 1

    print(len(CIRCLES), frameCount)
    for c in CIRCLES:
        c.display()


def keyPressed():
    if key == 's':
        saveFrame("#######.png")