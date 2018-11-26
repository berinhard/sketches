# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames


WHITE = color(235, 235, 235, 130)
BLACK = color(27, 27, 27)


def random_polygon(x, y, radius, n_sides):
    section_angle = TWO_PI / n_sides
    angles = [map(random(1), 0, 1, 0, TWO_PI) for i in range(n_sides)]

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


    deformed_points.append(current_point)
    return deformed_points


def subdivide_line(p1, p2, depth, variance, variance_reduce):
    if not depth:
        return []

    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2

    new_x = map(noise((p1.x + p2.x + frameCount) / 130.0), 0, 1, -2.5, 2.5)
    new_y = map(noise((p1.y + p2.y + frameCount) / 97.0), 0, 1, -2.5, 2.5)

    new_x = mid_x + new_x * variance
    new_y = mid_y + new_y * variance
    new_p = PVector(new_x, new_y)

    new_depth = depth - 1
    new_variance = variance / variance_reduce
    points = subdivide_line(p1, new_p, new_depth, new_variance, variance_reduce)
    points.append(new_p)
    points.extend(subdivide_line(new_p, p2, new_depth, new_variance, variance_reduce))

    return points


def new_polygon(n_sides=4):
    global extra_variance, regular_points, live_deformations
    variance_noise = noise(frameCount)
    extra_variance = map(variance_noise, 0, 1, -1000, 2000)
    regular_points = random_polygon(width / 2, height / 2, 350, n_sides)
    live_deformations = []


def setup():
    size(900, 900)
    strokeWeight(2)
    noStroke()
    new_polygon()
    #frameRate(24)



def draw():
    global extra_variance, live_deformations

    background(BLACK)
    noFill()
    stroke(WHITE)


    if len(live_deformations) == 40:
        live_deformations.pop(0)
    live_deformations.append(deform(regular_points, 3, 300 + extra_variance, 2))


    for points in live_deformations:
        beginShape()
        for p in points:
            vertex(p.x, p.y)

        endShape()

    variance_noise = noise(frameCount / 79.0)
    extra_variance = map(variance_noise, 0, 1, -1000, 2000)

    if not frameCount % 720:
        refresh_polygon()

    save_video_frames(24, 10 * 60)


def refresh_polygon():
    noiseSeed(choice(range(0, 1000000)))
    n_sides = choice(range(3, 8))
    new_polygon(n_sides)
    redraw()


def keyPressed():
    global extra_variance, regular_points

    if key == 'n':
        refresh_polygon()