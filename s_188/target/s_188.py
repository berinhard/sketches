from pytop5js import *


def setup():
    createCanvas(window.innerWidth, window.innerHeight)
    background(242)


def draw():
    stroke(27, 27, 27, 2)
    noFill()

    row_size = 50
    for x in range(0, width + row_size, row_size):
        for y in range(0, height + row_size, row_size):
            r = random(1) * row_size
            ellipse(x, y, r, r)


# ==== This is required by pyp5js to work

# Register your events functions here
event_functions = {
    # "keyPressed": keyPressed,    as an example
}
start_p5(setup, draw, event_functions)
