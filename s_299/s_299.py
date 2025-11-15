import dataclasses
import itertools
import random
from functools import cached_property
from pathlib import Path
from statistics import mean

import cv2
import py5

# IMAGE_NAME = "bernardo-carnaval.jpeg"
IMAGE_NAME = "0005.jpg"
NUM_WALKERS = 350
OFFSET = 50
STROKE_WEIGHT = 1.5
BACKGROUND = (40, )
ALPHA = 205
BLACK = 7


im = cv2.imread(IMAGE_NAME)
h, w, c = im.shape


@dataclasses.dataclass
class ImageSection:
    x: int
    y: int
    pixels: list

    def draw(self):
        for x, y, c in self.pixels:
            py5.set_pixels(x + self.x, y + self.y, c)


@dataclasses.dataclass
class Walker():
    x: int
    y: int
    r: int
    color: tuple
    dir: int = 0
    pace_mult: int = 2

    def draw(self):
        py5.fill(self.color)
        py5.stroke_weight(STROKE_WEIGHT)
        py5.stroke(BLACK, BLACK, BLACK, ALPHA)
        py5.square(self.x, self.y, self.r)

    def move(self):
        if self.dir is None:
            self.dir = random.randint(0, 3)

        cur_dir = random.randint(0, 3)
        while self.dir is None or abs(cur_dir - self.dir) == 2:
            cur_dir = random.randint(0, 3)


        pace = self.r / 2
        match self.dir:
            case 0:
                self.x -= pace
            case 1:
                self.y -= pace
            case 2:
                self.x += pace
            case 3:
                self.y += pace

        self.dir = cur_dir


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
            walkers.append(Walker(x + OFFSET / 2, y + OFFSET / 2, r=OFFSET/2, color=color))
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
