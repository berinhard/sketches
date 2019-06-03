# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

inner_cube_size = 40
main_cube_size = 400
cubes = []

x_values = range(0, 800, inner_cube_size)
y_values = range(0, 800, inner_cube_size)

def setup():
    size(800, 800)
    stroke(27, 27, 27, 50)
    strokeWeight(2)


def draw():
    background(240)
    center_x, center_y = width / 2, height / 2

    for x in x_values:
        for y in y_values:
            diff = noise(x + frameCount * 0.04, y + frameCount * 0.08) * 50
            line(x + diff, y - diff, center_x, center_y)

    saveFrame("cover.png")