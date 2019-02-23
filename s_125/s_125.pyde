# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from berin.palettes import get_color_palette


def setup():
    global COLORS

    size(900, 900)
    COLORS = get_color_palette()

    background(38)
    frameRate(10)


def draw():
    stroke(0)
    strokeWeight(2)

    fill(choice(COLORS))
    rate = width / 10
    positions = range(-rate, width +  rate, rate)
    pos = choice(positions)

    rate = 5
    sizes = range(10, 60 + rate, rate)
    size = choice(sizes)

    if random(1) > 0.5:
        # horizontal
        rect(0, pos, width, size)
    else:
        # vertical
        rect(pos, 0, size, height)


def keyPressed():
    if key == 's':
        saveFrame("#######.png")
    if key == 'n':
        global COLORS
        COLORS = get_color_palette()
        background(38)
        redraw()