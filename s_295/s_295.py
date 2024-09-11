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
DARK_ORANGE = (255, 140, 17)
BURNT_ORANGE = (204, 85, 17)
PUMPKIN = (255, 117, 24)
ORANGE_RED = (255, 69, 17)
TANGERINE = (242, 133, 17)
CARROT_ORANGE = (237, 145, 33)
COPPER = (184, 115, 51)
AMBER = (255, 191, 17)
CINNAMON = (210, 105, 30)
RUST = (183, 65, 14)

# White colors that match well with the orange variations
PURE_WHITE = (255, 255, 255)
IVORY = (255, 255, 240)
BEIGE = (245, 245, 220)
ALABASTER = (240, 234, 214)
CREAM = (255, 253, 208)
PEARL = (234, 234, 234)
SILVER = (192, 192, 192)
OFF_WHITE = (250, 250, 250)
LAVENDER_BLUSH = (255, 240, 245)
HONEYDEW = (240, 255, 240)

# Pink colors that complement the orange variations
LIGHT_PINK = (255, 182, 193)
HOT_PINK = (255, 105, 180)
DEEP_PINK = (255, 20, 147)
PINK = (255, 192, 203)
DARK_ORCHID = (153, 50, 204)
MEDIUM_VIOLET_RED = (199, 21, 133)
ORCHID = (218, 112, 214)
FUCHSIA = (255, 0, 255)
PALE_VIOLET_RED = (219, 112, 147)
LAVENDER = (230, 230, 250)

# Green colors that complement the orange variations
FOREST_GREEN = (34, 139, 34)
OLIVE = (128, 128, 0)
LIME = (0, 255, 0)
SEAGREEN = (46, 139, 87)
MEDIUM_SEA_GREEN = (60, 179, 113)
DARK_OLIVE_GREEN = (85, 107, 47)
PALE_GREEN = (152, 251, 152)
SPRING_GREEN = (0, 255, 127)
CHARTREUSE = (127, 255, 0)
MINT_CREAM = (245, 255, 250)


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


def render(colors=None):
    colors = itertools.cycle(colors or [RED, PURE_WHITE])
    range_of_x = [
        (200, 300),
        (500, 600),
        (700, 800),
    ]

    for x1, x2 in range_of_x:
        c = next(colors)
        range_of_points = itertools.product(range(x1, x2), range(py5.height))
        fill_area(range_of_points, shuffle=True, c_second=c)


def setup():
    global img, rotated_img
    py5.size(900, 900, py5.P2D)
    py5.background(*BACKGROUND)


    render()

    angles = [90, 270, 133]
    for angle in angles:
        py5.push_matrix()
        py5.translate(py5.width / 2, py5.height / 2)
        py5.rotate(angle)

        render(colors=[PUMPKIN, SILVER])

        py5.pop_matrix()

    py5.save_frame("cover.png")


py5.run_sketch()
