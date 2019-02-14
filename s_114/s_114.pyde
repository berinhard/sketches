# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice


colors_1 = [
    color(8,61,95),
    color(0,166,182),
    color(55,189,182),
    color(156,205,175),
    color(190,210,173),
]
colors_2 = [
    color(15,154,250),
    color(254,200,4),
    color(242,99,34),
    color(122,45,89),
    color(24,27,70),
]
colors_3 = [
    color(74,133,184),
    color(228,238,242),
    color(121,184,74),
    color(154,189,229),
    color(236,207,70),
]

def setup():
    #size(900, 900)
    size(2560, 1080)
    noStroke()
    rectMode(CENTER)
    background(0)

def draw():
    square_sizes = range(50, 300, 25)
    square_positions_x = range(0, width, 25)
    square_positions_y = range(0, height, 25)
    angle_start = 0
    angles = [
        angle_start,
        angle_start + QUARTER_PI,
    ]

    x = choice(square_positions_x)
    y = choice(square_positions_y)

    with pushMatrix():
        d = choice(square_sizes)
        angle = choice(angles)
        translate(x, y)
        rotate(angle)
        fill(0, 0, 0, 30)

        if angle == angle_start:
            rect(10, 10, d, d)
        else:
            rect(10, 0, d, d)

        fill(choice(colors_3))
        rect(0, 0, d, d)

def keyPressed():
    if key == 's':
        saveFrame("######.png")
    if key == 'n':
        noLoop()