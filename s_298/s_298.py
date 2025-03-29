import itertools

import py5
import random

B = 27
C = 255 - B
COLORS = [
    (C, C, C),
    (C, C, C),
    (B, C, C),
    (C, B, C),
    (C, C, B),
    (B, B, C),
    (B, C, B),
    (C, B, B),
]


class CirclePattern:

    def __init__(self, pos, r):
        self.pos = pos
        self.r = r

    def inner_radius(self, n):
        r_rate = self.r // n
        return range(self.r, r_rate - 1, -r_rate)

    @classmethod
    def random_pattern(cls, pos, r):
        pattern_names = [name for name in dir(cls) if name.startswith("pattern_")]
        drawer = cls(pos, r)
        pattern = getattr(drawer, random.choice(pattern_names))
        pattern()

    def pattern_1(self):
        """
        Fulfilled circle with radius r
        """
        self.pattern_3(py5.TWO_PI)

    def pattern_2(self, n=5):
        """
        Circle with n sub circles
        """
        self.pattern_4(py5.TWO_PI, n=n)

    def pattern_3(self, angle=py5.PI):
        """
        Fulfilled arc with radius r and a certain angle. There's a rotation to avoid having every
        arc with the same orientation.
        """
        py5.push_matrix()
        self.rotate()

        color = random.choice(COLORS)
        py5.fill(*color)

        mode = py5.CLOSE if angle == py5.TWO_PI else py5.PIE
        py5.arc(0, 0, self.r, self.r, 0, angle, mode)

        py5.pop_matrix()

    def pattern_4(self, angle=py5.PI, n=10):
        """
        Same as the arc patter but with sub arcs
        """
        py5.push_matrix()
        self.rotate()

        mode = py5.CLOSE if angle == py5.TWO_PI else py5.PIE
        p_color = None
        for i_r in self.inner_radius(n):
            color = random.choice(COLORS)
            while color == p_color:
                color = random.choice(COLORS)
            p_color = color

            py5.fill(*color)
            py5.arc(0, 0, i_r, i_r, 0, angle, mode)

        py5.pop_matrix()

    def pattern_5(self, n=10):
        self.pattern_4(py5.HALF_PI, n=n)

    def pattern_6(self, n=10):
        self.pattern_4(py5.HALF_PI * 3, n=n)

    def pattern_7(self):
        self.pattern_3(py5.HALF_PI)

    def pattern_8(self):
        self.pattern_3(py5.HALF_PI * 3)

    def rotate(self):
        rotation_angles = [0, py5.HALF_PI, py5.PI, py5.PI + py5.HALF_PI]
        py5.translate(self.pos.x, self.pos.y)
        py5.rotate(random.choice(rotation_angles))


def setup():
    py5.size(1000, 1000)
    py5.background(B)
    py5.stroke(B)
    py5.stroke_weight(5)

    # TODO: distribuir esferas por raios conectados a uma altura H e indo para o máximo de heigh com um offset
    #     /|\
    #    / | \
    #   /  |  \
    #  /   |   \

    w, h = py5.width, py5.height
    x_range = range(0, w + 100, 100)
    y_range = range(0, h + 100, 100)
    coords = list(itertools.product(x_range, y_range))
    random.shuffle(coords)

    used = set()
    while coords:
        x, y = coords.pop()
        pos = py5.Py5Vector(x, y)
        CirclePattern.random_pattern(pos, 200)
        used.add((x, y))

    py5.save_frame("cover-temp.png")



py5.run_sketch()
