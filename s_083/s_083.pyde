# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10, 10)
GOLDEN = color(218, 145, 32, 10)
GREEN = color(49, 114, 59, 27)
BLACK_SUN = color(27, 27, 27, 53)
GREY_SUN = color(228, 228, 228, 10)



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


n_sides = 3
main_radius = 300

def setup():
    size(800, 800)
    noStroke()
    background(BLACK)
    #background(RED)
    #background(WHITE)

n = 0  # noise counter

def draw():
    global main_radius, n
    translate(width / 2, height / 2)

    n += 0.07
    main_radius = map(noise(n), 0, 1, -50, 410)
    for i, angle in enumerate(range(0, 360, 10)):
        angle += frameCount
        if i % 2:
            fill(BLACK_SUN)
        else:
            fill(GREY_SUN)

        angle = radians(angle)
        x = cos(angle) * main_radius
        y = sin(angle) * main_radius
        with pushMatrix():
            translate(x, y)
            points = regular_polygon(0, 0, 10, 4)

            beginShape()
            for p in points:
                vertex(p.x, p.y)
            endShape(CLOSE)

    print frameCount



def keyPressed():
    global n_sides
    if key.isdigit():
        n_sides = int(key)
    elif key == 's':
        saveFrame("#############.png")
