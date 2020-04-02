# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings

from random import choice, shuffle

img = None

def setup():
    global img
    size(1400, 1400)




def draw():
    background(15, 15, 17)
    img = loadImage('image.jpg')
    offset = 2
    for x in range(0, width, offset):
        i = x % 3
        value = ['r', 'g', 'b'][i]
        for y in range(0, height, offset):
            x_img = int(x / offset) - int(512 / 4.5)
            y_img = int(y / offset)
            pixel_color = img.get(x_img, y_img)

            if brightness(pixel_color) < 16:
                r, g, b = red(pixel_color), green(pixel_color), blue(pixel_color)

                random_v = 100
                if value == 'r':
                    r += random(-random_v, random_v)
                    g += random(-random_v, random_v)
                elif value == 'g':
                    g += random(-random_v / 4, random_v / 4)
                    b += random(-random_v / 4, random_v / 4)
                elif value == 'b':
                    b += random(-random_v * 2, random_v * 2)
                pixel_color = color(r, g, b)

            positions = [
                (x, y),
                (x + 1, y),
                (x + 1, y + 1),
                (x, y + 1),
            ]

            for x, y in positions:
                set(x, y, pixel_color)

    saveFrame('cover.png')
    noLoop()