# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json

add_library('svg')


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
    
    seed = int(random(10 ** 6))
    randomSeed(seed)
    import random as py_random
    py_random.seed(seed)
    
    beginRecord(SVG, 's_067_seed_{}.svg'.format(seed))

    noFill()
    ellipse(width/2, height/2, 700, 700)
    e_start, e_end = height / 2 - 350, height / 2 + 350
    y_pos = range(-350, 350, 3)
    with pushMatrix():
        translate(width / 2, height / 2)
        for i, y in enumerate(y_pos):
            y_offset = map(random(1), 0, 1, -10, 10)
            y += y_offset
            x = sqrt(350 ** 2 - y ** 2)
            line(-x, y , x, y)

    strokeWeight(1)
    stroke(BLACK)
    fill(WHITE)
    for i in range(10):
        main_triangle.split()
        
    main_triangle.display()
    
    endRecord()
    
    noLoop()
