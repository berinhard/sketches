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

MIN_RADIUS = 50
MAX_RADIUS = 200

class Bokeh(object):

    def __init__(self, radius=50):
        self.radius = 50
        self.x = choice(range(width))
        self.y = choice(range(height))
        self.velocity = PVector(1, 1)
        self.color = choice(get_color_palette())

    @property
    def dead(self):
        return self.radius > MAX_RADIUS

    def move(self, ref_point):
        direction = PVector(self.x, self.y)
        direction.sub(ref_point)
        direction.normalize()
        diff = height / direction.dist(PVector(self.x, self.y))
        direction.mult(2 * diff)
        self.x += self.velocity.x * direction.x
        self.y += self.velocity.y * direction.y

    def update(self, ref_point):
        self.move(ref_point)
        self.radius += 1

    def display(self):
        r = red(self.color)
        g = green(self.color)
        b = blue(self.color)
        a = map(self.radius, MIN_RADIUS, MAX_RADIUS, 100, 0)

        fill(color(r, g, b, a))
        ellipse(self.x, self.y, self.radius, self.radius)

bokeh_list = []

def setup():
    global px, py

    fullScreen()
    noStroke()
    background(BLACK)
    colorMode(RGB, 100)
    frameRate(24)
    noCursor()

    px = random(1) * width
    py = random(1) * height

def draw():
    background(BLACK)
    global bokeh_list, px, py, COLORS

    ref_point = PVector(px, py)

    bokeh_list.append(Bokeh())
    bokeh_list.append(Bokeh())
    bokeh_list = sorted(
        [b for b in bokeh_list if not b.dead],
        key=lambda b: b.radius,
    )
    for bokeh in bokeh_list:
        bokeh.display()
        bokeh.update(ref_point)

    print(len(bokeh_list))

    save_video_frames(24, 60 * 10)

    if random(1) > 0.995:
        COLORS = None
        global px, py
        px = random(1) * width
        py = random(1) * height



def keyPressed():
    global COLORS
    if key == 'n':
        COLORS = None
        global px, py
        px = random(1) * width
        py = random(1) * height