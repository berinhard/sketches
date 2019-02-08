# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

WHITE = color(230, 230, 230, 90)
BLACK = color(27, 27, 27)
RED = color(212, 32, 10, 90)


def setup():
    size(800, 800)
    background(BLACK)
    stroke(RED)
    strokeWeight(1)
    noFill()

def draw():
    angles = []
    angle = 0
    while angle <= TWO_PI:
        angles.append(angle)
        angle += TWO_PI / 360
    x0, y0 = width / 2, height / 2

    radius_by_pos = []
    n = 0
    for i in range(len(angles) / 2):
        radius = map(noise(n), 0, 1, 100, 350)
        radius_by_pos.append(radius)
        n += 0.024

    print(len(angles))
    print(len(radius_by_pos))
    for i, angle in enumerate(angles[:-1]):
        index = i
        stroke(RED)
        if i >= len(radius_by_pos):
            stroke(WHITE)
            index = len(radius_by_pos) - i - 1

        radius = radius_by_pos[index]
        x = x0 + radius * cos(angle)
        y = y0 + radius * sin(angle)

        ellipse(x, y, 100, 100)

    saveFrame("cover.png")
    noLoop()