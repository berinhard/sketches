# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

TOTAL_FRAMES = 100.0

def get_percent(total_frames, counter=None):
    counter = counter or frameCount
    return counter % total_frames / total_frames

BLACK = color(27, 27, 27)
PURPLE = color(235, 0, 235)
GOLD = color(235, 235, 0, 170)
CYAN = color(71, 235, 235)
WHITE = color(242, 242, 242)
RED = color(182, 127, 12, 139)


def setup():
    size(500, 500)
    background(CYAN)
    fill(BLACK)
    stroke(GOLD)
    strokeWeight(4)


def draw():
    percent = get_percent(TOTAL_FRAMES)

    positions = [
        (0, height / 2),
        (width, height / 2),
    ]

    for x, y in positions:
        angle = TWO_PI * percent
        coord = polar_coordinate(x, y, 250, angle)
        ellipse(coord.x, coord.y, 50, 50)


    positions = [
        (0, height),
        (width, 0),
        (width, height),
        (0, 0),
    ]

    for x, y in positions:
        angle = TWO_PI * percent
        coord = polar_coordinate(x, y, 250, -angle)
        ellipse(coord.x, coord.y, 75, 75)

    if frameCount > TOTAL_FRAMES * 2:
        noLoop()

    saveFrame("#####.png")
