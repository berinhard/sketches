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
        v_x, v_y = random(-3, 3), random(-3, 3)
        self.velocity = PVector(v_x, v_y)
        self.r = map(noise(frameCount * 0.032), 0, 1, 0, 150)
        self.c = choice(COLORS)

    def move(self):
        self.pos.add(self.velocity)
        self.r -= 1

    def display(self):
        r, g, b = red(self.c), green(self.c), blue(self.c)
        stroke(27, 27, 27, 100)
        fill(color(r, g, b, 200))
        ellipse(self.pos.x, self.pos.y, self.r, self.r)

    @property
    def is_appearing(self):
        conditions = [
            0 - self.r < self.pos.x < width + self.r,
            0 - self.r < self.pos.y < height + self.r,
            self.r > 0,
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

    #save_video_frames(40, 60)
    print(frameCount)

def keyPressed():
    global keep_adding

    if key == 's':
        saveFrame("#######.png")
    elif key == 'k':
        keep_adding = not keep_adding
    elif key == 'c':
        background(BLACK)