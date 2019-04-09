# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import uniform

move, target = None, None
def setup():
    size(900, 900)
    strokeWeight(3)
    background(240)
    stroke(color(27, 27, 27, 10))

def draw():
    v1 = PVector(100, 100)
    v2 = PVector(800, 100)
    v3 = PVector(800, 800)
    v4 = PVector(100, 800)
    vertices = [v1, v2, v3, v4]

    random_index = int(random(len(vertices)))
    random_v1, random_v2 = vertices[random_index], vertices[random_index - 1]
    p1 = PVector.lerp(random_v1, random_v2, random(1))

    random_index = int(random(len(vertices)))
    random_v1, random_v2 = vertices[random_index], vertices[random_index - 1]
    p2 = PVector.lerp(random_v1, random_v2, random(1))

    if not(p1.x == p2.x or p1.y == p2.y):
        line(p1.x, p1.y, p2.x, p2.y)


def keyPressed():
    if key == 's':
        saveFrame("########.png")