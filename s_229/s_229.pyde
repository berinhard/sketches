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


# patterns' reference: https://twitter.com/takawo/status/1173395633186557953


def pattern_1(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, -h, d, h)
    arc(h, 0, d, d, HALF_PI, PI)

def pattern_2(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, -h, h, d)

def pattern_3(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(-h, -h, -h, h, h, h)

def pattern_4(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, -h, d, d)

def pattern_5(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, 0, d, h)
    triangle(-h, 0, 0, 0, 0, -h)

def pattern_6(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(0, 0, 0, h, -h, h)
    triangle(0, 0, 0, -h, h, -h)

def pattern_7(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(0, 0, h, h)
    triangle(0, 0, h, 0, h, -h)

def pattern_8(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(-h, -h, 0, -h, -h, 0)
    triangle(h, h, h, 0, 0, h)

def pattern_9(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, -h, h, h)
    rect(0, 0, h, h)

def pattern_10(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(0, 0, h, 0, 0, h)
    arc(0, 0, d, d, HALF_PI, PI)
    rotate(PI)
    triangle(0, 0, h, 0, 0, h)
    arc(0, 0, d, d, HALF_PI, PI)


patterns = [
    #pattern_1,
    pattern_2,
    pattern_3,
    pattern_4,
    pattern_5,
    pattern_6,
    pattern_7,
    pattern_8,
    pattern_9,
]

img = None
img_2 = None

def setup():
    global img, img_2
    size(1280, 960)
    img = loadImage("img.jpg")
    img_2 = loadImage("img_2.jpg")
    stroke(42)
    fill(240)


def draw():
    background(240)

    tam = 80
    rot_angles = [0, HALF_PI, PI, 3 * HALF_PI]

    for x in range(0, width, tam):
        for y in range(0, height, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                fill(42)
                pattern = choice(patterns)
                pattern(tam, choice(rot_angles))

    loadPixels()

    pixels_map = {}
    img.loadPixels()
    img_2.loadPixels()
    for x in range(0, width):
        for y in range(0, height):
            loc = x + y * width
            pix = pixels[loc]
            r, g, b = red(pix), green(pix), blue(pix)
            if r == g == b == 42:
                pixels_map[loc] = img.get(x, y)
            elif r == g == b == 240:
                pixels_map[loc] = img_2.get(x, y)

    updatePixels()

    background(42)
    loadPixels()
    for k, v in pixels_map.items():
        pixels[k] = v
    updatePixels()

    noLoop()

def keyPressed():
    if key == 'n':
        loop()
        redraw()
    elif key == 's':
        saveFrame("########.png")