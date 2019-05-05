from pytop5js import *


def setup():
    createCanvas(900, 900)
    background(240)
    strokeWeight(2)


def draw():
    stroke(27, 27, 27, 2)
    offset = 30
    for i in range(100):
        x = i * offset + offset / 2
        for j in range(100):
           y = j * offset + offset / 2
           line(x, y, x + offset, y + sin(frameCount) * offset)




# This is required by pyp5js to work
start_p5(setup, draw)
