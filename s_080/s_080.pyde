# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from save_frames import save_video_frames


WHITE = color(235, 235, 235)
WHITE_WITH_ALPHA = color(235, 235, 235, 20)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10, 7)
GOLDEN = color(218, 185, 32, 7)
GREEN = color(32, 181, 10, 7)
CYAN = color(20, 255, 255, 7)
PURPLE = color(255, 20, 255, 7)


ANGLES = [45, 135, 225, 315]
DISTANCES = [10 * (i + 1) for i in range(10)]


class StableWalker(object):

    def __init__(self, pos):
        self.pos = pos
        self.start_pos = None
        self.end_pos = None
        self.walking_distance = 0
        self.angle = None

    def move(self):
        self.start_pos = self.pos

        self.angle = radians(choice([a for a in ANGLES if not radians(a) == self.angle]))
        self.walking_distance = choice(DISTANCES)
        x = self.pos.x + cos(self.angle) * self.walking_distance
        y = self.pos.y + sin(self.angle) * self.walking_distance

        if x > width:
            x = width
        elif x < 0:
            x = 0
        if y > height:
            y = height
        elif y < 0:
            y = 0

        self.next_pos = PVector(x, y)
        self.pos = self.next_pos

    def display(self):
        stroke(BLACK)
        line(self.start_pos.x, self.start_pos.y, self.next_pos.x, self.next_pos.y)

def setup():
    global walker
    size(800, 800)
    background(WHITE_WITH_ALPHA)
    strokeWeight(2)
    stroke(BLACK)
    frameRate(24)
    start = PVector(random(200, 600), random(200, 600))
    walker = StableWalker(start)

def draw():
    global walker

    noStroke()
    fill(WHITE_WITH_ALPHA)
    rect(0, 0, width, height)
    walker.move()
    walker.display()
    #save_video_frames(24, 60 * 5)

    if not frameCount % 2000:
        start = PVector(random(200, 600), random(200, 600))
        walker = StableWalker(start)
        background(WHITE)
