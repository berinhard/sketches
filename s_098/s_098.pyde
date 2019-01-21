# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

# Georg Nees Schotter study
# Based at Jim Plaxco's tutorial: http://www.artsnova.com/Nees_Schotter_Tutorial.html
from berin.shapes import regular_polygon
from random import choice

columns = 12
rows = 22
square_size = 30
rotation_step = 0.14
padding = 2 * square_size
soft_translation = 0.42

WHITE = color(248, 248, 248)
BLACK = color(17, 17, 17)

def setup():
    size((columns + 4) * square_size,(rows + 4) * square_size);
    strokeWeight(1)
    noFill()
    frameRate(2)
    rectMode(CENTER)
    stroke(BLACK)
    smooth()

def draw():
    background(WHITE)

    random_sum = 0
    for j, y in sorted(enumerate(range(padding, height - padding, square_size)), reverse=True):
        random_sum += j * rotation_step
        for x in range(padding, width - padding, square_size):
            random_v = random(-random_sum, random_sum)
            new_x, new_y = x + random_v * soft_translation, y + random_v * soft_translation

            with pushMatrix():
                translate(new_x, new_y)
                rotate(radians(random_v))

                current_size = square_size

                r, g, b = 17, 17, 17
                while current_size >= 10:
                    stroke(color(r, g, b, map(current_size, 10, square_size, 100, 255)))
                    radius = current_size * sqrt(2) / 2
                    regular_polygon(0, 0, radius, 4, angle_rotation=3 * QUARTER_PI + PI)
                    current_size -= 5

    saveFrame("#####.png")