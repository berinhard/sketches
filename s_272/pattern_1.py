#!/usr/bin/env python
# encoding: utf-8
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from palettes import get_color_palette
from random import choice

class Pattern1(object):
    """
    Linhas pulsandoda esquerda para a direita sobre um grid

    Valores randômicos:
      - nº de linhas a serem desenhadas
      - largura das linhas horizontais (tamanho do grid)
    """

    def prepare(self):
        self.max_iters = choice(range(3, 15))
        self.line_size = choice(range(10, 51, 10))
        self.x_offset = width / self.line_size
        self.iters = 0
        self.colors = cycle(get_color_palette()[::-1])
        strokeWeight(5)
        background(27)
        self.gen_new_line()

    def gen_new_line(self):
        self.py = None
        self.px = 0
        y_range = range(self.line_size, height, self.line_size)
        self.x_values = range(0, width, self.x_offset)
        self.y_values = [choice(y_range) for i in self.x_values]
        self.y_values[0] = height / 2
        self.y_values[-1] = height / 2
        stroke(self.colors.next())

    @property
    def force_refresh(self):
        return self.iters > self.max_iters

    def draw_loop(self):
        try:
            x, y = self.x_values.pop(0), self.y_values.pop(0)
            if self.py is not None:
                line(self.px, self.py, x, y)
            xf = x + self.x_offset
            line(x, y, xf, y)
            self.py = y
            self.px = xf
        except IndexError:
            self.iters += 1
            if self.force_refresh:
                self.prepare()
            else:
                self.gen_new_line()
