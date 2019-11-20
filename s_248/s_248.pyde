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


axiom = 'F'
sentence = axiom
rules = {
    'F': 'FF+[+F-F-F]-[-F+F+F]'
}


def generate():
    global sentence

    println('starting sentece!')
    new_sentence = ''
    for c in sentence:
        new_sentence += rules.get(c, c)

    println('new sentece!')
    sentence = new_sentence

    print('drawing new generation...')
    refresh_draw()
    print('done!')


def draw_sentence(x, y, tam, angle):
    translate(x, y)

    for c in sentence:
        if c == 'F':
            line(0, 0, tam, 0)
            translate(tam, 0)
        elif c == '+':
            rotate(angle)
        elif c == '-':
            rotate(-angle)
        elif c == '[':
            pushMatrix()
        elif c == ']':
            popMatrix()

tam = 200
def refresh_draw():
    global tam
    offset = 100
    angle = (PI / 12)
    tam *= 0.5
    alpha = 5

    background(42)
    strokeWeight(3)
    strokeCap(ROUND)

    resetMatrix()
    stroke(240, alpha)
    draw_sentence(0, height / 2 + offset, tam, angle)

    resetMatrix()
    stroke(231, 42, 39, alpha)
    draw_sentence(width, height / 2 - offset, -tam, angle)

def setup():
    size(900, 900)
    print(sentence)
    generate()

def mouseClicked():
    generate()

def draw():
    pass


c = 1
def keyPressed():
    global c
    if key == 's':
        saveFrame(str(c) + '.png')
        c += 1