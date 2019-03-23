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
WHITE = color(235, 235, 235, 1)
RED = color(242, 127, 12, 1)
LINE_COLOR = RED

def setup():
    size(900, 900)
    background(BLACK)

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

    def __init__(self, square):
        self.square = square
        self.select_new_vertices()

    def select_new_vertices(self):
        self.vertices = []

        edges = self.square.edges
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
                new_edge = self.square.next_edge(v.edge)
                v.go_to_new_edge(new_edge)

    def display(self):
        stroke(LINE_COLOR)
        strokeWeight(2.5)
        noFill()
        draw_shape(self.vertices, end_shape_mode=CLOSE)

class SquareWithTriangle(object):

    def __init__(self, x, y, size):
        self.pos = PVector(x, y)
        self.size = size
        self.innert_triangle = InnerTriangle(self)
        print(self.edges)

    def next_edge(self, edge):
        index = self.edges.index(edge)
        next_index = (index + 1) % len(self.edges)
        return self.edges[next_index]

    @property
    def edges(self):
        v = self.vertices
        return [(v[i - 1], v[i]) for i in range(4)]


    @property
    def vertices(self):
        w, h = self.size, self.size
        return [
            self.pos,  # v1
            self.pos + PVector(w, 0),  # v2
            self.pos + PVector(w, h),  # v3
            self.pos + PVector(0, h),  # v4
        ]

    def update(self):
        self.innert_triangle.update()

    def display(self):
        self.innert_triangle.display()
        v1, v2, v3, v4 = self.vertices


square = None

def draw():
    global square

    if not square:
        square = SquareWithTriangle(100, 100, 700)

    square.update()
    square.display()

def keyPressed():
    if key == 's':
        saveFrame("########.png")
