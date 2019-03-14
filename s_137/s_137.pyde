# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches


rects_to_draw = []
WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)


def setup():
    size(900, 900)
    rects_to_draw.append((0, 0, 900, 900, 900, 900))
    fill(WHITE)
    stroke(BLACK)
    strokeWeight(2)
    frameRate(3)


def draw():
    next_rects = []

    if not rects_to_draw:
        saveFrame("#######.png")
        noLoop()

    while rects_to_draw:
        x, y, w, h, limit_x, limit_y = rects_to_draw.pop()
        if not (w >= 20 and h >=20):
            continue

        new_w, new_h = int(random(x + 3 * w / 4, w)), int(random(y + 3 * h / 4, h))
        new_x, new_y = 0, 0

        next_rects.append((new_x, new_y, new_w, new_h, x + w, y + h))

        v1, v2, v3, v4 = [
            PVector(new_x, new_y), # v1
            PVector(new_w, new_y), # v2
            PVector(new_x, new_h), # v3
            PVector(new_w, new_h), # v4
        ]

        index = random(0.1, 0.8)
        p = PVector.lerp(v2, v4, index)

        l_x, l_y = int(p.x), int(p.y)
        line(l_x, l_y, limit_x, l_y)

        index = random(0.1, 0.8)
        p = PVector.lerp(v3, v4, index)

        l_x, l_y = int(p.x), int(p.y)
        line(l_x, l_y, l_x, limit_y)

        rect(x, y, w, h)


    for x in next_rects:
        rects_to_draw.append(x)