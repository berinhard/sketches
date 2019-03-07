# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from itertools import cycle


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 123)


class FabricThread(object):

    def __init__(self, x, y):
        self.pos = PVector(x, y)
        values = [map(i, 0, 179, 0, 3 * HALF_PI) for i in range(180)]
        self.angles = cycle(values)
        self.base_angle = random(TWO_PI)

    def move(self):
        angle = next(self.angles)
        v = PVector.fromAngle(self.base_angle + angle)
        v.mult(2)
        self.pos.add(v)

    def display(self):
        ellipse(self.pos.x, self.pos.y, 10, 10)

fabric_thread = []

def setup():
    size(900, 900)
    background(WHITE)
    stroke(BLACK)
    fill(RED)


def draw():
    for fabric in fabric_thread:
        fabric.move()
        fabric.display()

    if len(fabric_thread) < 100 and frameCount % 10:
        fabric_thread.append(FabricThread(width / 2, height / 2))

def keyPressed():
    if key == 's':
        saveFrame("###########.png")