# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import choice


def setup():
    size(700, 700)
    rectMode(CENTER)
    background(27)
    colorMode(HSB)


x, y = 0, 350
tamanho = 100

def draw():
    x = map(
        noise(frameCount * 0.0042),
        0, 1,
        0, width
    )
    y = map(
        noise((frameCount + 14122) * 0.008),
        0, 1,
        0, height
    )

    with pushMatrix():
        translate(x, y)
        angle = radians(frameCount) % TWO_PI
        rotate(angle)
        print(angle)

        tamanho = map(
            cos(angle),
            -1, 1,
            0, 200
        )

        strokeWeight(2)
        stroke(random(0, 255), 255, 255, 10)
        line(-tamanho, 0, tamanho, 0)

        # if limite <= 0:
        #     saveFrame("cover23333.png")
        #     noLoop()


def keyPressed():
    if key == 's':
        saveFrame("cover.png")