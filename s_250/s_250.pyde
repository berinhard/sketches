# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice

axiom = 'A'
sentence = axiom
rules = {
    'A': 'AA+A+AA-A-AA+B',
    'B': 'BB-B-BB+B+BB-A'
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

    print('desenhando: ' + sentence)
    for c in sentence:
        if c in ['A', 'B']:
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
    angle = (PI / 2)
    tam *= 0.5
    alpha = 80

    background(42)
    strokeWeight(4)
    strokeCap(SQUARE)

    resetMatrix()
    stroke(240, alpha)
    draw_sentence(width / 2 + 100, height / 2, tam, angle)

    resetMatrix()
    stroke(231, 42, 39, alpha)
    draw_sentence(width / 2 - 100, height / 2, -tam, -(angle + PI))

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
