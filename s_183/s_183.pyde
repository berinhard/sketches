# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

COLORS = get_color_palette()
WIDTH, HEIGHT = 900, 900


from random import choice
class Particle(object):

    def __init__(self):
        self.pos = PVector(random(WIDTH), random(HEIGHT))
        self.speed = PVector(random(-5, 5), random(-3, 3))
        self.r = random(50, 100)
        self._reference = None
        self.c = choice(COLORS)

    @property
    def reference(self):
        if not self._reference:
            self._reference = choice(particles)
        return self._reference

    def move(self):
        acc = PVector.random2D()
        acc.mult(2)
        self.speed.add(acc)
        self.speed.limit(8)
        self.pos.add(self.speed)
        self.r -= 1

    def display(self):
        if self.r > 0:
            stroke(27, 27, 27, 25)
            fill(self.c)
            ellipse(self.pos.x, self.pos.y, self.r, self.r)


num_of_partciles = 500
particles = []

def setup():
    size(900, 900)
    for x in range(num_of_partciles):
        particles.append(Particle())


def draw():
    for particle in particles:
        particle.move()
        particle.display()


def keyPressed():
    global COLORS, particles

    if key == 'n':
        COLORS = get_color_palette()
        for x in range(num_of_partciles):
            particles.append(Particle())
        redraw()
    if key == 's':
        saveFrame("########.png")