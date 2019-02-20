# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Based in https://generativeartistry.com/tutorials/hypnotic-squares/
# http://recodeproject.com/translation/kyle-mcdonald-direct-random-squares-william-kolomyjec

from berin.grids import *
from random import choice
from itertools import cycle


WHITE = color(235)
BLACK = color(27, 27, 27)

elem_size = 100


def setup():
    size(904, 904)
    strokeWeight(1)
    noFill()
    frameRate(2)
    stroke(WHITE)
    background(BLACK)
    noFill()
    smooth()


class RecursiveSquares(object):

    def __init__(self, x, y, size, total_rects, min_elem_size=5):
        self.x, self.y = x, y
        self.size = size
        self.total_rects = total_rects
        self.min_elem_size = min_elem_size

    def display(self, x_move, y_move):
        self.recursive_display(self.x, self.y, self.size, x_move, y_move, current_rect=self.total_rects - 1)


    def recursive_display(self, x, y, size, x_move, y_move, current_rect):
        w = map(current_rect, -1, self.total_rects - 1, 3, 1)
        a = map(current_rect, -1, self.total_rects - 1, 230, 100)
        stroke(213, 12, 56, a)
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


def nested_squares():
    num_rects = int(random(4, 9))
    recursive_squares = RecursiveSquares(4, 4, elem_size - 4, num_rects)
    x_move = choice([-1, 0, 1])
    y_move = choice([-1, 0, 1])
    recursive_squares.display(x_move, y_move)


def draw():
    num_rows = width / elem_size + 1
    main_grid = VirtualGrid(0, 0, num_rows, elem_size)
    main_grid.draw(nested_squares)

    saveFrame("cover.png")
    noLoop()


def keyPressed():
    if key == 'n':
        redraw()
