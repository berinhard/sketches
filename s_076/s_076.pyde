# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)
GOLDEN = color(218, 185, 32, 140)
GREEN = color(32, 181, 10)

def setup():
    size(400, 900)
    background(WHITE)
    strokeWeight(2)
    frameRate(1)
    noFill()

def subdivide_line(p1, p2, num_divisions):
    points = [p1]

    if num_divisions > 1:
        step = 1.0 / num_divisions
        current_section = step
        points = [p1]
        while current_section < 1.0:
            points.append((
                lerp(p1[0], p2[0], current_section),  # x
                lerp(p1[1], p2[1], current_section),  # y
            ))
            current_section += step

    points.append(p2)
    return points

def draw():
    background(WHITE)

    single_line_size = 30
    y_range = range(100, height - 100, single_line_size)

    for i, x in enumerate(range(25, width - 25, single_line_size)):
        x += int(single_line_size / 2)
        for j, y in enumerate(y_range):
            current_x = x
            power = (len(y_range) - j)
            random_v = random(1) ** power
            angle = int(map(random_v, 0, 1, 0, 360))

            y_offset = 0
            if angle:
                stroke(RED)
                pow_scale = 0.5
                current_x = int(current_x + map(random(1), 0, 1, -1 * (j ** pow_scale), j ** pow_scale))
                min_y, max_y = -1 * (j ** pow_scale), j ** pow_scale
                y_offset = map(random(1), 0, 1, min_y, max_y)
                y += y_offset
            else:
                stroke(BLACK)

            with pushMatrix():
                translate(current_x, y)
                half_line = single_line_size / 2
                p1, p2 = (-half_line + 2.5, 0), (half_line - 2.5, 0)
                points = subdivide_line(p1, p2, j / 2)

                beginShape()
                vertex(*points[0])
                y_offset *= choice([1, -1])
                for xy in points[1:-1]:
                    xy = list(xy)
                    xy[1] += y_offset
                    vertex(*xy)
                    y_offset *= -1
                vertex(*points[-1])
                endShape()


def keyPressed():
    if key == 's':
        saveFrame("#######.png")
