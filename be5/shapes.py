import itertools
from functools import cached_property

import py5
import random
from be5.coords import polar_coordinate
from be5.draw import draw_shape

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



class MovingShape:

    def __init__(self, *points):
        self.points = points
        self.moving_point = None
        self.target = None

    @cached_property
    def moving_list(self):
        return itertools.cycle(self.points)

    def move(self):
        if not self.target and not self.moving_point:
            self.assign_new_moving_point()

        direction = self.target - self.moving_point
        direction.normalize()
        direction *= 3

        self.moving_point += direction

        tx, ty = int(self.target.x), int(self.target.y)
        px, py = int(self.moving_point.x), int(self.moving_point.y)
        mag = direction.mag
        if all([
            bool(tx - mag <= px <= tx + mag),
            bool(ty - mag <= py <= ty + mag),
        ]):
            self.moving_point = None
            self.target = None

    def assign_new_moving_point(self):
        self.moving_point = next(self.moving_list)
        new_target = None
        while not new_target:
            new_target = py5.Py5Vector(self.moving_point.x, self.moving_point.y)
            new_target.normalize()
            new_target.rotate(py5.random(0, py5.TWO_PI))
            new_target *= py5.random(100, 300)
            new_target += self.moving_point
            offset = 100
            if not (offset <= new_target.x <= py5.width - offset):
                new_target = None
            elif not offset <= new_target.y <= py5.height - offset:
                new_target = None

        self.target = new_target

    def draw(self):
        c = (99, 42, 232, 10)

        py5.stroke(*c)
        py5.no_fill()

        s = py5.create_shape()
        s.begin_shape()

        s.curve_vertex(self.points[0].x, self.points[0].y)
        for point in self.points:
            s.curve_vertex(point.x, point.y)
        s.curve_vertex(self.points[-1].x, self.points[-1].y)

        s.end_shape(py5.CLOSE)
        py5.shape(s)

        debug = False
        if debug and self.target:
            py5.stroke(255, 9, 255)
            py5.circle(self.target.x, self.target.y, 2)


class WithCenterShape:

    def __init__(self, center, radius, num_points, radius_noise=0, radius_off=0):
        self.center = center
        self.radius = radius
        self.num_points = num_points
        self.radius_noise = radius_noise
        self.angle = py5.TWO_PI / self.num_points
        self.off = radius_off

    @property
    def points(self):
        for i in range(0, self.num_points + 1):
            radius_off = py5.random(-self.off, self.off) * self.radius_noise
            radius = self.radius + radius_off

            angle = i * self.angle
            yield polar_coordinate(
                self.center.x, self.center.y, radius, angle
            )

    def draw(self):
        draw_shape(self.points)
