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

WIDTH, HEIGHT = 900, 900
COLORS = get_color_palette()

class SplitedCircle(object):

    def __init__(self, x, y, r, num_slices):
        self.pos = PVector(x, y)
        self.r = r * 2
        self.num_slices = num_slices
        self.slice_angle = TWO_PI / num_slices
        self.slice_angles = [i * self.slice_angle for i in range(num_slices + 1)]
        self.current_angle = 0
        self.angle_inc = TWO_PI / (r * 2)
        #self.invert_rotation
        self.speed = PVector(random(-5, 5), random(-3, 3))
        #self._reference = None

        self.colors = []
        prev_color = choice(COLORS)
        for i in range(num_slices + 1):
            c = choice(COLORS)
            while c == prev_color:
                c = choice(COLORS)
            self.colors.append(c)
            prev_color = c

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y


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
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.current_angle)
            for i, angle in enumerate(self.slice_angles):
                start_angle = self.slice_angles[i - 1]
                noStroke()
                fill(self.colors[i])
                arc(0, 0, self.r, self.r, start_angle, angle, PIE)
            self.current_angle += self.angle_inc


particles = []
num_of_particles = 500
def setup():
    size(900, 900)

    for i in range(num_of_particles):
        particles.append(
            SplitedCircle(random(width), random(height), 50, 8)
        )

    background(240)



def draw():
    for particle in particles:
        particle.move()
        particle.display()


def keyPressed():
    global COLORS, particles

    if key == 'n':
        COLORS = get_color_palette()
        particles = []
        for x in range(num_of_particles):
            particles.append(SplitedCircle(random(width), random(height), 50, 7))
            background(240)
        redraw()
    if key == 's':
        saveFrame("########.png")