# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice

RED = color(212, 23, 49)

class LineWalker():

    def __init__(self, start):
        self.start = start
        self.end = start
        self.move_forward = True
        self.color = color(27)
        self.weight = 3
        if random(1) > 0.92:
            self.color = color(212, 23, 49)
            self.weight = 6
        self.current_angle = 0

    @property
    def is_out_of_canvas(self):
        return self.start.x >= width

    def move(self):
        if self.is_out_of_canvas:
            return

        self.start = self.end
        size = choice(range(20, 216, 10))
        if self.move_forward:
            self.end = self.end + PVector(size, 0)
        else:
            angles = [i * TWO_PI / 8  for i in range(8)]
            coord = polar_coordinate(0, 0, size, choice(angles))
            self.end = self.end + PVector(coord.x, coord.y)

        self.move_forward = not(self.move_forward)

    def draw(self, draw_line=False):
        strokeWeight(self.weight)
        stroke(self.color)
        line(self.start.x, self.start.y, self.end.x, self.end.y)

walkers = []
def init_sketch(background_color=None):
    global walkers
    global PALETTE

    PALETTE = get_color_palette()
    walkers = []
    for y in range(0, height, 40):
        walkers.append(LineWalker(PVector(0, y)))

    if background_color:
        background(242)

def setup():
    size(900, 900)
    frameRate(5)
    init_sketch(27)


def draw():
    if all([w.is_out_of_canvas for w in walkers]):
        return

    print(frameCount)
    for walker in walkers:
        walker.move()

    for walker in [w for w in walkers if w.color == color(27)]:
        walker.draw()

    for walker in [w for w in walkers if w.color == RED]:
        walker.draw()

def keyPressed():
    if key == 'n':
        init_sketch(27)
    if key == 's':
        saveFrame("#####.png")
