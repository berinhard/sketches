# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

def setup():
    size(900, 900)

def draw():
    v1 = PVector(100, 100)
    v2 = PVector(800, 100)
    v3 = PVector(800, 800)
    v4 = PVector(100, 800)
    vertices = [v1, v2, v3, v4]

    index = int(random(len(vertices)))
    v1, v2 = vertices[index], vertices[index - 1]
    percent = random(1)
    p1 = PVector.lerp(v1, v2, percent)

    index = int(random(len(vertices)))
    v1, v2 = vertices[index], vertices[index - 1]
    percent = random(1)
    p2 = PVector.lerp(v1, v2, percent)

    line(p1.x, p1.y, p2.x, p2.y)