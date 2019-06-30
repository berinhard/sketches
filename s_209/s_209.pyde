# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings


class Particle(object):

    def __init__(self):
        self.pos = PVector(random(width), height)
        self.direction = PVector.random2D()

    def point_to(self, angle):
        v = PVector(0, 1)
        v.rotate(angle)
        self.direction = v

    def move(self, angle=None):
        self.pos.add(self.direction)

    def display(self):
        fill(210, 14, 39, 5)
        noStroke()
        ellipse(self.pos.x, self.pos.y, 5, 5)


class FlowField(object):

    def __init__(self):
        self.map = {}
        self.res = 20

    def get_noise_value(self, pos):
        x = int(pos.x / self.res) * self.res
        y = int(pos.y / self.res) * self.res

        return noise(x, y, frameCount * 0.001)

    def display(self):
        res = self.res

        x_range = range(0, width, self.res)
        y_range = range(0, height, self.res)

        for x in x_range:
            for y in y_range:
                pos = PVector(x, y)
                with pushMatrix():
                    translate(pos.x, pos.y)

                    noise_value = self.get_noise_value(pos)
                    angle = map(noise_value, 0, 1, 0, TWO_PI)

                    rotate(angle)
                    stroke(27)
                    line(0, 0, res/2, res/2)
                    fill(255, 0, 0)
                    ellipse(res / 2, res / 2,  2, 2)

    def affect(self, particle):
        noise_value = self.get_noise_value(particle.pos)
        angle = map(noise_value, 0, 1, 0, TWO_PI)
        particle.point_to(angle)


flow_field = FlowField()
particles = []
def setup():
    size(900, 900)
    for i in range(400):
        particles.append(Particle())
    background(240)


def draw():
    for particle in particles:
        flow_field.affect(particle)
        particle.move()
        particle.display()

    print(frameRate)


def keyPressed():
    if key == 's':
        saveFrame("############.png")