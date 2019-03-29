# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# 2ª Noite de Processing - Recife
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

BLACK = color(27, 27, 27)
PURPLE = color(235, 0, 235, 1)
GOLD = color(235, 235, 0, 1)
CYAN = color(0, 235, 235, 40)
WHITE = color(242, 242, 242, 1)
RED = color(242, 127, 12, 40)

BACK_RED = color(121, 32, 45)
BACK_BLUE = color(35, 32, 121)
BACK_GREEN = color(19, 114, 77)

COLOR_1 = CYAN
COLOR_2 = RED


TOTAL_FRAMES = 100.0


def setup():
    size(400, 400)
    rectMode(CENTER)
    noFill()
    background(255)
    frameRate(15)


POINTS = []
def draw():
    background(BLACK)
    x, y = width / 2, height / 2

    percent = (frameCount % TOTAL_FRAMES) / TOTAL_FRAMES
    percent = easings.easeInOutSine(percent)
    angle = TWO_PI * percent #* 0.1

    base_size = 380
    if percent < 0.5:
        size = base_size * percent
    else:
        size = base_size * (1 - percent)

    line_color = lerpColor(COLOR_1, COLOR_2, percent)
    if percent > 0.5:
        weight = 6 - 5 * percent
    else:
        weight = 6 - 5 * (1 - percent)

    translate(x, y)
    points = regular_polygon(0, 0, size, 6, end_shape_mode=CLOSE, draw=False)

    if percent <= 0.5:
        data = [points, weight, line_color, angle]
        POINTS.append(data)
    else:
        p = len(POINTS)
        POINTS.pop(p - 1)

    print(len(POINTS))

    for points, w, l, a in POINTS:
        rotate(angle)
        strokeWeight(w)
        stroke(l)
        draw_shape(points, end_shape_mode=CLOSE)

    #if frameCount > TOTAL_FRAMES:
    #    noLoop()
    #saveFrame("####.png")