# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames

WHITE = color(235)
RED = color(181, 32, 10, 210)
BLACK = color(27, 27, 27, 220)
GOLDEN = color(218, 145, 32)
GREEN = color(49, 114, 59)
COLORS = [BLACK] * 60 + [RED] * 40

def setup():
    global positions, colors

    size(800, 800)
    strokeWeight(3)

    circle_space = 50
    grid = range(25, width / 2, circle_space)
    positions = []
    for x in grid:
        for y in grid:
            positions.append((x, y))

    colors = [choice(COLORS) for p in positions]


def get_symmetric(x, y, base_x, base_y):
    x = abs(base_x + x)
    y = abs(base_y + y)
    return x, y


def draw_pattern(base_x, base_y):
    for i, coord in enumerate(positions):
        x, y = coord
        noise_scale = 17.0
        n = noise((frameCount + i) / noise_scale)
        radius = map(n, 0, 1, 30, 110)

        c = colors[i]
        x, y = get_symmetric(x, y, base_x, base_y)

        fill(c)
        ellipse(x, y, radius, radius)


def draw():
    global positions, colors
    if not (frameCount - 1) % 200:
        colors = [choice(COLORS) for p in positions]

    background(WHITE)
    draw_pattern(0, 0)
    draw_pattern(-1 * width, 0)
    draw_pattern(0, -1 * height)
    draw_pattern(-1 * width, -1 * height)

    #noLoop()
    #save_video_frames(25, 60 * 10)