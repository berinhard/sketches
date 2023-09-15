import py5
import random

COLORS = [
    (232, 232, 53),
    (80, 27, 27),
]

class TriSquare:

    def __init__(self, v1, v2, v3, v4):
        self.v1, self.v2, self.v3, self.v4 = v1, v2, v3, v4
        colors = COLORS[:]
        random.shuffle(colors)
        self.c1, self.c2 = colors

    def draw(self):
        py5.stroke_weight(1.1)
        py5.fill(*self.c1)
        py5.stroke(*self.c1)
        py5.triangle(self.v1.x, self.v1.y, self.v3.x, self.v3.y, self.v4.x, self.v4.y)
        py5.fill(*self.c2)
        py5.stroke(*self.c2)
        py5.triangle(self.v1.x, self.v1.y, self.v3.x, self.v3.y, self.v2.x, self.v2.y)
