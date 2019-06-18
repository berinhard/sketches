# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# Live demo: https://berinhard.github.io/sketches/s_195/
# Created with https://github.com/berinhard/pyp5js
from pyp5js import *
from random import choice


square_size = 30
squares = []


class Square:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color(0, 255, 255, 8)
        self._angle = 0
        self.sin_angle = random(0, TWO_PI)
        self.speed = int(random(1, 6))
        self.rotation_speed = random(0.01, 0.1)
        self._revert = False

    def display(self):
        push()

        r = map(self.angle, TWO_PI, 0, 0, self.size)
        if self._revert:
            r = self.size - r

        translate(self.x, self.y)
        rotate(self.angle)
        noFill()
        stroke(self.color)
        strokeWeight(2)
        rect(0, map(sin(self.sin_angle), -1, 1, -10, 10), r, r)

        pop()

    def update(self):
        prev_angle = self.angle
        self.angle = (frameCount * self.rotation_speed) % TWO_PI
        self.x += self.speed
        self.sin_angle += 0.1

        if prev_angle <= self.angle:
            self._revert = not self._revert

    @property
    def is_appearing(self):
        return self.x < (width + self.size)


def setup():
    pixelDensity(displayDensity())
    w, h = window.innerWidth, window.innerHeight
    createCanvas(w, h)

    background(27)
    rectMode(CENTER)


def draw():
    global squares

    if not frameCount % 50:
        y = mouseY
        if y > 0:
            squares.append(Square(0, y, square_size))

    for square in squares:
        square.update()
        square.display()

    squares = [s for s in squares if s.is_appearing]
