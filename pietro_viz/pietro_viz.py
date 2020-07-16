# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from pattern_1 import Pattern1
from pattern_2 import Pattern2
from pattern_3 import Pattern3
from pattern_4 import Pattern4

from random import choice

patterns = {
    '1': Pattern1(),
    '2': Pattern2(),
    '3': Pattern3(),
    '4': Pattern4(),
}

active_pattern = choice(patterns.values())
#active_pattern = patterns['4']

def setup():
    fullScreen()
    active_pattern.prepare()


def draw():
    global active_pattern
    active_pattern.draw_loop()
    if random(1) > 0.998:
        active_pattern = choice(patterns.values())
        active_pattern.prepare()


def keyPressed():
    global active_pattern
    pattern = patterns.get(key)
    if pattern:
        active_pattern = pattern
        active_pattern.prepare()
