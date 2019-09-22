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


def init_sketch():
    global by_dist, COLORS

    COLORS = get_color_palette()
    by_dist = {}

    for i in range(1200):
        by_dist[i] = choice(COLORS)



def setup():
    size(600, 600)
    noStroke()
    init_sketch()


def draw():
    print(COLORS)
    step = 20

    for x in range(0, width + step, step):
        for y in range(0, height + step, step):
            dist_from_center = int(dist(x, y, width / 2, height / 2))
            fill(by_dist[dist_from_center])

            r_x = abs(x - width / 2)
            r_x = map(r_x, 0, width/2, 20, 60)
            r_y = abs(y - height / 2)
            r_y = map(r_y, 0, height/2, 20, 60)
            ellipse(x, y, r_x, r_y)

    noLoop()

def keyPressed():
    if key == 'n':
        loop()
        init_sketch()
        redraw()
    elif key == 's':
        saveFrame("########.png")