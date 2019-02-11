# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from berin.shapes import IntersectionLine

WHITE = color(230, 230, 230)
BLACK = color(27, 27, 27)
RED = color(21, 153, 210)

INTERVAL = 10
def setup():
    size(900, 900)
    frameRate(10)
    strokeWeight(2)
    background(BLACK)

lines = []

def ordering(p1, p2):
    if p1.x < p2.x or p1.y < p2.y:
        return -1
    elif p1.x == p2.x and p1.y == p2.y:
        return 0
    return 1


def ordering_list_elem(el1, el2):
    return ordering(el1[0], el2[0])


def draw():
    global lines

    assert width == height
    x_range = range(0, width, INTERVAL)
    y_range = range(0, height, INTERVAL)

    if random(1) > 0.5:
        y = choice(y_range)
        p1 = PVector(choice(x_range), y)
        p2 = PVector(choice(x_range), y)
    else:
        x = choice(x_range)
        p1 = PVector(x, choice(y_range))
        p2 = PVector(x, choice(y_range))

    p1, p2 = sorted([p1, p2], cmp=ordering)
    new_line = IntersectionLine(p1, p2)


    intersections = []   # compute all intersection points with existing lines
    for c_line in lines:
        inter = new_line.get_intersection(c_line)
        if inter:
            intersections.append((inter, c_line))

    current_line = new_line
    if intersections:
        segments = []
        previous = p1
        previous_line = None
        for inter, inter_line in sorted(intersections, cmp=ordering_list_elem):  # split line into segments
            inter = PVector(inter.x, inter.y)

            segment = IntersectionLine(previous, inter)
            segment.add_line_intersection(previous_line)
            segment.add_line_intersection(inter_line)
            segments.append(segment)

            previous = inter
            previous_line = inter_line
        else:
            segments.append(IntersectionLine(previous, p2))  # we can't forget the last point

        valid_line = sorted(segments, key=lambda s: s.line_size(), reverse=True)[0]  # keeps the segment with the greatest size
        current_line = valid_line


    alpha = map(current_line.line_size(), 0, 900, 100, 255)
    w = map(current_line.line_size(), 0, 900, 1, 5)
    strokeWeight(w)
    stroke(color(21, 153, 210, alpha))
    lines.append(current_line)
    current_line.display()

    print(frameCount)

count = 0
def keyPressed():
    global count, lines

    if key == 'n':
        count += 1
        saveFrame("{}.png".format(count))
        lines = []
        background(BLACK)
        redraw()
    elif key == 'b':
        background(BLACK)