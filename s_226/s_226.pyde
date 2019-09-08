# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/


def setup():
    size(900, 900)
    background(242)
    strokeWeight(4)


def polar_coordinate(x0, y0, r, angle):
    x = x0 + r * cos(angle)
    y = y0 + r * sin(angle)

    return x, y


def draw():
    x, y = width / 2, height / 2
    r = 300
    num_points = 30

    stroke(211, 23, 38, 47)
    for i in range(1, num_points):
        angle = TWO_PI / i
        px, py = polar_coordinate(x, y, r, angle)

        line(px, py, x, y)

    stroke(42, 42, 42, 47)
    for i in range(num_points + 1):
        angle = (i * PI / num_points) + PI
        px, py = polar_coordinate(x, y, r, angle)

        line(px, py, x, y)

    if frameCount == 10:
        saveFrame("cover.png")
        noLoop()