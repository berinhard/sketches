# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27, 12)
RED = color(181, 32, 10, 6)

radius = 700


def setup():
    size(700, 700)
    rectMode(CENTER)
    background(WHITE)
    stroke(BLACK)
    strokeWeight(3)
    noFill()

def draw():
    t_x, t_y = frameCount * 0.7, (901332 + frameCount) * 0.8
    rate_x, rate_y = noise(t_x), noise(t_y)
    r_x = radius * rate_x
    r_y = radius * rate_y

    with draw_at_center():
        rotate(radians(frameCount))
        stroke(RED)
        rect(0, 0, r_x, r_y)
        stroke(BLACK)
        ellipse(0, 0, r_x, r_y)


    print frameCount

def keyPressed():
    if key == 's':
        saveFrame('##########.png')