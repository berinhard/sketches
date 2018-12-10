# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10)
GOLDEN = color(218, 185, 32, 140)
GREEN = color(32, 181, 10)

def setup():
    size(900, 900)
    background(WHITE)
    strokeWeight(4)

def draw():
    background(WHITE)

    num_cols = 4
    powers = [1, 2, 3, 4]
    spacing = 20
    col_width = width / num_cols

    lines_row_spacing = 10
    number_of_lines = (width - 100) / lines_row_spacing
    line_spacing = 5
    line_size = 30

    for counter in range(num_cols):
        x_offset = col_width * counter
        col_x_range = [x_offset + (2 * spacing), x_offset + (col_width - 2 * spacing)]
        power = powers[counter]

        col_size = col_x_range[1] - col_x_range[0]

        lines_per_col = range(col_x_range[0], col_x_range[1], line_size + line_spacing)
        for i, x in enumerate(lines_per_col):

            lines_num = range(number_of_lines)
            for j in lines_num:
                y = 50 + j * lines_row_spacing

                angle = map(j, lines_num[0], lines_num[-1], 0, 360)
                angle += frameCount

                stroke(BLACK)
                if not counter % 2:
                    stroke(RED)
                    angle *= -1

                with pushMatrix():
                    translate(x, y)
                    rotate(radians(angle))
                    line(0, 0, line_size, 0)

    if frameCount <= 360:
        saveFrame("####.png")
    else:
        noLoop()


def keyPressed():
    if key == 's':
        saveFrame("#######.png")