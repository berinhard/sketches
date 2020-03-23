# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from itertools import cycle
from random import choice

img_pixels = {}
cell_size = 10
title_colors = cycle([
    color(240, 0, 240),
    color(0, 240, 240),
    color(240, 240, 0),
    color(42, 42, 42),
])
active_title = next(title_colors)

def setup():
    print("loading image...")
    img = loadImage('pietro.jpeg')
    for x in range(img.width):
        for y in range(img.height):
            img_pixels[(x, y)] = (img.get(x, y), choice(['r', 'g', 'b']))
    print('done!')
    noStroke()
    size(1280, 960)
    #frameRate(24)


def draw():
    global active_title

    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            c, variant = img_pixels[(x, y)]
            r, g, b = red(c), green(c), blue(c)

            noise_value = noise(x, y, frameCount * 0.09)
            diff = map(noise_value, 0, 1, -255, 255)
            if variant == 'r':
                r += diff
            elif variant == 'g':
                g += diff
            else:
                b += diff

            c = color(r, g, b)
            fill(c)
            rect(x, y, cell_size, cell_size)


    #### TITLE
    y_grid_step = height / 12
    font = createFont("Uroob", 128)
    textFont(font)
    if not frameCount % (24 * 2):
        active_title = next(title_colors)
    fill(active_title)
    textAlign(CENTER, CENTER)
    text("pietro bapthysthe", width / 2, 2 * y_grid_step)

    #### DESC
    font = createFont("Uroob", 64)
    textFont(font)
    fill(240, 240, 240)
    text("live @ eulerroom equinox 2020", width / 2, height / 2)
    text("sunday, 22 march", width / 2, height / 2 + y_grid_step)
    text("03:30am utc / 00:30am brazil", width / 2, height / 2 + 2 * y_grid_step)

    #save_video_frames(24, 30)
    saveFrame("cover.png")
    noLoop()