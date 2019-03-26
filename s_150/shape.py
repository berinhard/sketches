from berin.coords import polar_coordinate
import random as py_random
from berin.shapes import draw_shape
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

class FillingShapeVertex(object):

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


class ShapeInnerFilling(object):

    def __init__(self, edges, n_vertices=3, line_color=None):
        self.edges = edges
        self.n_vertices = n_vertices
        self.select_new_vertices()
        self.line_color = line_color or LINE_COLOR

    def select_new_vertices(self):
        self.vertices = []

        edges = self.edges[:]
        py_random.shuffle(edges)
        for i in range(self.n_vertices):
            edge = edges.pop()
            start, end = edge

            lerp_index = random(1)
            pos = PVector.lerp(start, end, lerp_index)

            v = FillingShapeVertex(pos, edge, lerp_index, random(0.001, 0.01))
            self.vertices.append(v)

    def update(self):
        for v in self.vertices:
            try:
                v.move()
            except FillingShapeVertex.ReachedMaxEdge:
                index = self.edges.index(v.edge)
                next_index = (index + 1) % len(self.edges)
                new_edge = self.edges[next_index]
                v.go_to_new_edge(new_edge)

    def display(self):
        stroke(self.line_color)
        strokeWeight(2.5)
        noFill()
        draw_shape(self.vertices, end_shape_mode=CLOSE)

class ShapeWithInnerFilling(object):

    def __init__(self, vertices, print_background=True, line_color=None):
        self.vertices = vertices
        self.filling = ShapeInnerFilling(self.edges, line_color=line_color)
        self.print_background = print_background

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
        self.filling.update()

    def display(self):
        if self.print_background:
            fill(SHAPE_BACKGROUND)
            noStroke()
            draw_shape(self.vertices, end_shape_mode=OPEN)
            self.print_background = False

        self.filling.display()