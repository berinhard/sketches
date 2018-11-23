# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
add_library('pdf')


WHITE = color(235, 235, 235)
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
    new_y = map(noise((p1.y + p2.y + frameCount) / 130.0), 0, 1, -2.5, 2.5)

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
    global extra_variance, regular_points

    size(900, 900)
    frameRate(2)
    strokeWeight(1)
    noStroke()
    extra_variance = -300
    background(WHITE)
    regular_points = random_polygon(width / 2, height / 2, 350, 4)
    
    beginRecord(PDF, "00000.pdf"); 



def draw():
    global extra_variance

    print(extra_variance)
    noFill()
    stroke(BLACK)

    if extra_variance == 1500:
        endRecord()

    points = deform(regular_points, 3, 300 + extra_variance, 2)

    beginShape()
    for p in points:
        vertex(p.x, p.y)

    endShape()

    extra_variance += 100


def keyPressed():
    global extra_variance, regular_points

    print(key)
    if key == 'a':
        extra_variance += 100
    elif key == 'z' and extra_variance > -300:
        extra_variance -= 100
    elif key == 'n':
        beginRecord(PDF, "############.pdf");
        noiseSeed(choice(range(0, 1000000)))
        background(WHITE)
        extra_variance = -300
        regular_points = random_polygon(width / 2, height / 2, 350, 4)
        redraw()
    elif key == 's':
        saveFrame("###########.png")

    print("new variance", extra_variance)
