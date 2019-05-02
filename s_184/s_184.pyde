# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice


easings_func = [
    easings.easeInOutSine,
    easings.easeInOutQuad,
    easings.easeInOutCubic,
]


TOTAL_FRAMES = 200.0

def get_percent(total_frames, counter=None):
    counter = counter or frameCount
    return counter % total_frames / total_frames


COLORS = get_color_palette()


class SplitedCircle(object):

    def __init__(self, x, y, r, num_slices):
        self.x, self.y = x, y
        self.r = r * 2
        self.num_slices = num_slices
        self.slice_angle = TWO_PI / num_slices
        self.slice_angles = [i * self.slice_angle for i in range(num_slices + 1)]
        self.easing = choice(easings_func)

    def display(self, percent, invert_rotation=False):
        percent = self.easing(percent)
        if invert_rotation:
            percent *= -1

        with pushMatrix():
            rotate(TWO_PI * percent)
            for i, angle in enumerate(self.slice_angles):
                start_angle = self.slice_angles[i - 1]
                noStroke()
                fill(colors[i])
                arc(self.x, self.y, self.r, self.r, start_angle, angle, PIE)


circles = []
colors = []
def setup():
    size(900, 900)
    num_slices = 8

    prev_color = choice(COLORS)
    for i in range(num_slices + 1):
        c = choice(COLORS)
        while c == prev_color:
            c = choice(COLORS)
        colors.append(c)
        prev_color = c

    circles.extend([
        SplitedCircle(0, 0, 350, num_slices),
        SplitedCircle(0, 0, 250, num_slices),
        SplitedCircle(0, 0, 150, num_slices),
    ])


def draw():
    background(240)
    with draw_at_center():
        percent = get_percent(TOTAL_FRAMES)
        for i, circle in enumerate(circles):
            circle.display(percent, invert_rotation=bool(i % 2))

        fill(240)
        ellipse(0, 0, 100, 100)

    if frameCount == TOTAL_FRAMES:
        noLoop()
    saveFrame("#####.png")