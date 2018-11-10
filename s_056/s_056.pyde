# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames

WHITE = color(235)
RED = color(181, 32, 10)
BLACK = color(27, 27, 27)
GOLDEN = color(218, 145, 32)
GREEN = color(49, 114, 59)
COLORS = [GOLDEN] * 90 + [GREEN] * 10
COLORS_2 = [GOLDEN] * 80 + [WHITE] * 20

def setup():
    global positions, colors, colors_2, randoms

    size(800, 800)
    strokeWeight(3)
    frameRate(0.5)

    circle_space = 50
    grid = range(25, width / 2 + 25, circle_space)
    positions = []
    for x in grid:
        for y in grid:
            positions.append((x, y))

    colors = [choice(COLORS) for p in positions]
    colors_2 = [choice(COLORS_2) for p in positions]
    randoms = [random(1) for p in positions]


def get_symmetric(x, y, base_x, base_y):
    x = abs(base_x + x)
    y = abs(base_y + y)
    return x, y


def draw_pattern(base_x, base_y):
    for i, coord in enumerate(positions):
        x_0, y_0 = coord
        noise_scale = 17.0
        n = noise((frameCount + i) / noise_scale)

        x, y = get_symmetric(x_0, y_0, base_x, base_y)

        c = colors[i]
        #fill(c)
        fill(BLACK)

        if randoms[i] > 0.57:
            radius = 50
            ellipse(x, y, radius, radius)

            if base_x:
                x, y = get_symmetric(x_0 + radius / 2, y_0, base_x, base_y)
            if base_x:
                x, y = get_symmetric(x_0 + radius / 2, y_0, base_x, base_y)

            fill(c)
            rect(x, y, radius / 2, radius / 2)



def draw():
    global positions, colors, randoms

    colors = [choice(COLORS) for p in positions]
    randoms = [random(1) for p in positions]

    stroke(WHITE)
    background(RED)
    draw_pattern(0, 0)
    draw_pattern(-1 * width, 0)
    draw_pattern(0, -1 * height)
    draw_pattern(-1 * width, -1 * height)

    #noLoop()
    #save_video_frames(0.5, 60 * 10)
