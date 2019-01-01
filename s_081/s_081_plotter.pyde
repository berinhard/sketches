# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from save_frames import save_video_frames

add_library('svg')


WHITE = color(235, 235, 235)
WHITE_WITH_ALPHA = color(235, 235, 235, 70)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10, 7)
GOLDEN = color(218, 185, 32, 7)
GREEN = color(32, 181, 10, 7)
CYAN = color(20, 255, 255, 7)
PURPLE = color(255, 20, 255, 7)


DISTANCES = [20 * (i + 1) for i in range(15)]
ANGLES = [45, 135, 225, 315]


class SplitableLine(object):

    def __init__(self, start_pos, angle=None, walking_distance=None):
        self.start_pos = start_pos
        self.walking_distance = walking_distance or choice(DISTANCES)
        self.angle = angle or radians(choice(ANGLES))
        self.end_pos = None

    def split(self):
        x = self.start_pos.x + cos(self.angle) * self.walking_distance
        y = self.start_pos.y + sin(self.angle) * self.walking_distance
        self.end_pos = PVector(x, y)

        lerp_index = choice(range(1, 10)) / 10.0
        pos = PVector.lerp(self.start_pos, self.end_pos, lerp_index)

        return SplitableLine(pos, self.angle + HALF_PI)

    def display(self):
        stroke(0)
        line(self.start_pos.x, self.start_pos.y, self.end_pos.x, self.end_pos.y)


splitable_lines = [
    SplitableLine(PVector(200, 200), walking_distance=DISTANCES[-1]),
    SplitableLine(PVector(600, 200), walking_distance=DISTANCES[-1]),
    SplitableLine(PVector(200, 600), walking_distance=DISTANCES[-1]),
    SplitableLine(PVector(600, 600), walking_distance=DISTANCES[-1]),

]


def setup():
    global walker
    size(800, 800)
    #background(BLACK)
    strokeWeight(1)
    #frameRate(24)
    stroke(0)

def draw():
    global splitable_lines

    beginRecord(SVG, 's_081.svg')
    for i in range(1000):
        new_lines = []
        for s_line in splitable_lines:
            new_lines.append(s_line.split())
            s_line.display()

        splitable_lines = new_lines

    print frameCount
    noLoop()
    endRecord()

def keyPressed():
    if key == 's':
        saveFrame("#########.png")