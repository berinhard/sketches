# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(245, 245, 245)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10, 140)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)


points = []
to_be_processed = []


COLORS = None
def get_color_palette():
    global COLORS

    if not COLORS:
        with open("data/1000.json") as fd:
            colors = json.load(fd)
            COLORS = choice(colors)

    return COLORS


def populate_points():
    global points, to_be_processed, COLORS

    points = []
    while len(points) < 100:
        print(len(points))
        p = PVector(random(width), random(height))
        if not points:
            points.append(p)
        else:
            dists = [PVector.dist(p, o) for o in points if p != o]
            if min(dists) > 40:
                points.append(p)

    to_be_processed = points[:]
    COLORS = None


def setup():
    size(900, 900)
    background(BLACK)
    populate_points()


def draw():
    global main_triangle, to_be_processed, points

    for p in points:
        point(p.x, p.y)

    if to_be_processed:
        current_point = to_be_processed.pop(0)
        vectors_by_dist = sorted([(PVector.dist(current_point, o), o) for o in points if current_point != o], key=lambda x: x[0])
        close_1, close_2 = vectors_by_dist[:2]
        p1, p2 = close_1[1], close_2[1]

        p = current_point
        c = choice(get_color_palette())
        if not c:
            noFill()
        else:
            fill(c)
        beginShape()
        vertex(p.x, p.y)
        vertex(p1.x, p1.y)
        vertex(p2.x, p2.y)
        endShape(CLOSE)
    elif not frameCount % 10:
        saveFrame("############.png")
        populate_points()
        background(BLACK)


