# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import choice

SCALE = 1


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
    print('done! new sentence len: ' + str(len(sentence)))


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

tam = 260 * SCALE
def refresh_draw():
    global tam
    offset = 200 * SCALE
    angle = (PI / 12)
    tam *= 0.505
    alpha = 5

    background(42)
    strokeWeight(3 * SCALE)
    strokeCap(ROUND)

    print("\tDrawing tree 01...")
    resetMatrix()
    stroke(235, 222, 205, alpha)
    draw_sentence(0, height / 2 + offset, tam, angle)

    print("\tDrawing tree 02...")
    resetMatrix()
    stroke(29, 117, 105, alpha)
    draw_sentence(width, height / 2 - offset, -tam, angle)


add_library('svg')
def setup():
    size(1200 * SCALE, 1200 * SCALE)
    scale(SCALE)

def mouseClicked():
    redraw()

def draw():
    #print(sentence)

    f = createGraphics(width, height, SVG, "out.svg")
    beginRecord(f)
    generate()
    saveFrame("#########.png")
    noLoop()
    endRecord()