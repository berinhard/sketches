# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235, 130)
BLACK = color(27, 27, 27)


COLORS = None
def get_color_palette():
    global COLORS

    if not COLORS:
        with open("data/1000.json") as fd:
            colors = json.load(fd)
            COLORS = choice(colors)

    return COLORS

MIN_RADIUS = 1
MAX_RADIUS = 100

class Bokeh(object):

    def __init__(self):
        self.radius = MIN_RADIUS
        self.x = choice(range(width))
        self.y = choice(range(height))
        self.velocity = PVector(2.5, 2.5)
        self.color = choice(get_color_palette())
        self.skip_step = random(0, 0.6)
        self.positions = [(self.x, self.y, self.radius, random(1))]
        self.max_radius = choice(range(100, 150))

    @property
    def reached_max(self):
        return self.radius > self.max_radius

    @property
    def dead(self):
        return not self.positions

    def move(self, ref_point):
        direction = PVector(self.x, self.y)
        direction.sub(ref_point)
        direction.normalize()
        diff = height / direction.dist(PVector(self.x, self.y))
        direction.mult(1.1 * diff)
        self.x += self.velocity.x * direction.x
        self.y += self.velocity.y * direction.y

    def update(self, ref_point):
        self.move(ref_point)
        self.radius += 1
        if not self.reached_max:
            prob = random(1)
            if prob <= self.skip_step:
                self.positions.append((self.x, self.y, self.radius, random(1)))
        elif self.positions:
            self.positions.pop(0)

    def display(self):
        for x, y, radius, prob in self.positions:
            if prob > self.skip_step:
                continue
            elif x > width + 30:
                continue
            elif y > height + 30:
                continue
            r  = red(self.color)
            g = green(self.color)
            b = blue(self.color)
            a = map(radius, MIN_RADIUS, self.max_radius, 20, 100)
            stroke(color(r, g, b, a))

            with pushMatrix():
                translate(x, y)
                rotate(radians(radius))
                rect(0, 0, radius, radius)
                rotate(radians(45))
                rect(0, 0, radius / sqrt(2), radius / sqrt(2))
                if radius > 80:
                    radius = radius / sqrt(2)
                    rotate(radians(45))
                    rect(0, 0, radius / sqrt(2), radius / sqrt(2))


bokeh_list = []

def setup():
    global px, py

    size(1000, 1000)
    background(BLACK)
    colorMode(RGB, 100)
    frameRate(24)
    noCursor()
    noFill()
    strokeWeight(2)
    rectMode(CENTER)

    px = random(1) * width
    py = random(1) * height

def draw():
    global bokeh_list, px, py, COLORS
    background(BLACK)

    ref_point = PVector(px, py)

    if len(bokeh_list) < 100:
        bokeh_list.append(Bokeh())

    for bokeh in bokeh_list:
        bokeh.display()
        bokeh.update(ref_point)

    bokeh_list = [b for b in bokeh_list if not b.dead]

    if random(1) > 0.996:
        COLORS = None
        global px, py
        px = random(1) * width
        py = random(1) * height

    #save_video_frames(24, 60 * 10)


def keyPressed():
    global COLORS, bokeh_list
    if key == 'n':
        background(BLACK)
        COLORS = None
        global px, py
        px = random(1) * width
        py = random(1) * height
        bokeh_list = []
    elif key == 's':
        saveFrame("##########.png")