import py5

from shapes import MovingShape

SIZE = 900


def new_shape():
    global shape, POINTS
    py5.background(15)
    POINTS = [
        py5.Py5Vector(py5.random(py5.width), py5.random(py5.height)),
        py5.Py5Vector(py5.random(py5.width), py5.random(py5.height)),
        py5.Py5Vector(py5.random(py5.width), py5.random(py5.height)),
        py5.Py5Vector(py5.random(py5.width), py5.random(py5.height)),
        py5.Py5Vector(py5.random(py5.width), py5.random(py5.height)),
    ]
    shape = MovingShape(*POINTS)


def setup():
    py5.size(SIZE, SIZE, py5.P2D)
    new_shape()


def draw():
    global shape
    shape.move()
    shape.draw()

    if py5.is_key_pressed:
        if py5.key in ['s', 'S']:
            py5.save_frame("cover.png")
        elif py5.key in ['n', "N"]:
            new_shape()

py5.run_sketch()
