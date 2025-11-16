import dataclasses
import itertools
import logging
import random
from functools import cached_property
from statistics import mean

import cv2
import py5

IMAGE_NAME = "0001.JPG"
NUM_WALKERS = 350
OFFSET = 50
STROKE_WEIGHT = 1.5
BACKGROUND = (40, )
ALPHA = 205
BLACK = 7


im = cv2.imread(IMAGE_NAME)
h, w, c = im.shape


@dataclasses.dataclass
class Walker():
    x: int
    y: int
    r: int
    color: tuple
    dir: int = 0
    pace_mult: int = 1

    @property
    def vertices(self):
        return [
            (self.x - self.r, self.y - self.r),
            (self.x + self.r, self.y - self.r),
            (self.x + self.r, self.y + self.r),
            (self.x - self.r, self.y + self.r),
        ]
    def rand_dir(self, num):
        return random.randint(0, num - 1)

    def valid_next_cur(self, cur_dir, num_dir):
        is_opposite_direction = abs(cur_dir - self.dir) == num_dir // 2
        next_to_opposite = abs(abs(cur_dir - num_dir) - self.dir) in [1, 2]

        logging.debug(f"{cur_dir=}, {self.dir=}, {is_opposite_direction=}, {next_to_opposite=}")

        if is_opposite_direction:
            return False

        if next_to_opposite:
            return False

        return True

    def move(self):
        num_dir = 8

        if self.dir is None:
            self.dir = self.rand_dir(num_dir)

        cur_dir = self.rand_dir(num_dir)
        while not self.valid_next_cur(cur_dir, num_dir):
            cur_dir = self.rand_dir(num_dir)

        pace = self.r
        pace *= self.pace_mult
        match self.dir:
            case 0:
                self.y -= pace
            case 1:
                self.y -= pace / 2
                self.x += pace / 2
            case 2:
                self.x += pace
            case 3:
                self.y += pace / 2
                self.x += pace / 2
            case 4:
                self.y += pace
            case 5:
                self.y += pace / 2
                self.x -= pace / 2
            case 6:
                self.x -= pace
            case 7:
                self.y -= pace / 2
                self.x -= pace / 2

        self.dir = cur_dir

    def draw(self):
        py5.fill(self.color)
        py5.stroke_weight(STROKE_WEIGHT)
        py5.stroke(BLACK, BLACK, BLACK, ALPHA)



class SquareWalker(Walker):

    def draw(self):
       super().draw()
       py5.square(self.x, self.y, self.r)


class TriangleWalker(Walker):

    def draw(self):
        """
        4 vertices of a square can compose 4 triangles
        """
        super().draw()

        triangle_points = set()
        while len(triangle_points) < 3:
            triangle_points.add(random.choice(self.vertices))
            logging.debug(f"{triangle_points=}")

        triangle_points = list(triangle_points)
        py5.triangle(
            triangle_points[0][0],
            triangle_points[0][1],
            triangle_points[1][0],
            triangle_points[1][1],
            triangle_points[2][0],
            triangle_points[2][1],
        )


@dataclasses.dataclass
class BrokenImage:
    path: str
    x: int
    y: int

    @cached_property
    def img(self) -> py5.Image:
        img = py5.load_image(self.path)
        img.load_pixels()
        return img

    @cached_property
    def walkers(self):
        walkers = []
        chosen = set()
        while len(chosen) < NUM_WALKERS:
            x = int(py5.random(0, py5.width)) // OFFSET * OFFSET
            y = int(py5.random(0, py5.height)) // OFFSET * OFFSET
            if (x, y) in chosen:
                continue

            print(f"Creating {len(chosen) + 1}/{NUM_WALKERS} walker...")

            r, g, b = [], [], []
            for c_x, c_y in itertools.product(range(OFFSET), range(OFFSET)):
                color = self.img.get_pixels(x + c_x, y + c_y)
                r.append(py5.red(color))
                g.append(py5.green(color))
                b.append(py5.blue(color))

            r = mean(r)
            g = mean(g)
            b = mean(b)

            color = py5.color(r, g, b)

            if random.random() >= 0.9:
                walkers.append(SquareWalker(x + OFFSET / 2, y + OFFSET / 2, r=OFFSET, color=color, pace_mult=0.5))
            else:
                walkers.append(TriangleWalker(x + OFFSET / 2, y + OFFSET / 2, r=OFFSET / 2, color=color, pace_mult=1))

            chosen.add((x, y))
        return walkers

    def draw(self):
        for walker in self.walkers:
            walker.draw()
            walker.move()


def setup():
    global img, rotated_img
    py5.size(w, h, py5.P2D)
    py5.background(*BACKGROUND)

    img = BrokenImage(IMAGE_NAME, 0,0)
    py5.image(img.img, 0,0)

def draw():
    img.draw()
    targets = list(range(50, 601, 50))
    if py5.frame_count in targets:
       py5.save_frame(f"{py5.frame_count:03d}.png")

    if py5.frame_count == 601:
        py5.no_loop()




py5.run_sketch()
