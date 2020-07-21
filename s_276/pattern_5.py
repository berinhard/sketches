#!/usr/bin/env python
# encoding: utf-8
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from palettes import get_color_palette
from random import choice, randint, shuffle
from collections import defaultdict


class Block(object):

    def __init__(self, x, y, d, c):
        self.x, self.y = x, y
        self.d = d
        self.c = c
        self.n = choice(range(1, 5))

        available_pos = [
            (self.x - self.d, self.y - self.d),     # top left
            (self.x, self.y - self.d),              # top
            (self.x + self.d, self.y - self.d),     # top rigth
            (self.x - self.d, self.y),              # left
            (self.x + self.d, self.y),              # right
            (self.x - self.d, self.y + self.d),     # bottom left
            (self.x, self.y + self.d),              # bottom
            (self.x + self.d, self.y + self.d),     # bottom right
        ]
        shuffle(available_pos)
        self.positions = [available_pos.pop() for x in range(self.n)]

    def draw(self):
        noFill()
        stroke(self.c)
        for x, y in self.positions:
            line(self.x, self.y, x, y)



class Pattern5(object):

    def prepare(self):
        self.blocks = []
        self.cell_size = choice(range(50, 151, 10)) / 2
        self.x_values = range(0, width + self.cell_size, self.cell_size)
        self.y_range = defaultdict(int)
        self.colors = cycle(get_color_palette())

        strokeWeight(5)
        strokeCap(RECT)
        background(27)

    def draw_loop(self):
        x = choice(self.x_values)
        y = self.y_range[x]
        self.blocks.append(Block(x, y, self.cell_size, self.colors.next()))
        self.y_range[x] += self.cell_size

        for b in self.blocks:
            b.draw()

        if min(self.y_range.values()) > height:
            self.prepare()
