# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.grids import VirtualGrid
from berin.save_frames import save_video_frames
from random import choice


WHITE = color(235, 235, 235)
LIGHT_WHITE = color(213, 1)
BLACK = color(27, 27, 27)
colors = []

def recursive_triangles(p1, p2, p3, depth):
    triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
    if depth == 0:
        return

    points = [p1, p2, p3]
    new_p1 = choice([p1, p2, p3])
    points.remove(new_p1)

    new_p2 = PVector.lerp(points[0], points[1], 0.5)
    new_p3 = choice(points)

    recursive_triangles(new_p1, new_p2, new_p3, depth - 1)


def setup():
    size(900, 900)
    stroke(LIGHT_WHITE)
    background(BLACK)
    noFill()
    strokeWeight(2)
    frameRate(24)


def draw():
    p1 = PVector(0, 0)
    p2 = PVector(0, height)
    p3 = PVector(width, height)
    p4 = PVector(width, 0)
    recursive_triangles(p1, p2, p3, 5)
    recursive_triangles(p1, p4, p3, 5)
    print(frameCount)


def keyPressed():
    if key == 'n':
        redraw()
    if key == 's':
        saveFrame("###########.png")