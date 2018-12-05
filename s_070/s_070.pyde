# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27, 10)
RED = color(181, 32, 10, 20)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)


def deform(points, depth, variance, variance_reduce):
    deformed_points = []

    for i, current_point in enumerate(points):
        previous_point = points[i - 1]
        deformed_points.append(previous_point)
        deformed_points.extend(
            subdivide_line(previous_point, current_point, depth, variance / 10.0, variance_reduce)
        )


    deformed_points.append(current_point)
    return deformed_points


def subdivide_line(p1, p2, depth, variance, variance_reduce):
    if not depth:
        return []

    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2

    #new_x = map(noise((p1.x + p2.x + frameCount) / 130.0), 0, 1, -2.5, 2.5)
    #new_y = map(noise((p1.y + p2.y + frameCount) / 97.0), 0, 1, -2.5, 2.5)
    new_x = map(random(1), 0, 1, -2.5, 2.5)
    new_y = map(random(1), 0, 1, -2.5, 2.5)

    new_x = mid_x + new_x * variance
    new_y = mid_y + new_y * variance
    new_p = PVector(new_x, new_y)

    new_depth = depth - 1
    new_variance = variance / variance_reduce
    points = subdivide_line(p1, new_p, new_depth, new_variance, variance_reduce)
    points.append(new_p)
    points.extend(subdivide_line(new_p, p2, new_depth, new_variance, variance_reduce))

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
    strokeWeight(2)
    noFill()

def draw():
    for i, x in enumerate(cols):
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

            deformed_points = deform([p1, p2], 5, 100.0 / (0.1 * (i + 1)) , 2)

            stroke(BLACK)
            if i == len(cols) - red_index:
                stroke(RED)

            beginShape()
            for p in deformed_points:
                vertex(p.x, p.y)
            endShape()


def keyPressed():
    if key == 's':
        saveFrame("#######.png")