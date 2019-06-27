# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.palettes import get_color_palette
from random import choice


max_particles = 1000
particle_size = 10
particles = []
structures = []
max_dist_from_center = 600 * sqrt(2) / 2
min_dist = 7 * particle_size / 10
colors = get_color_palette()
# colors = [
#     color(255, 255, 0),
#     color(255, 0, 255),
#     color(0, 255, 255),
# ]


class Particle(object):

    def __init__(self):
        self.pos = PVector(width / 2, height / 2)
        self.direction = PVector.random2D()
        self.direction.mult(3)
        self._stick = False
        self.color = None

    def walk(self):
        self.pos.add(self.direction)

    def dist(self, other):
        return self.pos.dist(other.pos)

    def stick_to(self, other=None):
        if not other:
            self.color = choice(colors)
        else:
            self.color = other.color
        self._stick = True

    def from_center(self):
        return self.pos.dist(PVector(width / 2, height / 2))

    def stick(self):
        if not self._stick:
            x, y = int(self.pos.x), int(self.pos.y)

            border_conditions = [
                x <= 0,
                x >= width,
                y <= 0,
                y >= height
            ]
            if any(border_conditions):
                self.stick_to()
            else:
                for structure in structures:
                    if self.dist(structure) <= min_dist:
                        self.stick_to(structure)
                        break

        return self._stick

def setup():
    size(600, 600)
    noStroke()


def draw():
    background(27)

    if not structures:
        for i, c in enumerate(colors):
            r = 30
            fill(c)
            rect(i * r, 0, r, r)

    for i in range(100):
        if len(particles) <= max_particles:
            particle = Particle()
            particles.append(particle)

        to_remove = []
        for particle in particles:
            if not particle.stick():
                particle.walk()
            else:
                structures.append(particle)
                to_remove.append(particle)

        for particle in to_remove:
            particles.remove(particle)

    for particle in structures:
        size = map(particle.from_center(), 0, max_dist_from_center, 2, 20)
        fill(particle.color)
        ellipse(particle.pos.x, particle.pos.y, size, size)

def keyPressed():
    if key == 's':
        noLoop()
    elif key == 'c':
        redraw()
    elif key == 'f':
        saveFrame("############.png")