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


def setup():
    size(900, 900)
    background(240)
    stroke(color(27, 27, 27))
    strokeWeight(2)


def draw():
    background(220)
    r = 400

    n_pairs = 3
    colors = get_color_palette()

    with pushMatrix():
        translate(width / 2, height / 2)
        points = []
        prev_angle = 0


        n_pairs = 4
        angle_inc = TWO_PI / n_pairs
        all_angles = [angle_inc * (i + 1) for i in range(16)]

        prev_angle = 0
        for i in range(n_pairs):
            angle = random(prev_angle, all_angles[i])
            pos = polar_coordinate(0, 0, r, angle)
            prev_angle += angle

            angle = random(prev_angle, all_angles[i])
            scaled_r = r / 2
            iner_pos = polar_coordinate(0, 0, scaled_r, angle)
            prev_angle += angle

            points.extend([pos, iner_pos])
            prev_angle = all_angles[i]

        from itertools import combinations
        for sub_points in combinations(points, 3):
            fill(choice(colors))
            draw_shape(sub_points,  end_shape_mode=CLOSE)

    noLoop()


def keyPressed():
    if key == 'n':
        redraw()
    if key == 's':
        saveFrame("#####.png")