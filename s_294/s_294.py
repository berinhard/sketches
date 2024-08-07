import dataclasses
import itertools
import random
from functools import cached_property
from itertools import cycle
import shapely
import numpy as np

import py5
import tqdm

BACKGROUND = [34,]
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
    h_second: int = 8
    c_main: list[int, int, int] = (17, 17, 17)
    c_second: list[int, int, int] = (232, 17, 17)

    def __post_init__(self):
        self.angle = random.choice([0, py5.HALF_PI, py5.PI, py5.THIRD_PI])#py5.random(0, py5.TWO_PI)
        self.h_second = 5
        self.c_second = list(self.c_second)

    def draw(self):
        v1 = polar_coordinate(self.x, self.y, self.h_main, self.angle)
        v2 = polar_coordinate(self.x, self.y, - self.h_main, self.angle)
        py5.stroke(*self.c_main)
        py5.stroke_weight(3)
        py5.line(v1.x, v1.y, v2.x, v2.y)

        # right
        py5.stroke_weight(py5.random(1, 2))
        c_second = list(self.c_second)
        self.c_second[0] = c_second[0] + py5.random(-50, 50)
        off_v1 = polar_coordinate(v1.x, v1.y, self.h_second, self.angle)
        py5.stroke(*self.c_second)
        py5.line(v1.x, v1.y, off_v1.x, off_v1.y)

        # left
        self.c_second[0] = c_second[0] + py5.random(-50, 50)
        off_v2 = polar_coordinate(v2.x, v2.y, - self.h_second, self.angle)
        py5.stroke(*self.c_second)
        py5.line(v2.x, v2.y, off_v2.x, off_v2.y)


def setup():
    global img, rotated_img
    py5.size(900, 900, py5.P2D)
    py5.background(*BACKGROUND)

    print("Building all points map...")
    all_points = itertools.product(range(py5.width), range(py5.height))
    all_points = np.array([shapely.Point(x, y) for x, y in all_points])
    print("Done.")

    off = 150
    x_range = list(range(off, py5.width - off, 30))
    y_range = list(range(off, py5.height - off, 60))
    shape_points = [(random.choice(x_range), random.choice(y_range)) for _ in range(4)]
    shape_1 = shapely.Polygon(shape_points)
    shape_points = [(random.choice(x_range), random.choice(y_range)) for _ in range(7)]
    shape_2 = shapely.Polygon(shape_points)


    print("Calculating intersections...")
    shape_1_points = all_points[shapely.contains(shape_1, all_points)]
    shape_2_points = all_points[shapely.contains(shape_2, all_points)]
    print("Done")

    c_list = [RED, OFF_WHITE]
    colors = itertools.cycle(cycle(c_list))
    for point in tqdm.tqdm(shape_1_points, desc="Rendering points from Shape 1"):
        if point.within(shape_2):
            continue
        line = LineWithNeighbors(x=point.x, y=point.y, c_second=next(colors))
        line.draw()

    c_list = [CINNAMON, SILVER]
    colors = itertools.cycle(cycle(c_list))
    for point in tqdm.tqdm(shape_2_points, desc="Rendering points from Shape 2"):
        if point.within(shape_1):
            continue
        line = LineWithNeighbors(x=point.x, y=point.y, c_second=next(colors))
        line.draw()

    c_name = str(c_list).replace(" ", "-")
    py5.save_frame(f"cover-{c_name}.png")


py5.run_sketch()
