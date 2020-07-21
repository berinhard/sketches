# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from pattern_2 import Pattern2

from random import choice

patterns = {
    '2': Pattern2(),
}

active_pattern = patterns['2']

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
