# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames

WHITE = color(235, 235, 235)
RED = color(181, 32, 10, 87)
BLACK = color(27, 27, 27, 36)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)
COLORS = [GOLDEN, GREEN, BLACK]
COLORS_2 = [GOLDEN] * 80 + [WHITE] * 20


def regular_polygon(x, y, radius, n_sides):
    section_angle = TWO_PI / n_sides
    angles = [section_angle * i for i in range(n_sides)]

    points = []
    for angle in angles:
        p = PVector(
            x + cos(angle) * radius,
            y + sin(angle) * radius,
        )
        points.append(p)

    return points


def deform(points, depth, variance, variance_reduce):
    deformed_points = []

    for i, current_point in enumerate(points):
        previous_point = points[i - 1]
        deformed_points.append(previous_point)
        deformed_points.extend(
            subdivide_line(previous_point, current_point, depth, variance / 10.0, variance_reduce)
        )

    return deformed_points


def subdivide_line(p1, p2, depth, variance, variance_reduce):
    if not depth:
        return []

    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2

    new_x = map(noise((p1.x + p2.x + frameCount) / 100.0), 0, 1, -2.5, 2.5)
    new_y = map(noise((p1.y + p2.y + frameCount) / 100.0), 0, 1, -2.5, 2.5)

    new_x = mid_x + new_x * variance
    new_y = mid_y + new_y * variance
    new_p = PVector(new_x, new_y)

    new_depth = depth - 1
    new_variance = variance / variance_reduce
    points = subdivide_line(p1, new_p, new_depth, new_variance, variance_reduce)
    points.append(new_p)
    points.extend(subdivide_line(new_p, p2, new_depth, new_variance, variance_reduce))

    return points


def setup():
    global extra_variance

    size(900, 900)
    frameRate(10)
    strokeWeight(3)
    noStroke()
    extra_variance = 0
    background(WHITE)



def draw():
    noFill()
    stroke(BLACK)

    regular_points = regular_polygon(width / 2, height / 2, 375, 2)
    points = deform(regular_points, 5, 300 + extra_variance, 2)

    beginShape()
    for p in points:
        vertex(p.x, p.y)

    endShape()

    print(frameCount)


def keyPressed():
    global extra_variance

    print(key)
    if key == 'a':
        extra_variance += 100
    elif key == 'z' and extra_variance > -300:
        extra_variance -= 100
    elif key == 's':
        saveFrame("###########.png")
    print("new variance", extra_variance)