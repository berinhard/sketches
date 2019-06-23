# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import choice


def setup():
    size(900, 900)
    rectMode(CENTER)
    noFill()
    strokeWeight(6)
    stroke(238)
    frameRate(1)

background_colors = [
    color(96),
    color(214, 20, 92),
    color(20, 214, 92),
    color(92, 20, 214),
    color(214, 184, 40),
]

def draw():
    background(choice(background_colors))

    square_size = 100
    for x in range(0, width + square_size, square_size):
        for y in range(0, height + square_size, square_size):
            ranges = [0.2 * i for i in range(5)]
            i = choice(ranges)
            if not i:
                ellipse(x, y, square_size, square_size)
            rect(x + lerp(0, square_size, i), y + lerp(0, square_size, i), square_size, square_size)
