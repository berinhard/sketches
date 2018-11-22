# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames

WHITE = color(235, 235, 235)
RED = color(181, 32, 10, 190)
BLACK = color(27, 27, 27, 190)
GOLDEN = color(218, 145, 32, 140)
GREEN = color(49, 114, 59, 105)
COLORS = [GOLDEN, GREEN, BLACK]
COLORS_2 = [GOLDEN] * 80 + [WHITE] * 20

INTERVAL = 10
px, py = -1000, -1000

def setup():
    size(800, 800)
    strokeWeight(2)
    frameRate(25)
    noStroke()


def draw():
    background(WHITE)
    intervals = range(INTERVAL, width - INTERVAL, INTERVAL)


    offset = 200
    n_offset = -200
    n_x = noise(frameCount / 92.0)
    n_y = noise(frameCount / 100.0)
    px, py = map(n_x, 0, 1, n_offset, width + offset), map(n_y, 0, 1, n_offset, height + offset)

    n_x_2 = noise((frameCount) / 102.0)
    n_y_2 = noise((frameCount) / 82.0)
    px_2, py_2 = map(n_x_2, 0, 1, n_offset, width + offset), map(n_y_2, 0, 1, n_offset, height + offset)


    for i, x in enumerate(intervals):
        for j, y in enumerate(intervals):
            index = i + j * len(intervals)
            n = noise((index + frameCount) / 74.0)

            rot_angle = radians(map(n, 0, 1, 0, 360))

            fill(GREEN)

            dist_1 = dist(x, y, px, py)
            dist_2 = dist(x, y, px_2, py_2)
            random_rot = False

            if dist_1 <= 50 and dist_2 <= 50:
                fill(choice([BLACK, RED]))
                random_rot = True
            elif dist_1 <= 50:
                fill(BLACK)
                random_rot = True
            elif dist_2 <= 50:
                fill(RED)
                random_rot = True

            if random_rot:
                rot_angle = radians(map(random(1), 0, 1, 0, 360))

            with pushMatrix():
                translate(x + INTERVAL / 2, y + INTERVAL / 2)
                rotate(rot_angle)
                w, h = 10, 10
                rect(0, 0, w, h)

    #save_video_frames(25, 10 * 60)