# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from collections import namedtuple

WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
BLUE = color(55,189,182)


def pattern():
    w, h = width / 2, height / 2
    p1, p2, p3 = PVector(0, 0), PVector(0, h), PVector(w, h)
    p4 = PVector.lerp(p1, p3, 0.5)
    p5 = PVector.lerp(p1, p2, 0.5)
    p6 = PVector.lerp(p1, PVector(w, 0), 0.5)


    strokeWeight(3)
    fill(BLUE)
    triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
    triangle(p6.x, p6.y, p4.x, p4.y, p3.x, p3.y)

    fill(WHITE)
    triangle(p3.x, p3.y, p4.x, p4.y, p5.x, p5.y)

    fill(BLACK)
    triangle(p6.x, p6.y, p4.x, p4.y, p5.x, p5.y)




def setup():
    background(WHITE)
    stroke(BLACK)
    size(900, 900)


class RotationalQuadrant(object):

    def __init__(self, x, y, rot_angle):
        self.x, self.y = x, y
        self.rot_angle = rot_angle

    def place(self):
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.rot_angle)

    def release(self):
        popMatrix()

    def __enter__(self, *args, **kwargs):
        self.place()

    def __exit__(self, *args, **kwargs):
        self.release()


def draw():
    w, h = width, height

    quadrants = [
        RotationalQuadrant(0, 0, rot_angle=0),
        RotationalQuadrant(w, 0, rot_angle=HALF_PI),
        RotationalQuadrant(0, h, rot_angle=3 * HALF_PI),
        RotationalQuadrant(w, h, rot_angle=PI),
    ]

    for quadrant in quadrants:
        with quadrant:
            pattern()

    strokeWeight(0.5)
    line(0, h / 2, w, h / 2)
    line(w / 2, 0, w / 2, h)

    noLoop()
    saveFrame("cover.png")