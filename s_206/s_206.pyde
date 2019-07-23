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
colors = []


def init_angles(count):
    global angles, colors

    colors = cycle(get_color_palette())
    angles = []
    for i in range(count):
        angles.append(random(TWO_PI))

    angles.sort()
    frameRate(12)


def setup():
    #size(1000, 1000)
    fullScreen()
    init_angles(7)
    strokeWeight(4)
    stroke(27, 27, 27, 130)


def draw():
    background(27)

    with draw_at_center():
        for r in range(max_r, min_r, -10):
            points = []

            for angle in angles:
                points.append(
                    polar_coordinate(0, 0, r, angle)
                )

            fill(next(colors))
            draw_shape([points[-1]] + points + [points[0]], end_shape_mode=CLOSE, vertex_func=curveVertex)

    if not frameCount % (12 * 5):
        init_angles(int(random(3, 10)))

    print(frameRate)


def keyPressed():
    global colors

    if key == 'n':
        init_angles(int(random(3, 10)))