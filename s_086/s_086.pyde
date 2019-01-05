# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from berin.save_frames import save_video_frames

WHITE = color(235)
RED = color(181, 32, 10)
BLACK = color(27, 27, 27)


def setup():
    global positions
    size(800, 800)
    strokeWeight(6)
    line_space = 10
    #frameRate(25)
    positions = range(-200, width / 2 + 200, line_space)


def draw():
    global positions

    background(WHITE)
    for i, x in enumerate(positions):
        noise_scale = 74.0
        n = noise((frameCount + i) / noise_scale)
        #print("Noise: {}".format(n))
        x_offset = map(n, 0, 1, -width, width)
        x += x_offset

        y = x
        if x > width / 2:
            y = height - y

        stroke(RED)
        line(x, y, 0, y)
        line(x, height - y, width, height - y)

        stroke(BLACK)
        line(x, 0, x, y)
        line(x, height, x, height - y)

    #noLoop()
    save_video_frames(25, 60)
