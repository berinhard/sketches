# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Live demo: https://berinhard.github.io/sketches/s_194/
# Created with https://github.com/berinhard/pyp5js
from pytop5js import *


square_size = 40
squares_map = {}


class Square:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self._alpha = 1
        self.color = (random(255), random(255), random(255), self.alpha)

    def display(self):
        if self.alpha == 1:
            fill(27)
        else:
            fill(*self.color)
        stroke(27, 27, 27, 30)
        rect(self.x, self.y, self.size, self.size)

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if self._alpha + value < 255:
            self._alpha += value

    def update(self):
        self.alpha += 2
        self.color = self.color[0], self.color[1], self.color[2], self.alpha


def setup():
    pixelDensity(displayDensity())
    w, h = window.innerWidth, window.innerHeight
    createCanvas(w, h)
    for x in range(0, w, square_size):
        for y in range(0, h, square_size):
            squares_map[(x, y)] = Square(x, y, square_size)
    background(27)


def clean_coord(x, y):
    x = x // square_size * square_size
    y = y // square_size * square_size
    return x, y


def draw():
    background(27)

    for square in squares_map.values():
        square.display()

    x, y = clean_coord(mouseX, mouseY)
    squares_map[(x, y)].update()
