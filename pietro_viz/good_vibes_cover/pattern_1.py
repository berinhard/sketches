#!/usr/bin/env python
# encoding: utf-8
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from palettes import get_color_palette
from random import choice, seed
from string import ascii_lowercase
from random import choice, randint, shuffle, seed
from collections import defaultdict


RED = color(255 - 27 * 2.5, 46, 28)
GREEN = color(27 / 2, 27 * 5, 27)
ORANGE = color(255 - 27, 27 * 4.5, 27)
WHITE = color(242)
BLACK = color(27)

def get_state(a, b, c, d):
    """
    Binary number as 0110 (a=0, b=1, c=1, d=10)
    """
    return a * 8 + b * 4 + c * 2 + d * 1

def vline(v1, v2):
    line(v1.x, v1.y, v2.x, v2.y)

class Pattern1(object):
    SEED = sum([choice(range(10)) for i in range(64)])

    def prepare(self, w=0, h=0):
        self.SEED = 335
        randomSeed(self.SEED)
        fill(GREEN)
        noStroke()
        rect(0, 0, w, h)
        noFill()
        self.w, self.h = w, h
        self.cell_size = 100

    @property
    def r(self):
        return self.cell_size / 2

    def list_lines(self, x, y):
        start = PVector(x, y)
        return [
            (PVector(x - self.r, y - self.r), start),
            (PVector(x, y - self.r), start),
            (PVector(x + self.r, y - self.r), start),
            (PVector(x - self.r, y), start),
            (PVector(x + self.r, y), start),
            (PVector(x, y + self.r), start),
            (PVector(x - self.r, y + self.r), start),
            (PVector(x + self.r, y + self.r), start),
        ]

    def center_lines(self, x, y):
        start = PVector(x, y)
        return [
            (PVector(x - self.r / 2, y - self.r / 2), start),
            (PVector(x, y - self.r), start),
            (PVector(x + self.r / 2, y - self.r / 2), start),
            (PVector(x - self.r, y), start),
            (PVector(x + self.r, y), start),
            (PVector(x, y + self.r / 2), start),
        ]

    def draw_loop(self):
        strokeWeight(7)
        stroke(WHITE)

        x_values = range(self.r, self.w, self.cell_size)[1:-1]
        y_values = range(self.cell_size / 2, self.h, self.cell_size)[1:-1]

        for x in x_values:
            for y in y_values:
                lines = self.list_lines(x, y)
                min_line, max_lines = 2, len(lines) + 1

                num_lines = int(random(min_line, max_lines))
                if x == self.w / 2 and y == self.h / 2:
                    num_lines = max_lines - 1
                while num_lines > min_line - 1:
                    i = int(random(num_lines))
                    p1, p2 = lines.pop(i)
                    line(p1.x, p1.y, p2.x, p2.y)
                    num_lines -= 1

        x = self.w / 2
        y = self.h / 2
        strokeWeight(9)
        stroke(BLACK)
        lines = self.center_lines(x, y)
        for p1, p2 in lines:
            line(p1.x, p1.y, p2.x, p2.y)
