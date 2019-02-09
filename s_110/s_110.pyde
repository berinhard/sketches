# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice

steps = range(5, 101, 5)

WHITE = color(230, 230, 230, 15)
BLACK = color(27, 27, 27)
RED = color(212, 32, 10, 30)

def setup():
    size(800, 800)
    background(BLACK)

def draw():
    px, py = -10, -10
    x, y = px, py

    current = choice(['x', 'y'])
    color = choice([RED, WHITE])
    stroke(color)
    while y < height:
        if current == 'x':
            x = px + choice(steps)
            y = py
            current = 'y'
        else:
            x = px
            y = py + choice(steps)
            current = 'x'

        line(px, py, x, y)
        px, py = x, y

    print(frameCount)
    if frameCount > 1000:
        saveFrame("######.png")
        noLoop()