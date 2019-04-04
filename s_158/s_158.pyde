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

TOTAL_FRAMES = 100.0

def get_percent(total_frames, counter=None):
    counter = counter or frameCount
    return counter % total_frames / total_frames

def setup():
    size(600, 400)
    stroke(BLACK)
    strokeWeight(5)


max_dist, min_dist = -10000000000000, 1000000000000000000

def draw():
    global max_dist, min_dist

    background(WHITE)

    fill(BLACK)
    percent = easings.easeInOutSine((get_percent(TOTAL_FRAMES)))

    counter = frameCount % (TOTAL_FRAMES * 2)
    if counter < TOTAL_FRAMES:
        x = width * percent
    else:
        x = width - width * percent

    y = 200
    noStroke()
    fill(13, 162, 226)
    ellipse(x, y, 100, 100)

    circle_x = x
    x_range = range(0, width + 10, 10)
    noFill()

    for i, x in enumerate(x_range):
        diff = circle_x - x
        h = map(abs(diff), 0, 600, 150, 30)
        a = map(abs(diff), 0, 600, 30, 200)
        #stroke(27, 27, 27, a)

        c = lerpColor(BLACK, color(13, 162, 226), map(abs(diff), 0, 600, 0, 1))
        stroke(c)

        if diff > max_dist:
            max_dist = diff
        elif diff < min_dist:
            min_dist = diff
        ellipse(x, y, 30, h)

    print(min_dist, max_dist)

    if frameCount == TOTAL_FRAMES * 2 :
        noLoop()

    saveFrame("#####.png")