# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from collections import namedtuple
import random as py_random
choice = py_random.choice

BLACK = color(27, 27, 27)
PURPLE = color(235, 0, 235, 1)
GOLD = color(235, 235, 0, 1)
CYAN = color(0, 235, 235, 1)
WHITE = color(242, 242, 242, 1)
RED = color(242, 127, 12, 1)

BACK_RED = color(121, 32, 45)
BACK_BLUE = color(35, 32, 121)
BACK_GREEN = color(19, 114, 77)

LINE_COLOR = WHITE
SHAPE_BACKGROUND = BLACK
BACKGROUND = color(242, 242, 242)

def setup():
    size(900, 900)
    background(BACKGROUND)

class TriangleVertex(object):

    class ReachedMaxEdge(Exception):
        pass

    def __init__(self, pos, edge, edge_pos, velocity):
        self.pos = pos
        self.edge = edge
        self.velocity = velocity
        self.edge_pos = edge_pos

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def go_to_new_edge(self, edge):
        self.edge = edge
        self.pos = edge[0]
        self.edge_pos = 0


    def move(self):
        start, end = self.edge
        new_pos = self.edge_pos + self.velocity

        if new_pos >= 1:
            raise self.ReachedMaxEdge()

        self.pos = PVector.lerp(start, end, new_pos)
        self.edge_pos = new_pos


class InnerTriangle(object):

    def __init__(self, edges):
        self.edges = edges
        self.select_new_vertices()

    def select_new_vertices(self):
        self.vertices = []

        edges = self.edges[:]
        py_random.shuffle(edges)
        for i in range(3):
            edge = edges.pop()
            start, end = edge

            lerp_index = random(1)
            pos = PVector.lerp(start, end, lerp_index)

            v = TriangleVertex(pos, edge, lerp_index, random(0.001, 0.01))
            self.vertices.append(v)

    def update(self):
        for v in self.vertices:
            try:
                v.move()
            except TriangleVertex.ReachedMaxEdge:
                index = self.edges.index(v.edge)
                next_index = (index + 1) % len(self.edges)
                new_edge = self.edges[next_index]
                v.go_to_new_edge(new_edge)

    def display(self):
        stroke(LINE_COLOR)
        strokeWeight(2.5)
        noFill()
        draw_shape(self.vertices, end_shape_mode=CLOSE)

class ShapeWithTriangle(object):

    def __init__(self, vertices):
        self.vertices = vertices
        self.inner_triangle = InnerTriangle(self.edges)
        self.print_background = True

    @classmethod
    def random_shape(cls, x, y, radius, n_sides):
        angles = sorted([random(TWO_PI) for i in range(n_sides)])
        vertices = [polar_coordinate(x, y, radius, a) for a in angles]
        return cls(vertices)

    @property
    def edges(self):
        v = self.vertices
        return [(v[i - 1], v[i]) for i in range(len(v))]

    def update(self):
        self.inner_triangle.update()

    def display(self):
        if self.print_background:
            fill(SHAPE_BACKGROUND)
            noStroke()
            draw_shape(self.vertices, end_shape_mode=OPEN)
            self.print_background = False

        self.inner_triangle.display()


square = None

def draw():
    global square

    if not square:
        x, y = width / 2, height / 2
        square = ShapeWithTriangle.random_shape(x, y, 400, 7)

    for i in range(2):
        square.update()
        square.display()

    print(frameCount)

def keyPressed():
    if key == 's':
        saveFrame("########.png")
    elif key == 'n':
        global square
        square = None
        background(BLACK)
        redraw()