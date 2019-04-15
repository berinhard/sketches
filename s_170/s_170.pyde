# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

p1, p2 = PVector(800, 100), PVector(100, 800)
cp_1, cp_2 = None, None

X1_START, Y1_START = 0, 123312
X2_START, Y2_START = 33192, 1203


def update_coords(step_x1, step_y1, step_x2, step_y2):
    global cp_1, cp_2

    off_range = [-650, 650]
    x1 = map(noise(X1_START + frameCount * step_x1), 0, 1, *off_range)
    y1 = map(noise(Y1_START + frameCount * step_y1), 0, 1, *off_range)
    cp_1 = p1 + PVector(x1, y1)

    x2 = map(noise(X2_START + frameCount * step_x2), 0, 1, *off_range)
    y2 = map(noise(Y2_START + frameCount * step_y2), 0, 1, *off_range)
    cp_2 = p2 + PVector(x2, y2)


def setup():
    noFill()
    size(900, 900)
    update_coords(0, 0, 0, 0)
    stroke(10, 193, 7, 5)
    strokeWeight(3)
    background(27)


def draw():
    bezier(
        p1.x,
        p1.y,
        cp_1.x,
        cp_1.y,
        cp_2.x,
        cp_2.y,
        p2.x,
        p2.y
    )
    update_coords(0.04, 0.024, 0.072, 0.055)

def keyPressed():
    if key == 's':
        saveFrame("######.png")