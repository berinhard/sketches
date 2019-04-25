# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice
from itertools import combinations

COLORS = [color(255, 255, 0), color(0, 255, 255), color(255, 0, 255)]

class Particle(object):

    def __init__(self):
        x = random(width)
        y = random(height)
        speed_range = [-10, 10]
        self.pos = PVector(x, y)
        self.velocity = PVector(random(*speed_range), random(*speed_range))
        self.color = choice(COLORS)

    def move(self):
        self.pos.add(self.velocity)
        if self.is_vertical_bound:
            self.velocity.x *= -1

        if self.is_horizontal_bound:
            self.velocity.y *= -1

    @property
    def is_vertical_bound(self):
        return self.pos.x <= 0 or self.pos.x >= width

    @property
    def is_horizontal_bound(self):
        return self.pos.y <= 0 or self.pos.y >= height


    def display(self):
        noStroke()
        fill(self.color)
        #ellipse(self.pos.x, self.pos.y, 25, 25)

    def link(self, particle):
        distance = self.pos.dist(particle.pos)

        max_dist = PVector(0, 0).dist(PVector(width, height))
        alpha_v = map(distance, 0, max_dist, 200 , 0)
        stroke_w = map(distance, 0, max_dist, 6, 2)
        stroke_map = map(distance, 0, max_dist, 0, 1)
        stroke_color = lerpColor(self.color, particle.color, stroke_map)
        r, g, b = red(stroke_color), green(stroke_color), blue(stroke_color)
        stroke(r, g, b, alpha_v)
        strokeWeight(stroke_w)

        line(self.pos.x, self.pos.y, particle.pos.x, particle.pos.y)

    @property
    def is_not_appearing(self):
        off_border_conditions = [
            self.pos.x < 0,
            self.pos.x > width,
            self.pos.y < 0,
            self.pos.y > height,
        ]
        return any(off_border_conditions)

    @property
    def is_appearing(self):
        return not self.is_not_appearing


particles = []
max_num_of_particles = 10

def setup():
    global combined_particles

    size(900, 900)
    for i in range(max_num_of_particles):
        new_particle = Particle()
        particles.append(new_particle)

    combined_particles = list(combinations(particles, 2))
    frameRate(24)
    background(27)


def draw():
    global particles, combined_particles
    noStroke()
    fill(color(27, 27, 27, 10))
    rect(0, 0, width, height)

    for particle in particles:
        particle.move()
        particle.display()

    for particle_1, particle_2 in combined_particles:
        particle_1.link(particle_2)