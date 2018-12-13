# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)


def subdivide_line(p1, p2, depth):
    if not depth:
        return []

    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2

    new_p = PVector(mid_x, mid_y)

    new_depth = depth - 1
    points = subdivide_line(p1, new_p, new_depth)
    points.append(new_p)
    points.extend(subdivide_line(new_p, p2, new_depth))

    return points


def initial_state():
    global cols, red_index

    space = 15
    cols = range(0, width, space)
    red_index = int(random(len(cols)))


def setup():
    size(900, 900)
    background(WHITE)
    stroke(BLACK)
    initial_state()
    strokeWeight(1)
    noFill()

def draw():
    for i, x in enumerate(cols):
        strokeWeight(2)
        with pushMatrix():
            translate(x, 0)

            p1 = PVector(0, 0)
            p2 = PVector(0, x)

            stroke(BLACK)
            if i == red_index:
                stroke(RED)
            line(p1.x, p1.y, p2.x, p2.y)

        with pushMatrix():
            translate(x, x)

            p1 = PVector(0, 0)
            p2 = PVector(0, height - x)

            internal_points = [p1] + subdivide_line(p1, p2, 5) + [p2]

            stroke(BLACK)
            if i == len(cols) - red_index:
                stroke(RED)

            for i, p in enumerate(internal_points[1:]):
                previous_p = internal_points[i]
                strokeWeight(random(10))
                line(previous_p.x, previous_p.y, p.x, p.y)

    noLoop()

def keyPressed():
    if key == 's':
        saveFrame("#######.png")