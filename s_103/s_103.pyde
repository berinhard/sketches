# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Reference: @the_golden_line https://www.instagram.com/p/BtY1Uc7g7F5/

from random import choice, shuffle


WHITE = color(228, 288, 288)
BLACK = color(27, 27, 27)
RED = color(218, 32, 10)
GOLDEN = color(218, 185, 32)
GREEN = color(32, 181, 10)



WHITE = color(228, 228, 228)
BLACK = color(27, 27, 27, 35)
RED = color(181, 32, 10, 70)


def setup():
    size(900, 900)
    background(WHITE)
    rectMode(CENTER)
    noFill()

def draw():
    translate(width / 2, height / 2)


    r = 300
    rate = 0.8
    angle_rate = rate
    square_r = r - rate * (frameCount - 1)
    angle_rotation = radians(frameCount * angle_rate)
    rotate(angle_rotation)
    square_d = square_r * sqrt(2)
    circle_r = square_d / 2

    if frameCount % 2:
        stroke(BLACK)
    elif abs(square_r) > 100:
        stroke(RED)
    else:
        stroke(choice([GOLDEN, GREEN]))

    with pushMatrix():
        rotate(QUARTER_PI)
        rect(0, 0, square_r, square_r)

    centers = [
        (0, -circle_r),
        (circle_r, 0),
        (-circle_r, 0),
        (0, circle_r),
    ]

    for x, y in centers:
        d = circle_r * 2
        ellipse(x, y, d, d)

    if abs(square_r) > 300:
        noLoop()
        saveFrame("########.png")