# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.grids import *
from random import choice
from collections import namedtuple


WHITE = color(228, 288, 288)
BLACK = color(27, 27, 27)

def setup():
    size(900, 900)
    strokeWeight(2)
    noFill()
    frameRate(2)
    rectMode(CENTER)
    stroke(WHITE)
    noFill()
    smooth()


def random_internal_grid():
    row_size = 50
    num_rows = int(random(3, 7))
    grids = [
        EvenColumnsGrid(0, 0, num_rows, row_size),
        VirtualGrid(0, 0, num_rows, row_size),
        OddLinesGrid(0, 0, num_rows, row_size),
        DiagonalsOnlyGrid(0, 0, num_rows, row_size),
        RandomPositioningGrid(0, 0, num_rows, row_size, percent=0.82),
    ]
    args = [
        (ellipse, 0, 0, 40, 40),
        (rect, 0, 0, 40, 40),
        (triangle, 0, 0, 50, 50, 0, 50),
        (line, 0, 0, 50, 50),
        (line, 0, 50, 50, 0),
        (arc, 0, 0, 40, 40, 0, PI),
        (arc, 0, 0, 40, 40, PI, 2 * PI),
    ]
    colors = [
        WHITE,
        color(255, 255, 0),
        color(255, 0, 255),
        color(0, 255, 255),
    ]
    stroke(choice(colors))
    grid = choice(grids)
    grid.draw(*choice(args))


def draw():
    background(BLACK)

    row_size = 50
    num_rows = width / row_size + 1
    main_grid = RandomPositioningGrid(0, 0, num_rows, row_size, percent=0.94)
    main_grid.draw(random_internal_grid)

    print(frameCount)
    saveFrame("######.png")
    noLoop()


def keyPressed():
    if key == 'n':
        redraw()