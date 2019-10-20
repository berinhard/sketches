# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from itertools import cycle
from random import choice



max_r = 400
segments = 10

COLORS = cycle(get_color_palette())


def setup():
    size(900, 900)
    background(27)
    frameRate(10)


percent = 0
percent_inc = 0.005

def get_percent(total_frames, counter=None):
    counter = counter or frameCount
    return counter % total_frames / total_frames

def draw():
    global percent, COLORS

    translate(width / 2, height / 2)
    p0 = PVector(0, 0)
    p1 = polar_coordinate(p0.x, p0.y, max_r, 0)

    num_sequences = 12
    base_angle = TWO_PI / num_sequences

    strokeWeight(3)
    for a in range(num_sequences):
        with pushMatrix():
            rotate(a * base_angle)

            raw_c = unhex(next(COLORS)[1:])
            c = color(raw_c)
            r, g, b = red(c), green(c), blue(c)
            stroke(r, g, b, 80)

            for i in range(1, (segments + 1)):
                with pushMatrix():
                    start = PVector.lerp(p0, p1, (i - 1) / float(segments))
                    end = PVector.lerp(p0, p1, i / float(segments))
                    rotate(i * percent * (TWO_PI / 36))
                    line(start.x, start.y, end.x, end.y)

    noStroke()
    fill(27)
    ellipse(0, 0, max_r / segments, max_r / segments)

    percent += percent_inc

    if not frameCount % 60:
        saveFrame("########.png")
        COLORS = cycle(get_color_palette())
        background(27)
        percent = 0
