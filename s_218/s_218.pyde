# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings


colors = get_color_palette()


def setup():
    size(1000, 400)
    background(250)
    stroke(42, 42, 42)
    strokeWeight(5)


px, py = 0, 0
x = 0
step = 20
def draw():
    global x, px, py
    #if frameCount > 1:
     #   noLoop()

    step = 50
    for base_y in range(0, height + step, step):
        for x in range(0, width + step, step):
            with pushMatrix():
                translate(0, base_y)

                dist_from_center = abs(width / 2 - x)
                percent_from_center = map(dist_from_center, 0, width / 2, 0, 1)
                max_y = height / 2

                y = random(0, percent_from_center) * max_y
                line(x - step, 0, x, y)
                line(x, y, x + step, 0)

                #px, py = x, y
                #x += step

    noLoop()

def keyPressed():
    if key == 's':
        saveFrame("cover.png")