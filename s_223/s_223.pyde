# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice

W, H = 300, 700
interval = [50, 250]


class Particle(object):

    def __init__(self):
        self.pos = PVector(0, choice(range(0, H, 5)))

    def move(self):
        min_v, max_v = interval
        if min_v < self.pos.x < max_v:
            self.color = color(240, 240, 240, 30)
            self.pos += PVector(1, random(-2, 2))
        else:
            self.color = color(27, 27, 27, 210)
            self.pos += PVector(1, 0)

    def display(self):
        strokeWeight(4)
        stroke(self.color)
        point(self.pos.x, self.pos.y)


particles = []

def setup():
    size(W, H)
    for i in range(100):
        particles.append(Particle())

    background(240)


def draw():
    if frameCount == 1:
        noStroke()
        fill(27)
        rect(interval[0], 0, interval[1] - interval[0], height)

    for p in particles:
        p.move()
        p.display()

    saveFrame("######.png")