# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(245, 245, 245)
BLACK = color(27, 27, 27, 20)
RED = color(181, 32, 10, 82)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)


def setup():
    size(900, 900)
    background(WHITE)
    stroke(BLACK)

def draw():
    space = 15
    cols = range(0, width, space)
    red_index = int(random(len(cols)))

    for i, x in enumerate(cols):
        p1 = PVector(x, 0)
        p2 = PVector(x, x)

        angle_rate = i * 2
        angle = map(random(1), 0, 1, -1 * angle_rate, angle_rate)
        with pushMatrix():
            rotate(radians(angle))

            stroke(BLACK)
            if i == red_index:
                stroke(RED)
            line(p1.x, p1.y, p2.x, p2.y)


def keyPressed():
    if key == 's':
        saveFrame("#######.png")