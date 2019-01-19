# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.shapes import regular_polygon
from berin.save_frames import save_video_frames
from random import choice


WHITE = color(228, 228, 228, 200)
RED = color(228, 12, 10, 200)
BLACK = color(17, 17, 17)


def setup():
    size(900, 900)
    strokeWeight(1.5)
    stroke(WHITE)
    noFill()
    background(BLACK)

def draw():
    radius = 20#int(random(20, 300))
    x_positions = range(0, width + 100, 100)
    y_positions = range(0, height + 100, 100)
    #x, y = choice(x_positions), choice(y_positions)

    for x in x_positions:
        for y in y_positions:

            radius = 50
            if random(1) < 0.8:
                c = WHITE
                alpha = 180
            else:
                alpha = 230.0
                c = RED

            alpha_rate = alpha / radius
            weight_rate = radius / 20
            r, g, b = red(c), green(c), blue(c)
            while radius > 10:
                strokeWeight(1.5 * weight_rate)
                stroke(color(r, g, b, 210))
                regular_polygon(x, y, radius, 4, angle_rotation=QUARTER_PI)
                radius -= 5

            #if not frameCount % 90:
            #    saveFrame("#######.png")
            #    background(BLACK)