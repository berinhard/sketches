#!/usr/bin/env python
# encoding: utf-8
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from palettes import get_color_palette
from random import choice, randint, shuffle
from collections import defaultdict


def vline(v1, v2):
    line(v1.x, v1.y, v2.x, v2.y)


class Pattern6(object):

    def prepare(self):
        strokeWeight(5)
        strokeCap(RECT)
        background(27)

        self.size = 50
        self.cols  = 2 + width / self.size
        self.rows  = 2 + height / self.size

        self.number_iters = choice(range(2, 8))
        self.iters = 0
        self.fields = []
        self.colors = cycle(get_color_palette()[::-1])
        self.update_field()


    def update_field(self):
        self.fields = [
            [random(1) for y in range(self.rows)]
            for i in range(self.cols)
        ]


    def draw_loop(self):
        stroke(next(self.colors))
        for i in range(self.cols-1):
            for j in range(self.rows-1):
                x = i * self.size
                y = j * self.size

                v = self.get_value(i, j)
                if v == 0:
                    fill(244, 0, 0)
                else:
                    fill(244, 0, 244)

                r = map(self.fields[i][j], 0, 1, 10, 50)
                #ellipse(x, y, r, r)

                off = self.size * 0.5
                a = PVector(x + off, y)
                b = PVector(x + self.size, y + off)
                c = PVector(x + off, y + self.size)
                d = PVector(x, y + off)

                state = self.get_state(
                    self.get_value(i, j),
                    self.get_value(i+1, j),
                    self.get_value(i+1, j+1),
                    self.get_value(i, j+1),
                )

                if state == 1:
                    vline(c, d)
                elif state == 2:
                    vline(b, c)
                elif state == 3:
                  vline(b, d);
                elif state == 4:
                  vline(a, b);
                elif state == 5:
                  vline(a, d);
                  vline(b, c);
                elif state == 6:
                  vline(a, c);
                elif state == 7:
                  vline(a, d);
                elif state == 8:
                  vline(a, d);
                elif state == 9:
                  vline(a, c);
                elif state == 10:
                  vline(a, b);
                  vline(c, d);
                elif state == 11:
                  vline(a, b);
                elif state == 12:
                  vline(b, d);
                elif state == 13:
                  vline(b, c);
                elif state == 14:
                  vline(c, d);

        self.iters += 1
        if self.iters < self.number_iters:
            self.update_field()
        elif not self.iters % 200:
            self.prepare()
        else:
            self.lines = []

    def get_value(self, i, j):
        v = self.fields[i][j]
        return 0 if v < 0.5 else 1

    def get_state(self, a, b, c, d):
        """
        Binary number as 0110 (a=0, b=1, c=1, d=10)
        """
        return a * 8 + b * 4 + c * 2 + d * 1
