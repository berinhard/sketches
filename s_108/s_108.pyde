# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.save_frames import save_video_frames

WHITE = color(230, 230, 230)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)


def setup():
    size(870, 800)
    background(BLACK)
    strokeWeight(3)
    noFill()
    #frameRate(48)

def draw():
    background(BLACK)
    angle = 0
    inc = TWO_PI / 25.0
    y0 = height / 2

    step = 10
    for i, x in enumerate(sorted(range(-step, width + step, step), reverse=True)):
        y_diff = sin(angle) * map(noise((i + frameCount) / 83.0), 0, 1, 20, 400)

        y = y0 + y_diff
        stroke(RED)
        line(x, y0, x, y)

        y = y0 - y_diff
        stroke(WHITE)
        line(x, y0, x, y)

        angle += inc

    #save_video_frames(48, 60)

