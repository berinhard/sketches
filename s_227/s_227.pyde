# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice

img = None
COLORS = get_color_palette()
colors_by_x = []

def setup():
    global img
    size(1280, 960)
    img = loadImage("img.jpeg")

    curr_color = choice(COLORS)
    for x in range(1280):
        if not x % 5:
            curr_color = choice(COLORS)
        colors_by_x.append(curr_color)



def draw():
    img.loadPixels()
    loadPixels()

    for x in range(0, width):
        for y in range(0, height):
            img_pixel = img.get(x, y)
            location = x + y * width
            img_bright = map(brightness(img_pixel), 0, 255, 0, 1)

            if img_bright < 0.5:
                c = colors_by_x[x]
                r, g, b = red(c), green(c), blue(c)
                pixels[location] = color(r, g, b)
            else:
                pixels[location] = img_pixel

    updatePixels()
    saveFrame("cover.png")
    noLoop()