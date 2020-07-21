#!/usr/bin/env python
# encoding: utf-8
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from palettes import get_color_palette
from random import choice


class Walker(object):

    def __init__(self, x, y, step_size, max_steps):
        self.x = x
        self.y = y
        self.px = x
        self.py = y
        self.d = step_size
        self.max_steps = max_steps
        self.steps = 0
        self.dead = False

    def move(self):
        if self.steps >= self.max_steps:
            self.dead = True
        if self.dead:
            return

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
        available_pos = [
            (x, y)
            for x, y in available_pos
            if all([0 <= x <= width, x != self.px, 0 <= y <= height, y != self.py])
        ]

        self.px, self.py = self.x, self.y
        if available_pos:
            self.x, self.y = choice(available_pos)
            self.steps += 1
        else:
            self.dead = True


    def draw(self):
        line(self.px, self.py, self.x, self.y)


class Pattern2(object):
    """
    Walkers que se movem nas linhas horizontas/verticais/diagonais do grid partindo do centro da tela

    Valores randômicos:
      - nº de passos no grid
      - tamanho do grid
    """

    def prepare(self):
        strokeWeight(5)
        background(27)
        stroke(242)
        self.cell_size = choice(range(50, 101, 10))
        self.colors = cycle(get_color_palette()[::-1])
        self.new_walker()

    def new_walker(self):
        x, y = self.center
        stroke(self.colors.next())
        self.walker = Walker(x, y, self.cell_size, choice(range(20, 60)))

    @property
    def center(self):
        return width / 2, height / 2

    def draw_loop(self):
        self.walker.move()
        if self.walker.dead:
            self.new_walker()
        else:
            self.walker.draw()
