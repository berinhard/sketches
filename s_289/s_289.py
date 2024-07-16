import dataclasses
import random
from itertools import cycle

import py5

STROKE_WEIGHT = 2.5
BACKGROUND = (40, )
ALPHA = 225
C1 = (34, 139, 20, ALPHA)
C2 = (64, 84, 196, ALPHA)
C3 = (242, 242, 242, ALPHA)

COLORS = cycle([C1, C2, C3, C1, C2] * 20)

@dataclasses.dataclass
class Rectangle:
    x: int
    y: int
    w: int
    h: int

    def draw(self):
        py5.stroke(*next(COLORS))
        py5.rect(self.x, self.y, self.w, self.h)

@dataclasses.dataclass
class BrokenRectangle:
    x: int
    y: int
    w: int
    h: int
    num_sections: int

    @property
    def sections(self):
        section_len = self.w // self.num_sections
        range_mod = 50
        step = 25
        x_range = range(self.x, self.x + self.w, section_len)
        for i, x in enumerate(x_range):
            y_offset_range = range(-range_mod, range_mod + step, step)
            y = self.y + random.choice(y_offset_range)
            yield Rectangle(x, y, section_len, self.h)


def setup():
    py5.size(700, 700, py5.P2D)
    py5.no_fill()
    py5.stroke_weight(STROKE_WEIGHT)
    py5.background(*BACKGROUND)

def draw():
    py5.translate(py5.width / 2, py5.height / 2)
    halfs = [
        py5.TWO_PI,
        py5.HALF_PI,
    ]

    quarters = [
        py5.QUARTER_PI,
        py5.QUARTER_PI * 2,
        py5.QUARTER_PI * 3,
        py5.QUARTER_PI * 4,
    ]

    thirds = [
        py5.THIRD_PI,
        py5.THIRD_PI * 2,
        py5.THIRD_PI * 3,
        py5.THIRD_PI * 4,
        py5.THIRD_PI * 5,
        py5.THIRD_PI * 6,
    ]

    OCT_PI = py5.PI / 8
    octs = [
        OCT_PI * i for i in range(1, 9)
    ]

    angles = octs
    for angle in angles:
        py5.push_matrix()

        py5.rotate(angle)
        broken = BrokenRectangle(-250, -125, 500, 250, 20)
        for section in broken.sections:
            section.draw()

        py5.pop_matrix()

    py5.save_frame(f"{len(angles)}.png")
    py5.no_loop()


py5.run_sketch()
