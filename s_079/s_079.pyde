# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
import json


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)


def initial_state():
    global cols

    space = 15
    cols = range(0, width, space)


def setup():
    size(900, 900)
    background(WHITE)
    stroke(BLACK)
    initial_state()
    strokeWeight(1)
    noFill()
    stroke(BLACK)

def draw():
    for i, x in enumerate(cols):
        with pushMatrix():
            translate(x, 0)

            p1 = PVector(0, 0)
            p2 = PVector(0, x)

            line(p1.x, p1.y, p2.x, p2.y)

        with pushMatrix():
            translate(x, x)

            p1 = PVector(0, 0)
            p2 = PVector(0, height - x)

            line_size = PVector.dist(p1, p2)
            num_points = int(map(line_size, 15, 900, 1, 6))
            internal_points = [p1] + subdivide_line(p1, p2, num_points) + [p2]

            for i, p in enumerate(internal_points[1:]):
                previous_p = internal_points[i]
                paralel_lines(previous_p, p)

    noLoop()

def subdivide_line(p1, p2, depth):
    """
    Dado dois pontos, essa função retorna os pontos intermediários.
    Quanto maior o depth, mais pontos são retornados
    """
    if not depth:
        return []

    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2 + random(-20, 20)

    new_p = PVector(mid_x, mid_y)

    new_depth = depth - 1
    points = subdivide_line(p1, new_p, new_depth)
    points.append(new_p)
    points.extend(subdivide_line(new_p, p2, new_depth))

    return points

def paralel_lines(p1, p2):
    """
    Adaptação do código de desenhar setas do Alexandre Villares
    """
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    num_lines = [0, 2, 4, 6]

    L = PVector.dist(p1, p2)
    with pushMatrix():
        translate(p1.x, p1.y)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        line(0, 0, 0, L)

        for i in range(choice(num_lines)):
            index = i + 1
            x_off = 1 * index
            if not index % 2:
                x_off *= -1
            if x_off > 0:
                x_off += 1
            line(x_off, 0, x_off, L)

def keyPressed():
    if key == 's':
        saveFrame("#######.png")