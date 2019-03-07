# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle
from random import choice


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)


class FabricThread(object):

    def __init__(self, x, y):
        self.pos = PVector(x, y)
        max_range = 90
        if random(1) > 0.5:
            values = [map(i, 0, max_range - 1, 0, PI) for i in range(max_range)]
        else:
            values = [map(i, 0, max_range - 1, TWO_PI, PI) for i in range(max_range)]
        self.angles = cycle(values)

        n = 120
        self.base_angle = choice(range(0, n, 5)) * TWO_PI / n
        colors = [(235, 235, 0), (0, 235, 235), (235, 0, 235)]
        self.c = choice(colors)

    def move(self):
        angle = next(self.angles)
        v = PVector.fromAngle(self.base_angle + angle)
        v.mult(1.4)
        self.pos.add(v)

    def display(self):
        center = PVector(width / 2, height / 2)
        dist = abs(PVector.dist(center, self.pos))
        alpha = map(dist, 0, width / 2 * sqrt(2), 80, 10)
        fill(color(self.c[0], self.c[1], self.c[2], alpha))
        stroke(color(27, 27, 27, alpha))
        ellipse(self.pos.x, self.pos.y, 10, 10)

fabric_thread = []

def setup():
    size(900, 900)
    background(BLACK)
    stroke(BLACK)
    fill(WHITE)


def draw():
    for fabric in fabric_thread:
        fabric.move()
        fabric.display()

    if len(fabric_thread) < 100 and frameCount % 20:
        fabric_thread.append(FabricThread(width / 2, height / 2))

def keyPressed():
    if key == 's':
        saveFrame("###########.png")

    if key == 'n':
        global fabric_thread
        background(BLACK)
        fabric_thread = []
        redraw()
