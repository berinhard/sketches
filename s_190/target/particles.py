from pytop5js import *


class Particle():

    def __init__(self):
        self.pos = createVector(
            random(width),
            random(height)
        )
        self.speed = createVector(
            random(-5, 5),
            random(-5, 5),
        )

    def move(self):
        self.pos.add(self.speed)

    def display(self):
        ellipse(self.pos.x, self.pos.y, 10, 10)

    def out_of_boundaries(self):
        return any([
            self.pos.x < 0,
            self.pos.x > width,
            self.pos.y < 0,
            self.pos.y > height,
        ])
