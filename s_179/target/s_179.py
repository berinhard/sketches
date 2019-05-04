from random import choice
from pyp5js import *


x = 0
def setup():
    createCanvas(900, 900)
    strokeWeight(2)
    stroke(color(27, 27, 27, 170))


def draw():
    global x

    colors = [
        color(230, 0, 230),
        color(0, 230, 230),
        color(230, 230, 0),
    ]

    for j, y in enumerate(range(0, 900, 30 + 1)):
        r = map(noise(x, j, frameCount * 0.008), 0, 1, 5, 60)
        fill(choice(colors))
        ellipse(x, y, r, r)

    x += random(1, 10)
    if x >= width:
        console.log("finished")
        #saveCanvas("cover", "png")
        noLoop()


# This is required by pyp5js to work
start_p5(setup, draw)
