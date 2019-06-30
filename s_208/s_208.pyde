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

max_r = 450
min_r = 10
angles = []
colors = cycle(get_color_palette())


def init_angles(count):
    global angles, colors

    colors = cycle(get_color_palette())
    angles = []
    for i in range(count):
        angles.append(random(TWO_PI))

    angles.sort()
    frameRate(12)


def setup():
    size(1200, 1200)
    init_angles(7)
    strokeWeight(4)


def draw():
    background(27)

    with draw_at_center():
        for r in range(max_r, min_r, -10):
            points = []

            stroke(255, 255, 255, 121)
            for angle in angles:
                point_area = [-40, 40]
                x_noise_index = frameCount * angle * 0.05
                y_noise_index = frameCount * angle * 0.06 + 1042

                x = map(noise(x_noise_index), 0, 1, *point_area)
                y = map(noise(y_noise_index), 0, 1, *point_area)

                p = polar_coordinate(x, y, r, angle)
                points.append(p)


            fill(next(colors))
            if r <= min_r * 10:
                fill(27)
                noStroke()

            draw_shape(points, end_shape_mode=CLOSE, vertex_func=curveVertex)


def keyPressed():
    if key == 'n':
        init_angles(int(random(5, 14)))