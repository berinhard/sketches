# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from pattern_1 import Pattern1
from pattern_2 import Pattern2

from random import choice

patterns = {
    '1': Pattern1(),
    '2': Pattern2(),
}

active_pattern = choice(patterns.values())

def setup():
    fullScreen()
    active_pattern.prepare()


def draw():
    active_pattern.draw_loop()


def keyPressed():
    global active_pattern
    pattern = patterns.get(key)
    if pattern:
        active_pattern = pattern
        active_pattern.prepare()
