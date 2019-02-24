# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Based in https://generativeartistry.com/tutorials/hypnotic-squares/
# http://recodeproject.com/translation/kyle-mcdonald-direct-random-squares-william-kolomyjec

from berin.grids import *
from random import choice
from itertools import cycle


WHITE = color(235)
BLACK = color(27, 27, 27)

COLORS = [
    color(213, 12, 56),
    WHITE,
    color(235, 235, 0),
    color(235, 0, 235),
    color(0, 235, 235),
]
COLOR = choice(COLORS)

MAX_ELEM_SIZE = 200
class RecursivePackedSquare(object):

    def __init__(self, x, y, x_move, y_move, min_elem_size=10):
        self.x, self.y = x, y
        self.x_move, self.y_move = x_move, y_move
        self.size = MAX_ELEM_SIZE
        self.min_elem_size = min_elem_size

    @property
    def center_x(self):
        return self.x + self.radius

    @property
    def center_y(self):
        return self.y + self.radius

    @property
    def radius(self):
        return self.size / 2

    @property
    def total_rects(self):
        return int(map(self.size, self.min_elem_size, MAX_ELEM_SIZE, 1, 9))

    def get_x_range(self):
        return self.center_x - self.radius, self.center_x + self.radius

    def get_y_range(self):
        return self.center_y - self.radius, self.center_y + self.radius

    def is_colliding_with(self, square):
        x0, x1 = square.get_x_range()
        y0, y1 = square.get_y_range()

        if (x0 < self.center_x < x1 and y0 < self.center_y < y1):
            return True

        diff_x = abs(square.center_x - self.center_x)
        diff_y = abs(square.center_y - self.center_y)

        min_diff = square.radius + self.radius
        if diff_x < min_diff and diff_y < min_diff:
            return True

        return False


    def is_colliding(self):
        for square in packed_squares:
            if self.is_colliding_with(square):
                return True
        return False

    def resize(self):
        while self.is_colliding() and self.size > self.min_elem_size:
            self.size -= 1

    def display(self):
        self.recursive_display(self.x, self.y, self.size - 5, self.x_move, self.y_move, current_rect=self.total_rects - 1)

    def recursive_display(self, x, y, size, x_move, y_move, current_rect):
        max_w = map(self.size, self.min_elem_size, MAX_ELEM_SIZE, 1, 4)
        w = map(current_rect, -1, self.total_rects - 1, max_w, 1)
        a = map(current_rect, -1, self.total_rects - 1, 230, 100)

        r, g, b = red(COLOR), green(COLOR), blue(COLOR)
        stroke(r, g, b, a)
        strokeWeight(w)
        rect(x, y, size, size)

        if current_rect < 0:
            return

        new_size = self.size * float(current_rect) / self.total_rects + self.min_elem_size
        size_diff = size - new_size

        new_x = x + size_diff / 2
        new_y = y + size_diff / 2
        new_x -= (x - new_x) / float(current_rect + 2) * x_move
        new_y -= (y - new_y) / float(current_rect + 2) * y_move

        self.recursive_display(new_x, new_y, new_size, x_move, y_move, current_rect - 1)


def setup():
    size(904, 904)
    strokeWeight(1)
    noFill()
    stroke(WHITE)
    background(BLACK)
    noFill()
    smooth()


packed_squares = []
def draw():
    x = choice(range(0, width, 10))
    y = choice(range(0, height, 10))

    x_move = choice([-2, -1, 0, 1, 2])
    y_move = choice([-2, -1, 0, 1, 2])
    total_squares = int(random(3, 8))
    square = RecursivePackedSquare(x, y, x_move, y_move)
    square.resize()

    if not square.is_colliding():
        square.display()
        packed_squares.append(square)


def keyPressed():
    global COLOR, packed_squares

    if key == 'n':
        saveFrame("##########.png")
        COLOR = choice(COLORS)
        packed_squares = []
        background(BLACK)
        redraw()