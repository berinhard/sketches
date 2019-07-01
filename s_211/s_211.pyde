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


base_size = 100
def init_flowers():
    global r_size, flores

    r_size = base_size
    flores = []

    colors_range = range(160, 190)

    colors = [color(c, 39, 240, 5) for c in colors_range]
    for x in range(0 , width + base_size, base_size * 2):
        for y in range(0 , height + base_size, base_size * 2):
            petalas = int(random(4, 12))
            flores.append(
                (x, y, choice(colors), petalas)
            )

    background(240)

def setup():
    size(900, 900)
    init_flowers()
    colorMode(HSB, 360)

def draw():
    global r_size

    for x, y, cor, petalas in flores:
        rotacao_petala = TWO_PI / petalas

        for petala in range(petalas):
            with pushMatrix():
                translate(x, y)
                angle = radians(frameCount * 1.2) + rotacao_petala * petala
                rotate(angle)

                noFill()
                strokeWeight(1)
                stroke(cor)
                rect(0, 0, r_size, r_size)
                triangle(0, 0, 0, r_size, r_size, r_size)

    r_size -= 1

    print(frameRate)
    if frameCount > 2 * base_size :
        saveFrame("#########.png")
        noLoop()

def keyPressed():
    if key == 'n':
        init_flowers()
    elif key == 's':
        saveFrame("########.png")