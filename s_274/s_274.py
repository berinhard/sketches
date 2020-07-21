# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from pattern_3 import Pattern3

from random import choice

patterns = {
    '3': Pattern3(),
}

active_pattern = patterns['3']

def setup():
    fullScreen()
    active_pattern.prepare()


def draw():
    global active_pattern
    active_pattern.draw_loop()

def keyPressed():
    global active_pattern
    pattern = patterns.get(key)
    if pattern:
        active_pattern = pattern
        active_pattern.prepare()
    elif key == 's':
        saveFrame("cover.png")
