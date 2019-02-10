# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

WHITE = color(230, 230, 230, 120)
BLACK = color(27, 27, 27)
RED = color(21, 153, 210, 120)


def setup():
    size(900, 900)
    background(BLACK)
    stroke(RED)
    strokeWeight(1)
    noFill()


def draw():
    background(BLACK)

    angles = []
    angle = 0
    while angle <= TWO_PI:
        angles.append(angle)
        angle += TWO_PI / 360
    x0, y0 = width / 2, height / 2

    radius_by_pos = []
    n = random(100000)
    c1, c2 = random(100000), random(100000)
    for i in range(len(angles) / 2):
        radius = map(noise(n), 0, 1, 100, 450)
        w = map(noise(c1), 0, 1, 50, 200)
        h = map(noise(c2), 0, 1, 50, 200)
        radius_by_pos.append((radius, w, h))
        n += 0.03
        c1 += 0.011
        c2 += 0.0087

    print(len(angles))
    print(len(radius_by_pos))
    for i, angle in enumerate(angles[:-1]):
        index = i
        lerp_i = map(i, 0, len(angles) / 2 - 1, 0, 1)
        stroke(lerpColor(WHITE, RED, lerp_i))

        if i >= len(radius_by_pos):
            index = len(radius_by_pos) - i - 1
            lerp_i = map(i - len(radius_by_pos), 0, len(angles) / 2 - 1, 0, 1)
            stroke(lerpColor(RED, WHITE, lerp_i))

        radius, c1, c2 = radius_by_pos[index]
        x = x0 + radius * cos(angle)
        y = y0 + radius * sin(angle)

        ellipse(x, y, c1, c2)

    saveFrame("cover.png")
    noLoop()


count = 0
def keyPressed():
    global count

    if key == 'n':
        count += 1
        saveFrame("{}.png".format(count))
        redraw()
    elif key == 'b':
        background(BLACK)