# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
add_library('svg')

from pattern_1 import Pattern1

from random import choice

active_pattern = Pattern1()

def setup():
    size(1400, 1400)
    background(242)
    translate(250, 250)
    active_pattern.prepare(900, 900)

def draw():
    with pushMatrix():
        translate(250, 250)
        active_pattern.draw_loop()

    noLoop()


def keyPressed():
    if key == 's':
        saveFrame("seed_{}.png".format(active_pattern.SEED))
