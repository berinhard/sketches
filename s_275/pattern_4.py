#!/usr/bin/env python
# encoding: utf-8
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from palettes import get_color_palette
from random import choice, randint


class Walker(object):

    def __init__(self, x, y, step_size, c_list, n):
        self.p = PVector(x, y)
        self.step_size = step_size
        self.c = [c_list.next() for i in range(n)]
        self.dist = 0
        self.dist_off = choice(range(1, 4))

        d_args = [
            (step_size, step_size),
            (step_size, 0),
            (step_size, -step_size),
            (-step_size, step_size),
            (-step_size, 0),
            (-step_size, -step_size),
            (0, step_size),
            (0, -step_size),
        ]
        self.dests = [
            PVector(*d_args[randint(0, 9999) % len(d_args)])
            for i in range(n)
        ]

        v_args = [
            (2, 0),
            (-2, 0),
            (0, -2),
            (0, 2),
        ]
        self.dir = PVector(*v_args[randint(0, 9999) % len(v_args)])
        self.fixed = False

    def move(self):
        self.dist += 2
        self.fixed = False

        self.p += self.dir

        if not self.dist % (self.step_size * self.dist_off):
            self.fixed = True
            self.dist = 0

    def draw(self):
        for c, d in zip(self.c, self.dests):
            stroke(c)
            s = self.p + d
            line(s.x, s.y, self.p.x, self.p.y)

    @property
    def dead(self):
        min_w, max_w = (0 - self.step_size, width + self.step_size)
        min_h, max_h = (0 - self.step_size, height + self.step_size)

        return not all([
            min_w < self.p.x < max_w,
            min_h < self.p.y < max_h,
        ])


class Pattern4(object):

    def prepare(self):
        self.walkers = []
        self.fixed = []
        strokeWeight(5)
        stroke(242)
        strokeCap(ROUND)
        self.cell_size = choice(range(50, 101, 10))
        self.colors = cycle(get_color_palette()[::-1])

    def new_walker(self, x, y, n):
        self.walkers.append(Walker(x, y, self.cell_size, self.colors, n=n))

    def draw_loop(self):
        background(27)

        self.x_values = range(0, width + self.cell_size, self.cell_size)
        self.y_values = range(0, height + self.cell_size, self.cell_size)

        for w in self.fixed:
            w.draw()

        fixed = []
        for w in self.walkers:
            w.move()
            w.draw()
            if w.fixed:
                fixed.append(w)

        if not frameCount % 10:
            x, y = choice(self.x_values), choice(self.y_values)
            self.new_walker(x, y, n=choice(range(1, 8)))

        for w in fixed:
            self.walkers.remove(w)
        self.fixed.extend(fixed)

        self.walkers = [w for w in self.walkers if not (w.dead or w.fixed)]

        if len(self.fixed) > 120:
            self.prepare()
