#!/usr/bin/env python
# encoding: utf-8
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from palettes import get_color_palette
from random import choice, shuffle


class Pattern3(object):

    def prepare(self):
        strokeWeight(5)
        strokeCap(RECT)
        stroke(242)
        background(27)
        self.colors = cycle(get_color_palette()[::-1])

    def draw_loop(self):
        d = choice(range(50, 351, 50))

        x_value = range(0, width, d)
        y_value = range(0, height, d)

        x, y = choice(x_value), choice(y_value)

        if random(1) > 0.5:
            px = x + d
            py = y + d
        else:
            px = x + d
            py = y - d

        stroke(self.colors.next())
        line(px, py, x, y)
