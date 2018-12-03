# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)


class Triangle(object):

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.internal_triangles = []

    def display(self):
        triangle(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            self.p3.x, self.p3.y,
        )

        for internal in self.internal_triangles:
            internal.display()

    def split(self):
        if not self.internal_triangles:
            vertexes_length = sorted([
                (PVector.dist(self.p1, self.p2), self.p1, self.p2, self.p3),
                (PVector.dist(self.p1, self.p3), self.p1, self.p3, self.p2),
                (PVector.dist(self.p2, self.p3), self.p2, self.p3, self.p1),
            ], key=lambda x: x[0])

            distance, p1, p2, p3 = choice(vertexes_length)#[0]
            split = choice([0.3, 0.4, 0.5, 0.6, 0.7])
            half = PVector.lerp(p1, p2, split)

            self.internal_triangles.append(Triangle(p1, p3, half))
            self.internal_triangles.append(Triangle(p2, p3, half))
        else:
            for internal in self.internal_triangles:
                internal.split()


def setup():
    global main_triangle
    size(900, 900)
    main_triangle = Triangle(
        PVector(800, 700),
        PVector(100, 700),
        PVector(450, 20),
    )
    frameRate(1)

def draw():
    global main_triangle
    background(WHITE)

    noStroke()
    fill(RED)
    ellipse(width/2, height/2, 700, 700)

    strokeWeight(2)
    stroke(BLACK)
    fill(WHITE)
    main_triangle.display()
    main_triangle.split()

    print(frameCount)

    if frameCount < 16:
        saveFrame("#####.png")
    else:
        noLoop()