#!/usr/bin/env python
# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice


WIDTH, HEIGHT = 900, 900


class LineWithPoints(object):

    def __init__(self, p1, p2, base_y_offset, p_color=None):
        self.p1, self.p2 = p1, p2
        self.points = []
        self.y_offset = base_y_offset * (width / abs(self.p1.dist(self.p2)))
        self.p_color = p_color or color(245, 245, 245)

    def add_points(self, n=10):
        for i in range(n):
            self.points.append(self.new_point())

    def new_point(self):
        lerp_i = random(1)
        point = PVector.lerp(self.p1, self.p2, lerp_i)

        y_scale = map(abs(lerp_i - 0.5) ** 2, 0, 0.25, 1, 0)  # hiperbole curve
        y_offset = self.y_offset * y_scale

        point.y += random(-y_offset, y_offset)
        return point

    def display(self):
        r, g, b = red(self.p_color), green(self.p_color), blue(self.p_color)

        noStroke()
        for p in self.points:
            dist_from_line = p.dist(PVector(p.x, self.p1.y))
            r = map(dist_from_line, 0, self.y_offset, 3, 12)
            a = map(dist_from_line, 0, self.y_offset, 210, 1)

            fill(r, g, b, a)
            ellipse(p.x, p.y, r, r)


def setup():
    size(WIDTH, HEIGHT)
    background(24)
    x_off = 100
    y = height / 2
    y_offset = 150

    y1, y2, y3 = y, y - y_offset - 75, y + y_offset + 75

    lines = [
        LineWithPoints(PVector(x_off, y2), PVector(width - x_off, y2), y_offset, color(245, 0, 245)),
        LineWithPoints(PVector(x_off, y3), PVector(width - x_off, y3), y_offset, color(245,  245, 0)),
        LineWithPoints(PVector(x_off, y), PVector(width - x_off, y), y_offset),
    ]
    for line in lines:
        line.add_points(int(random(5000, 9000)))
        line.display()

    saveFrame("cover.png")

def draw():
    pass
