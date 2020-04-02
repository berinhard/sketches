# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Reference: https://generativeartistry.com/tutorials/circle-packing/
from random import choice, shuffle
from berin.coords import polar_coordinate
from berin.shapes import draw_shape

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
        rate = TWO_PI / self.num_points
        counter = int(map(self.r, MIN_RADIUS, MAX_RADIUS, 5, 30))
        for j in range(counter):
            for i in range(self.num_points + 1):
                angle = rate * i + random(1) * TWO_PI
                v = PVector.random2D()
                v.rotate(angle)
                v.mult(self.r)
                v.add(PVector(self.x, self.y))

                BLACK = color(27, 27, 27, 56)
                stroke(BLACK)
                strokeWeight(2)
                line(self.x, self.y, v.x, v.y)

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
    background(242)
    noFill()
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


def keyPressed():
    if key == 's':
        saveFrame("#######.png")