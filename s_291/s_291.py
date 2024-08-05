import dataclasses
import itertools
import random
from functools import cached_property
from itertools import cycle

import py5
import tqdm

BACKGROUND = (232, 232, 232)

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

    @property
    def pos(self):
        return py5.Py5Vector(self.x, self.y)

    def draw(self):
        angle =  py5.random(0, py5.TWO_PI)
        self.angle = angle

        v1 = polar_coordinate(self.x, self.y, self.h_main, self.angle)
        v2 = polar_coordinate(self.x, self.y, - self.h_main, self.angle)
        py5.stroke(*self.c_main)
        py5.line(v1.x, v1.y, v2.x, v2.y)

        # right
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



def setup():
    global img, rotated_img
    py5.size(900, 900, py5.P2D)
    py5.background(*BACKGROUND)
    py5.stroke_weight(5)


    points = list(itertools.product(range(py5.width), range(py5.height)))
    random.shuffle(points)
    for x, y in tqdm.tqdm(points):
        line = LineWithNeighbors(x=x, y=y)
        line.draw()

    #py5.save_frame("cover.png")


py5.run_sketch()
