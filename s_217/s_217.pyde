# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice


class SquareWithLines(object):

    def __init__(self, x, y, size):
        self.pos = PVector(x, y)
        self.size = size
        self.num_lines = int(random(10))
        self.lerp_intervals = [0.2, 0.4, 0.6, 0.8]
        self.lines_positions = []

    @property
    def vertices(self):
        """
        Vertices visual positions:

        v1 --- v2
         |      |
         |      |
        v4 --- v3
        """
        w, h = self.size, self.size
        return [
            self.pos + PVector(0, 0),  # v1
            self.pos + PVector(w, 0),  # v2
            self.pos + PVector(w, h),  # v3
            self.pos + PVector(0, h),  # v4
        ]

    @property
    def edges(self):
        """
        Returns a list of tuples representing (edge_start, edge_end)
        """
        v = self.vertices
        return [(v[i - 1], v[i]) for i in range(4)]

    def populate_lines(self):
        for i in range(self.num_lines):
            e1 = choice(self.edges)
            e2 = choice(self.edges)
            while e1 == e2:
                e2 = choice(self.edges)

            v1, v2 = e1
            v3, v4 = e2
            p1 = PVector.lerp(v1, v2, choice(self.lerp_intervals))
            p2 = PVector.lerp(v3, v4, choice(self.lerp_intervals))

            self.lines_positions.append((p1, p2))


    def display(self):
        noStroke()
        if not self.lines_positions:
            fill(202, 21, 32)
            rect(self.pos.x, self.pos.y, self.size, self.size)
        else:
            fill(27)
            rect(self.pos.x, self.pos.y, self.size, self.size)

        for i, points in enumerate(self.lines_positions):
            p1, p2 = points
            stroke(240)
            w = 1
            if len(self.lines_positions) > 1:
                w = map(i, 0, len(self.lines_positions) - 1, 4, 1)
            strokeWeight(w)
            line(p1.x, p1.y, p2.x, p2.y)


square_size = 60
def init():
    global squares

    squares = []
    for x in range(0, width, square_size):
        for y in range(0, height, square_size):
            square = SquareWithLines(x+2, y+2, square_size-4)
            square.populate_lines()
            squares.append(square)


def setup():
    size(900, 900)
    init()


def draw():
    background(242)
    for square in squares:
        square.display()

    #saveFrame("cover.png")