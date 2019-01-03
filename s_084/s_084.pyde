# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin import coords


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)


def setup():
    size(800, 800)
    strokeWeight(3)
    background(WHITE)

n = 0  # noise counter

def draw():
    global n

    with coords.draw_at_center():
        n += 0.07
        main_radius = map(noise(n), 0, 1, -50, 410)
        for i, angle in enumerate(range(0, 360, 10)):
            stroke(BLACK)
            angle += frameCount % 360
            if 180 <= main_radius <= 240:
                stroke(RED)

            angle = radians(angle)
            x = cos(angle) * main_radius
            y = sin(angle) * main_radius

            point(x, y)

        print frameCount

def keyPressed():
    if key == 's':
        saveFrame("#############.png")