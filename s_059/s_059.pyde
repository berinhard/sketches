# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames

WHITE = color(235, 235, 235)
RED = color(181, 32, 10, 105)
BLACK = color(27, 27, 27)
GOLDEN = color(218, 145, 32, 120)
GREEN = color(49, 114, 59, 105)
COLORS = [GOLDEN, GREEN, BLACK]
COLORS_2 = [GOLDEN] * 80 + [WHITE] * 20

def setup():
    size(1500, 800)
    strokeWeight(2)
    background(BLACK)
    frameRate(60)


def draw():
    noise_scale = 132.0

    x = frameCount % width
    if not x and not (frameCount / width) % 2:
        background(BLACK)
        noiseSeed(int(random(0, 1000000000)))

    y = noise(frameCount / noise_scale) * (height - 100)

    x2 = 100 + x
    y2 = 100 + noise((100 + frameCount) / (noise_scale - 30)) * (height - 100)

    if random(1) < 0.93:
        stroke(GREEN)
        if y2 > y:
            stroke(RED)
        line(x, y, x2, y2)

    save_video_frames(60, 60 * 10)