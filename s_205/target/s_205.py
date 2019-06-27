from pyp5js import *

def setup():
    pixelDensity(displayDensity())
    w, h = window.innerWidth, window.innerHeight
    createCanvas(w, h)
    frameRate(10)
    strokeWeight(2)


def draw():
    background(242)

    for i, y in enumerate(range(0, height, 25)):
        index = (frameCount + i) * 0.07
        max_x = map(noise(index), 0, 1, 0, width)

        stroke(27)
        for x in range(0, max_x, 10):
            line(x, y, x - 10, y + 20)

        fill(27)
        noStroke()
        beginShape()
        vertex(x + 10, y)
        vertex(width, y)
        vertex(width, y + 20)
        vertex(x, y + 20)
        endShape(CLOSE)

        stroke(242)
        for x in range(max_x, width + 10, 10):
            line(x - 10, y, x, y + 20)


def keyPressed():
    if key == 's':
        saveCanvas('out', 'png')
