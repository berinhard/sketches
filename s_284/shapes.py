import py5
import random

COLORS = [
    (232, 232, 53),
    (80, 27, 27),
]

COLORS = [
    (251, 34, 149),
    (90, 194, 35)
]


class TriSquare:

    def __init__(self, v1, v2, v3, v4):
        self.v1, self.v2, self.v3, self.v4 = v1, v2, v3, v4
        colors = COLORS[:]
        random.shuffle(colors)
        self.c1, self.c2 = colors

    def draw(self):
        py5.stroke_weight(1)
        py5.stroke(27, 27, 27, 100)
        random_point = (
            py5.random(self.v1.x, self.v2.x),
            py5.random(self.v1.y, self.v4.y)
        )

        py5.fill(*self.c1)
        s = py5.create_shape()
        s.begin_shape()
        s.curve_vertex(self.v1.x, self.v1.y)
        s.curve_vertex(self.v1.x, self.v1.y)
        s.curve_vertex(*random_point)
        s.curve_vertex(self.v3.x, self.v3.y)
        s.curve_vertex(*random_point)
        s.curve_vertex(self.v4.x, self.v4.y)
        s.curve_vertex(self.v4.x, self.v4.y)
        s.end_shape(py5.CLOSE)
        py5.shape(s)

        py5.fill(*self.c2)
        s = py5.create_shape()
        s.begin_shape()
        s.curve_vertex(self.v1.x, self.v1.y)
        s.curve_vertex(self.v1.x, self.v1.y)
        s.curve_vertex(*random_point)
        s.curve_vertex(self.v3.x, self.v3.y)
        s.curve_vertex(*random_point)
        s.curve_vertex(self.v2.x, self.v2.y)
        s.curve_vertex(self.v2.x, self.v2.y)
        s.end_shape(py5.CLOSE)
        py5.shape(s)
