# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Live demo: https://berinhard.github.io/sketches/s_195/
# Created with https://github.com/berinhard/pyp5js
from pytop5js import *
from random import choice


square_size = 30
squares_map = {}


class Circle:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.base_size = size
        self.size = size
        self.i, self.j = self.x // square_size, self.y // square_size
        self.color = color(0, 255, 255, 15)

    def display(self):
        noFill()
        stroke(self.color)
        strokeWeight(3)
        ellipse(self.x, self.y, self.size, self.size)

    def update(self):
        r = map(noise(self.i, self.j, frameCount * 0.01), 0, 1, -40, 140)
        self.size = self.base_size + r



def setup():
    pixelDensity(displayDensity())
    w, h = window.innerWidth, window.innerHeight
    createCanvas(w, h)
    for x in range(0, w + square_size, square_size):
        for y in range(0, h + square_size, square_size):
            squares_map[(x, y)] = Circle(x, y, square_size)

def clean_coord(x, y):
    x = x // square_size * square_size
    y = y // square_size * square_size
    return x, y


def draw():
    background(27)

    for square in squares_map.values():
        square.update()
        square.display()

    print(frameRate())
