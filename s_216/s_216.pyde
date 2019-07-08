# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import shuffle
from itertools import cycle

COLORS = get_color_palette()
colors_1 = cycle(COLORS[:3])
colors_2 = cycle(COLORS[3:])
print(COLORS)


class Particle(object):

    def __init__(self, pos, v, c):
        self.pos = pos
        self.direction = PVector.random2D()
        self.color = c
        self.v = v

    def point_to(self, angle):
        v = PVector(self.v.x, self.v.y)
        v.rotate(angle)
        self.direction = v

    def move(self, angle=None):
        self.pos.add(self.direction)

    def display(self):
        stroke(27, 27, 27, 10)
        strokeWeight(2)
        fill(self.color)
        ellipse(self.pos.x, self.pos.y, 5, 5)


class FlowField(object):

    def __init__(self):
        self.map = {}
        self.res = 20

    def get_noise_value(self, pos):
        x = int(pos.x)
        y = int(pos.y)

        #return noise(x, y, frameCount)
        return random(1)

    def affect(self, particle):
        noise_value = self.get_noise_value(particle.pos)
        angle = map(noise_value, 0, 1, HALF_PI, TWO_PI)
        particle.point_to(angle)


flow_field = FlowField()
particles = []
def setup():
    size(900, 900)
    for i in range(400):
        pos = PVector(random(width), height)
        particles.append(Particle(pos, PVector(0, 1), next(colors_1)))

    for i in range(200):
        pos = PVector(random(width), 0)
        particles.append(Particle(pos, PVector(0, -1), next(colors_2)))

    shuffle(particles)
    background(27)


def draw():
    for particle in particles:
        flow_field.affect(particle)
        particle.move()
        particle.display()


def keyPressed():
    if key == 's':
        saveFrame("############.png")