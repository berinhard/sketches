# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from berin.save_frames import save_video_frames

GREEN = color(49, 255, 59)
WHITE = color(198)
RED = color(181, 12, 10)
BLACK = color(17, 17, 17)
BLUE = color(10, 38, 240)
GOLDEN = color(255, 130, 0)

COLORS = [
    WHITE,
    RED,
    BLACK,
    GOLDEN,
    GREEN,
]


amplitude = 28


class Particle():

    def __init__(self, y):
        self.theta_inc = random(0.01, 0.1)
        self.x, self.y = 0, y
        self.theta = random(TWO_PI)
        self.pos = PVector(0, sin(self.theta) * amplitude + y)
        #self.r = map(noise(frameCount * 0.032), 0, 1, 0, 150)
        self.c = BLUE

    def move(self):
        self.theta += self.theta_inc
        self.x += 1
        self.pos = PVector(self.x, sin(self.theta) * amplitude + self.y)


    def display(self):
        r, g, b = red(self.c), green(self.c), blue(self.c)
        #stroke(27, 27, 27, 100)
        noStroke()
        fill(color(r, g, b, 5))
        ellipse(self.pos.x, self.pos.y, 5, 5)

    @property
    def is_appearing(self):
        return self.x <= width



particles = []


def setup():
    size(900, 900)
    strokeWeight(1)
    stroke(BLACK)
    background(BLACK)

keep_adding = True

def draw():
    global particles

    values = range(0, width + 1, 30)
    y = choice(values)

    if keep_adding:
        p = Particle(y)
        particles.append(p)

    particles = [p for p in particles if p.is_appearing]

    for p in particles:
        p.move()
        p.display()

    print(frameCount, len(particles))

def keyPressed():
    global keep_adding

    if key == 's':
        saveFrame("#######.png")
    elif key == 'k':
        keep_adding = not keep_adding
    elif key == 'c':
        background(BLACK)