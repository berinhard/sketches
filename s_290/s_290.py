import dataclasses
import random
from functools import cached_property
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
class ImageSection:
    x: int
    y: int
    pixels: list

    def draw(self):
        for x, y, c in self.pixels:
            py5.set_pixels(x + self.x, y + self.y, c)

@dataclasses.dataclass
class BrokenImage:
    path: str
    x: int
    y: int
    num_sections: int = 20

    @cached_property
    def img(self) -> py5.Image:
        img = py5.load_image(self.path)
        img.load_pixels()
        return img

    @property
    def sections(self):
        range_mod = 75
        step = 25
        w, h = self.img.width, self.img.height
        section_len = w / self.num_sections
        sections_x_values = range(0, w, int(section_len))

        prev_v = None
        for section_x in sections_x_values[:-1]:
            pixels = []
            for pixel_x in range(section_x, int(section_x + section_len)):
                for pixel_y in range(0, h):
                    pixels.append((pixel_x, pixel_y, self.img.get_pixels(pixel_x, pixel_y)))

            y_offset_range = range(-range_mod, range_mod + step, step)
            y_offset = prev_v
            while y_offset == prev_v:
                y_offset = random.choice(y_offset_range)
            prev_v = y_offset
            y = self.y + y_offset
            yield ImageSection(self.x + section_x // 2, y, pixels)

    def draw(self):
        # py5.image(self.img, self.x, self.y)
        for section in self.sections:
            section.draw()


def setup():
    global img, rotated_img
    py5.size(900, 900, py5.P2D)
    py5.background(*BACKGROUND)

    img = BrokenImage("image.jpeg", 70, 100)
    img.draw()
    py5.save_frame("borges.png")


py5.run_sketch()
