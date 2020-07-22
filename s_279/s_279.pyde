#!/usr/bin/env python
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import choice


class ScratchLine(object):

    def __init__(self, p1, p2, w, noise_scale=0):
        self.w = w + random(-0.5 * noise_scale, 0.5 * noise_scale)
        r = self.w * noise_scale;
        self.p1 = p1
        self.p2 = p2
        self.p1 = PVector(p1.x + random(-r,r), p1.y + random(-r,r))
        self.p2 = PVector(p2.x + random(-r,r), p2.y + random(-r,r))

    def display(self):
        strokeWeight(self.w)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


def setup():
    size(900, 900)
    background(242)
    stroke(27)


def draw():
    if frameCount > 75:
        return

    off = width / 8
    x, y = off, off
    s = 6 * width / 8
    points = [
        PVector(x, y),
        PVector(x + s, y),
        PVector(x + s, y + s),
        PVector(x, y + s),
    ]

    i = choice(range(len(points)))
    j = i - 2
    p1, p2 = points[i], points[i - 1]
    while j == i:
        j = choice(range(len(points)))
    p3, p4 = points[j], points[j - 1]

    rand_1 = random(1)
    p1 = PVector.lerp(p1, p2, rand_1)
    p2 = PVector.lerp(p4, p3, rand_1)

    new_line = ScratchLine(p1, p2, 10, 5)
    new_line.display()

def keyPressed():
    if key == 's':
        saveFrame("#########.png")
