from pytop5js import *


def setup():
    createCanvas(window.innerWidth, window.innerHeight)
    background(242)


def draw():
    noFill()


    row_size = 100
    x_pos = enumerate(range(0, width + row_size, row_size))
    y_pos = enumerate(range(0, height + row_size, row_size))

    for i, x in x_pos:
        for j, y in y_pos:
            stroke(27, 27, 27, 5)
            if frameCount == 1:
                rect(x, y, row_size, row_size)
            r = noise(i, j, frameCount * 0.004) * row_size
            ellipse(x, y, r, r)

    print(frameCount)


# ==== This is required by pyp5js to work

# Register your events functions here
event_functions = {
    # "keyPressed": keyPressed,    as an example
}
start_p5(setup, draw, event_functions)
