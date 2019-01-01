# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)


def regular_polygon(x, y, radius, n_sides, angle_rotation=0):
    section_angle = TWO_PI / n_sides
    angles = [section_angle * i for i in range(n_sides)]

    points = []
    for angle in angles:
        p = PVector(
            x + cos(angle + angle_rotation) * radius,
            y + sin(angle + angle_rotation) * radius,
        )
        points.append(p)

    return points


def draw_recursive_polygons(x, y, radius, n_sides=None, step=0, angle_rotation=0):
    if radius <= 10:
        return

    n_sides = n_sides or int(random(4, 7))
    points = regular_polygon(x, y, radius, n_sides, angle_rotation)

    noFill()
    beginShape()
    for p in points:
        vertex(p.x, p.y)
    endShape(CLOSE)

    angle_rotation = radians(random(-45, 45))
    for p in points:
        draw_recursive_polygons(p.x, p.y, radius / 2, n_sides, step, angle_rotation)


n_sides = 3

def setup():
    size(800, 800)
    stroke(BLACK)
    frameRate(1)


def draw():
    background(WHITE)
    draw_recursive_polygons(width / 2, height / 2, 180, n_sides)


def keyPressed():
    global n_sides
    if key.isdigit():
        n_sides = int(key)
    elif key == 's':
        saveFrame("{}.png".format(n_sides))
