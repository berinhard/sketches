# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

BLACK = color(27, 27, 27)
WHITE = color(242, 242, 242)

TOTAL_FRAMES = 150.0

def get_percent(total_frames, counter=None):
    counter = counter or frameCount
    return counter % total_frames / total_frames


def setup():
    size(500, 500)


C1 = color(221, 39, 15)
C2 = color(14, 175, 38)
C3 = color(244, 139, 2)

def draw():
    background(WHITE)
    strokeWeight(12)
    stroke(BLACK)


    easing_func = easings.easeInOutCirc
    percent = easing_func(get_percent(TOTAL_FRAMES))
    percent_2 = easings.easeInOutSine(get_percent(TOTAL_FRAMES))
    angle = TWO_PI * percent

    w, h = 200, 100
    x, y =  150, 50
    points = [
        PVector(x + sin(angle) * h, y),
        PVector(x + w + sin(angle) * h, y),
        PVector(x + w - cos(angle) * h, y + h),
        PVector(x + -cos(angle) * h, y + h),
    ]

    ### first shape
    fill(C1)
    draw_shape(points, end_shape_mode=CLOSE)

    fill(C2)
    for p in points:
        ellipse(p.x, p.y, 30, 30)


    x, y =  150, 200
    angle_ = TWO_PI * percent_2
    points = [
        PVector(x + -sin(angle_) * h, y),
        PVector(x + w - sin(angle_) * h, y),
        PVector(x + w + cos(angle_) * h, y + h),
        PVector(x + cos(angle_) * h, y + h),
    ]

    ### second shape
    fill(C3)
    draw_shape(points, end_shape_mode=CLOSE)

    fill(C1)
    for p in points:
        ellipse(p.x, p.y, 30, 30)

    x, y =  150, 350
    points = [
        PVector(x + sin(angle) * h, y),
        PVector(x + w + sin(angle) * h, y),
        PVector(x + w - cos(angle) * h, y + h),
        PVector(x + -cos(angle) * h, y + h),
    ]

    ### third shape
    fill(C1)
    draw_shape(points, end_shape_mode=CLOSE)

    fill(C2)

    for p in points:
        ellipse(p.x, p.y, 30, 30)

    saveFrame("#####.png")

    if frameCount == TOTAL_FRAMES:
        noLoop()