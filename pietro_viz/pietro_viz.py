# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from pattern_1 import Pattern1

pattern_1 = Pattern1()

def setup():
    fullScreen()
    pattern_1.prepare()


def draw():
    pattern_1.draw_loop()
