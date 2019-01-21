# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import regular_polygon
from berin.save_frames import save_video_frames
from random import choice


WHITE = color(228, 228, 228)
BLACK = color(17, 17, 17)


def setup():
    size(900, 900)
    strokeWeight(1.5)
    stroke(BLACK)
    noFill()
    background(WHITE)
    frameRate(2)

def draw():
    radius = 20#int(random(20, 300))
    x_positions = range(0, width + 100, 100)
    y_positions = range(0, height + 100, 100)

    #background(WHITE)
    for x in x_positions:
        for y in y_positions:
            radius = 50

            r, g, b = 17, 17, 17
            angle = choice([QUARTER_PI, HALF_PI, QUARTER_PI * 3, PI])

            if random(1) > 0.8:
                continue
            while radius > 10:
                strokeWeight(map(radius, 10, 50, 0.5, 2))
                stroke(color(r, g, b, map(radius, 10, 50, 5, 100)))
                regular_polygon(x, y, radius, 4, angle_rotation=angle)
                radius -= 5

    if not frameCount % 5:
        saveFrame("#######.png")
        background(WHITE)

    print(frameCount)