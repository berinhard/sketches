# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings


def setup():
    size(900, 900)
    background(240)
    stroke(color(27, 27, 27))
    strokeWeight(3)


def draw():
    background(240)
    r = 400

    with pushMatrix():
        translate(width / 2, height / 2)
        points = []
        prev_angle = 0
        for i in range(3):
            angle = random(TWO_PI - prev_angle)
            pos = polar_coordinate(0, 0, r, angle)
            prev_angle += angle
            angle = random(angle, prev_angle)
            scaled_r = r / 2
            iner_pos = polar_coordinate(0, 0, scaled_r, angle)
            prev_angle += angle

            points.extend([pos, iner_pos])

        fill(27)
        draw_shape(points, end_shape_mode=CLOSE)

        fill(240)
        draw_shape(points[len(points) / 2:], end_shape_mode=CLOSE)
        fill(201, 25, 35)
        draw_shape(points[:len(points) / 2], end_shape_mode=CLOSE)

    noLoop()


def keyPressed():
    if key == 'n':
        redraw()
    if key == 's':
        saveFrame("#####.png")