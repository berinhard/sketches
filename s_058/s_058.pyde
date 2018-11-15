# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames

WHITE = color(235, 235, 235, 120)
RED = color(181, 32, 10)
BLACK = color(27, 27, 27)
GOLDEN = color(218, 145, 32)
GREEN = color(49, 114, 59)
COLORS = [GOLDEN, GREEN, BLACK]
COLORS_2 = [GOLDEN] * 80 + [WHITE] * 20

def setup():
    global positions, colors, colors_2, randoms

    size(800, 800)
    strokeWeight(3)
    #frameRate(8)
    stroke(WHITE)
    background(RED)


def get_symmetric(x, y, base_x, base_y):
    x = abs(base_x + x)
    y = abs(base_y + y)
    return x, y


def draw_pattern(base_x, base_y, vertex_x, vertex_y):
    x0, y0 = get_symmetric(0, 0, base_x, base_y)
    x1, y1 = get_symmetric(vertex_x, 0, base_x, base_y)
    x2, y2 = get_symmetric(0, vertex_y, base_x, base_y)

    triangle(x0, y0, x1, y1, x2, y2)


def draw():
    vertex_x = noise(frameCount / 10.0) * width * 1.1
    vertex_y = noise((1042 + frameCount) / 82.0) * height

    colors = [choice(COLORS) for i in range(4)]

    fill(colors[0])
    draw_pattern(0, 0, vertex_x, vertex_y)
    fill(colors[1])
    draw_pattern(-1 * width / 2, 0, vertex_x, vertex_y)
    fill(colors[2])
    draw_pattern(0, -1 * height / 2, vertex_x, vertex_y)
    fill(colors[3])
    draw_pattern(-1 * width / 2, -1 * height / 2, vertex_x, vertex_y)

    with pushMatrix():
        translate(width, height)
        angle = 180
        rotate(radians(angle))

        fill(colors[0])
        draw_pattern(0, 0, vertex_x, vertex_y)
        fill(colors[1])
        draw_pattern(-1 * width / 2, 0, vertex_x, vertex_y)
        fill(colors[2])
        draw_pattern(0, -1 * height / 2, vertex_x, vertex_y)
        fill(colors[3])
        draw_pattern(-1 * width / 2, -1 * height / 2, vertex_x, vertex_y)

    save_video_frames(8, 10 * 60)