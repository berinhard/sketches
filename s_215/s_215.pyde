# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from berin.save_frames import save_video_frames

GREEN = color(49, 114, 59)
WHITE = color(198)
RED = color(181, 12, 10)
BLACK = color(17, 17, 17)
GOLDEN = color(218, 145, 32)

COLORS = [
    WHITE,
    RED,
    BLACK,
    GOLDEN,
    GREEN,
]


class Particle():

    def __init__(self, x, y):
        self.pos = PVector(x, y)
        v_x, v_y = random(-10, 10), random(-10, 10)
        self.velocity = PVector(v_x, v_y)
        self.velocity.normalize()
        self.angle_inc = random(TWO_PI)
        self.angle = 0
        self.r = 2
        self.c = WHITE

    def move(self):
        self.angle += self.angle_inc
        sin_v = sin(self.angle)
        v_angle = map(sin_v, -1, 1, -QUARTER_PI, QUARTER_PI)
        self.velocity.rotate(v_angle)
        self.pos.add(self.velocity)
        self.velocity.rotate(-v_angle)

    def display(self):
        r, g, b = red(self.c), green(self.c), blue(self.c)
        noStroke()
        fill(color(r, g, b, 10))
        ellipse(self.pos.x, self.pos.y, self.r, self.r)

    @property
    def is_appearing(self):
        conditions = [
            0 < self.pos.x < width,
            0 < self.pos.y < height,
        ]
        return all(conditions)



particles = []


def setup():
    size(900, 900)
    strokeWeight(1)
    stroke(BLACK)
    background(BLACK)

keep_adding = True

def draw():
    global particles

    x = map(noise(frameCount * 0.007), 0, 1, 0, width)
    y = map(noise(frameCount * 0.012), 0, 1, 0, height)

    if keep_adding:
        p = Particle(x, y)
        particles.append(p)

    particles = [p for p in particles if p.is_appearing]

    for p in particles:
        p.move()
        p.display()

    print(frameCount)

def keyPressed():
    global keep_adding

    if key == 's':
        saveFrame("#######.png")
    elif key == 'k':
        keep_adding = not keep_adding
    elif key == 'c':
        background(BLACK)