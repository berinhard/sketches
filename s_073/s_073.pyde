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

def draw():
    background(WHITE)

    single_line_size = 30
    y_range = range(100, height - 100, single_line_size)

    for i, x in enumerate(range(25, width - 25, single_line_size)):
        x += int(single_line_size / 2)
        for j, y in enumerate(y_range):
            current_x = x
            power = (len(y_range) - j) ** 1.2
            random_v = random(1) ** power
            angle = int(map(random_v, 0, 1, 0, 360))

            if angle:
                stroke(RED)
                current_x = int(current_x + map(random(1), 0, 1, -1 * (j ** 0.8), j ** 0.8))
                y = int(y + map(random(1), 0, 1, -1 * (j ** 0.8), j ** 0.8))
            else:
                stroke(BLACK)

            with pushMatrix():
                translate(current_x, y)
                if angle:
                    rotate(radians(angle))
                line(-single_line_size / 2 + 2.5, 0, (single_line_size) / 2 - 2.5, 0)
                line(-single_line_size / 2 + 2.5, -4, (single_line_size) / 2 - 2.5, -4)
                line(-single_line_size / 2 + 2.5, 4, (single_line_size) / 2 - 2.5, 4)


def keyPressed():
    if key == 's':
        saveFrame("#######.png")
