# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)


def setup():
    size(900, 900)
    strokeWeight(2)
    stroke(WHITE)
    noFill()
    frameRate(24)


def draw():
    background(BLACK)

    with draw_at_center():
        rotate(radians(frameCount / 4.0))
        n = noise(frameCount * 0.012)
        r = map(n, 0, 1, 2, 50)
        a = map(n, 0, 1, 255, 10)
        stroke(235, 235, 245, a)
        rate = int(r)
        angle_rate = PI / rate
        angles = [angle_rate * i for i in range(rate)]

        for angle in angles:
            r = map(n, 0, 1, 0, width / 2)
            regular_polygon(0, 0, r, 3, angle)

    save_video_frames(30, 24)