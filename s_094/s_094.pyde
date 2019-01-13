# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import draw_shape
from berin.save_frames import save_video_frames
from random import choice


WHITE = color(228, 228, 228, 200)
RED = color(228, 12, 10, 200)
BLACK = color(17, 17, 17)


def setup():
    size(900, 900)
    strokeWeight(1)
    stroke(WHITE)
    noFill()
    background(BLACK)

def draw():
    radius = int(random(20, 300))
    x_positions = range(0, width, 20)
    y_positions = range(0, height, 20)
    x, y = choice(x_positions), choice(y_positions)

    if random(1) < 0.8:
        c = WHITE
        alpha = 180
    else:
        alpha = 230.0
        c = RED

    alpha_rate = alpha / radius
    r, g, b = red(c), green(c), blue(c)
    while radius > 20:
        stroke(color(r, g, b, radius * alpha_rate))
        ellipse(x, y, radius, radius)
        radius -= 12

    if not frameCount % 90:
        saveFrame("#######.png")
        background(BLACK)