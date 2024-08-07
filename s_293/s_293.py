"""
This was a bug I got in the middle of the idea from s_292.
I decided to keep it because I liked the final result.
Happy accidents.
"""

import dataclasses
import itertools
import random
from functools import cached_property
from itertools import cycle

import py5
import tqdm

BACKGROUND = (17,17,17)
RED = (232, 17, 17)

def polar_coordinate(x0, y0, r, angle):
    x = x0 + r * py5.cos(angle)
    y = y0 + r * py5.sin(angle)

    return py5.Py5Vector(x, y)


@dataclasses.dataclass
class LineWithNeighbors:
    x: int
    y: int
    angle: int = 0
    h_main: int = 10
    c_main: list[int, int, int] = (17, 17, 17)
    c_second: list[int, int, int] = (232, 17, 17)

    def __post_init__(self):
        self.angle = py5.random(0, py5.TWO_PI)

    def draw(self):
        v1 = polar_coordinate(self.x, self.y, self.h_main, self.angle)
        v2 = polar_coordinate(self.x, self.y, - self.h_main, self.angle)
        py5.stroke(*self.c_main)
        py5.stroke_weight(5)
        py5.line(v1.x, v1.y, v2.x, v2.y)

        # right
        py5.stroke_weight(py5.random(1, 3))
        self.c_second = list(self.c_second)
        self.c_second[0] = 200 + py5.random(-50, 50)
        off_v1 = polar_coordinate(v1.x, v1.y, self.h_main / 2, self.angle)
        py5.stroke(*self.c_second)
        py5.line(v1.x, v1.y, off_v1.x, off_v1.y)

        # left
        self.c_second[0] = 299 + py5.random(-50, 50)
        off_v2 = polar_coordinate(v2.x, v2.y, - self.h_main / 2, self.angle)
        py5.stroke(*self.c_second)
        py5.line(v2.x, v2.y, off_v2.x, off_v2.y)


def fill_area(points, shuffle=False, **kwargs):
    if shuffle:
        points = list(points)
        random.shuffle(points)

    for x, y in tqdm.tqdm(points):
        line = LineWithNeighbors(x=x, y=x, **kwargs)
        line.draw()


def setup():
    global img, rotated_img
    py5.size(900, 900, py5.P2D)
    py5.background(*BACKGROUND)


    range_of_x = [
        (200, 300),
        (500, 600),
        (700, 800),
    ]
    range_of_y = range_of_x[::-1]

    for x1, x2 in range_of_x:
        range_of_points = itertools.product(range(x1, x2), range(py5.height))
        fill_area(range_of_points, shuffle=True, c_second=RED)

    # for y1, y2 in range_of_y:
    #     range_of_points = itertools.product(range(py5.width), range(y1, y2))
    #     fill_area(range_of_points, shuffle=True, c_second=RED)

    py5.save_frame("cover.png")


py5.run_sketch()
