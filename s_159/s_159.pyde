# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice


WIDTH, HEIGHT = 900, 900
Y_RANGE = [150, 300, 450, 600, 750]


start_x = 0
current_y = choice(Y_RANGE)
current_x = 0

noise_w, noise_h = 0, 0

BLACK = color(27, 27, 27)
WHITE = color(242, 242, 242, 15)

def setup():
    global noise_w, noise_h
    size(WIDTH, HEIGHT)
    noFill()
    background(BLACK)
    stroke(WHITE)
    strokeWeight(3)

    noise_w = noise(0)
    noise_h = noise(3124)


def draw():
    global noise_w, noise_h, current_x, current_y

    w = map(noise_w, 0, 1, 20, 80)
    h = map(noise_h, 0, 1, 100, 250)
    ellipse(current_x, current_y, w, h)

    current_x += 5
    if current_x > width:
        current_y = choice(Y_RANGE)
        current_x = 0

    noise_w = noise(frameCount * 0.004)
    noise_h = noise(frameCount* 0.0097 + 3124)


def keyPressed():
    if key == 's':
        saveFrame("########.png")