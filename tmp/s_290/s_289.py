import dataclasses
import random

import py5

from be5.shapes import TriSquare as BaseTriSquare


SIZE = 900
BACKGROUND = (42, 42, 42)
LINE = (220, 220, 220, 10)
C1 = (54, 169, 27)
C2 = (74, 94, 206)
C3 = (21, 21, 21)

# balance c1 or c3 qtd
COLORS = [C1, C2, C2]

@dataclasses.dataclass
class InnerCircles:
    center: py5.Py5Vector
    radius: int
    inner_count: int

    @property
    def delta_r(self):
        return self.radius // self.inner_count

    def draw(self):
        c1 = self.center

        min_r = 10
        max_r = self.radius + min_r
        for r in reversed(range(min_r, max_r, self.delta_r)):
            y = py5.remap(r, min_r, max_r, self.center.y - self.radius/2, self.center.y)
            py5.circle(c1.x, y, r)


SHAPES = []
def populate_shapes():
    center = py5.Py5Vector(400, 400)
    SHAPES.append(InnerCircles(center, 60, 5))

def setup():
    py5.size(SIZE, SIZE, py5.P2D)
    populate_shapes()

def draw():
    with py5.push():
        #py5.translate(150, 150)
        for shape in SHAPES:
            shape.draw()

    if py5.is_key_pressed:
        if py5.key in ['s', 'S']:
            py5.save_frame("cover03.png")
        elif py5.key in ['n', "N"]:
            populate_shapes()


py5.run_sketch()
