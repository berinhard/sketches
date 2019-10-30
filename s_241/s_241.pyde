# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import choice


def setup():
    size(700, 700)
    rectMode(CENTER)
    background(242)

raio_x = 300
raio_y = 300

def draw():
    #noStroke()
    #fill(242, 242, 242, 20)
    #rect(width / 2, height / 2, 700, 700)
    global raio_x, raio_y

    with pushMatrix():
        translate(width/2, height/2)
        rotate(radians(frameCount))

        limite = 900 - (frameCount / 100) * 40
        raio_x = map(
            noise(frameCount * 0.01),
            0, 1,
            0, limite
        )
        raio_y = map(
            noise((frameCount + 14913279) * 0.008),
            0, 1,
            0, limite
        )

        print(frameCount, limite)
        strokeWeight(2)
        noFill()
        stroke(27, 27, 27, 10)
        ellipse(0, 0, raio_x, raio_y)

        if limite <= 0:
            saveFrame("cover.png")
            noLoop()