# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from random import choice
from berin.palettes import get_color_palette

COLORS = get_color_palette()

def setup():
    #size(900, 900)
    size(int(900*4.166),int(900*4.166))
    noStroke()
    rectMode(CENTER)
    background(0)

def draw():
    scale(300/72.0)

    square_sizes = range(50, 300, 25)
    square_positions_x = range(0, width, 25)
    square_positions_y = range(0, height, 25)
    angle_start = 0
    angles = [
        angle_start,
        angle_start + QUARTER_PI,
    ]

    x = choice(square_positions_x)
    y = choice(square_positions_y)

    with pushMatrix():
        d = choice(square_sizes)
        angle = choice(angles)
        translate(x, y)
        rotate(angle)
        fill(0, 0, 0, 30)

        if angle == angle_start:
            rect(10, 10, d, d)
        else:
            rect(10, 0, d, d)

        fill(choice(COLORS))
        rect(0, 0, d, d)

    print(frameCount)

def _redraw():
    background(0)
    redraw()


def keyPressed():
    global COLORS
    if key == 'z':
        COLORS = get_color_palette()
        _redraw()
    if key == 'n':
        _redraw()
    if key == '1':
        COLORS = ['#a2825c', '#88d3ab', '#f9fad2', '#f5da7a', '#ff985e', '#ff985e', '#ff985e', '#ff985e', '#ff985e']  # marrom, azul, bege, amarelo, laranja
        _redraw()
    if key == '2':
        COLORS = ['#a2825c', '#88d3ab', '#f9fad2', '#f9fad2', '#f9fad2', '#f9fad2', '#f5da7a', '#ff985e']  # marrom, azul, bege, amarelo, laranja
        _redraw()
    if key == '3':
        COLORS = ['#a2825c', '#88d3ab', '#88d3ab', '#88d3ab', '#88d3ab', '#88d3ab', '#f9fad2', '#f5da7a', '#ff985e']  # marrom, azul, bege, amarelo, laranja
        _redraw()
    if key == 's':
        saveFrame("#####.png")

    name = str(COLORS)
    print(name)