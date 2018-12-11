# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)
GOLDEN = color(218, 185, 32, 140)
GREEN = color(32, 181, 10)

def setup():
    size(400, 900)
    background(WHITE)
    strokeWeight(2)
    frameRate(1)
    noFill()

def polygon_points(x, y, radius, num_points):
    """
    Python version of https://processing.org/examples/regularpolygon.html
    """
    angle = 0
    vertex_angle = TWO_PI / num_points

    points = []
    while angle < TWO_PI:
        sx = x + cos(angle) * radius
        sy = y + sin(angle) * radius
        points.append((sx, sy))
        angle += vertex_angle

    return points

def draw():
    background(WHITE)

    single_line_size = 30
    y_range = range(100, height - 100, single_line_size)

    for i, x in enumerate(range(25, width - 25, single_line_size)):
        x += int(single_line_size / 2)
        for j, y in enumerate(y_range):
            current_x = x
            power = (len(y_range) - j) ** 1.2
            random_v = random(1) ** power
            angle = int(map(random_v, 0, 1, 0, 360))

            if angle:
                stroke(RED)
                scale = 0.6
                current_x = int(current_x + map(random(1), 0, 1, -1 * (j ** scale), j ** scale))
                y = int(y + map(random(1), 0, 1, -1 * (j ** scale), j ** scale))
            else:
                stroke(BLACK)

            with pushMatrix():
                translate(current_x, y)
                if angle:
                    rotate(radians(angle))
                rotate(radians(270 + angle))
                triangle_points = polygon_points(0, 0, 14, 3)
                p1, p2, p3 = triangle_points

                edge_1 = lerp(p1[0], p2[0], 0.75), lerp(p1[1], p2[1], 0.75)
                edge_2 = lerp(p1[0], p3[0], 0.75), lerp(p1[1], p3[1], 0.75)

                xedge_1 = lerp(p1[0], p2[0], 0.25), lerp(p1[1], p2[1], 0.25)
                xedge_2 = lerp(p1[0], p3[0], 0.25), lerp(p1[1], p3[1], 0.25)


                points = [edge_1, p1, edge_2]

                beginShape()
                for xy in triangle_points:
                    vertex(*xy)

                if angle:
                    line(edge_1[0], edge_1[1], edge_2[0], edge_2[1])
                    line(xedge_1[0], xedge_1[1], xedge_2[0], xedge_2[1])
                else:
                    vertex(triangle_points[0])

                endShape()


def keyPressed():
    if key == 's':
        saveFrame("#######.png")
