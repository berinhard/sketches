# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice

WIDTH, HEIGHT = 1920, 1080
BLACK = color(27, 27, 27)
PURPLE = color(235, 0, 235, 1)
GOLD = color(235, 235, 0, 1)
CYAN = color(0, 235, 235, 1)
WHITE = color(242, 242, 242, 1)
RED = color(182, 127, 12, 1)

BACK_RED = color(121, 32, 45)
BACK_BLUE = color(35, 32, 121)
BACK_GREEN = color(19, 114, 77)

class LineWalker():

    def __init__(self, start):
        self.start = start
        self.end = start
        self.move_forward = True
        self.color = choice(PALETTE)
        self.weight = random(4, 32)

    @property
    def is_out_of_canvas(self):
        return self.start.x >= width

    def move(self):
        if self.is_out_of_canvas:
            return

        self.start = self.end
        size = choice(range(5, 216, 10))
        if self.move_forward:
            self.end = self.end + PVector(size, 0)
        else:
            direction = -1 if random(1) > 0.5 else 1
            self.end = self.end + PVector(0, size * direction)

        self.move_forward = not(self.move_forward)

    def draw(self, draw_line=False):
        if not draw_line:
            stroke(self.color)
            strokeWeight(self.weight)
            line(self.start.x, self.start.y, self.end.x, self.end.y)
        else:
            stroke(27, 27, 27, 50)
            strokeWeight(map(self.weight, 4, 32, 0, 4))
            line(self.start.x, self.start.y, self.end.x, self.end.y)

walkers = []
def init_sketch(background_color=None):
    global walkers
    global PALETTE

    PALETTE = get_color_palette()
    walkers = []
    for y in range(0, HEIGHT, 40):
        walkers.append(LineWalker(PVector(0, y)))

    if background_color:
        background(background_color)

def setup():
    size(WIDTH, HEIGHT)
    frameRate(5)
    init_sketch(27)


def draw():
    if all([w.is_out_of_canvas for w in walkers]):
        return

    print(frameCount)
    for walker in walkers:
        walker.move()
        walker.draw()
        walker.draw(True)

def keyPressed():
    if key == 'n':
        init_sketch(27)
    if key == 's':
        saveFrame("#####.png")