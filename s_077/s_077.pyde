# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames
import json


WHITE = color(235, 235, 235, 7)
BLACK = color(27, 27, 27)
RED = color(181, 32, 10, 7)
GOLDEN = color(218, 185, 32, 7)
GREEN = color(32, 181, 10, 7)
CYAN = color(20, 255, 255, 7)
PURPLE = color(255, 20, 255, 7)

COLORS = [RED, GOLDEN, GREEN, CYAN, PURPLE, WHITE]


followers = []


class Particle():

    def __init__(self, x, y, angle=0):
        self.angle = angle
        self.speed = random(0.2, 0.8)
        self.x, self.y = x, y


    def move(self):
        self.angle += random(-0.4, 0.4)

        x_offset = cos(self.angle) * self.speed
        y_offset = sin(self.angle) * self.speed

        x = self.x + x_offset
        y = self.y + y_offset
        if not 0 < x < width:
            x_offset *= -1
        if not 0 < y < height:
            y_offset *= -1

        self.x += x_offset
        self.y += y_offset

    def display(self):
        with pushMatrix():
            translate(self.x, self.y)
            rotate(self.angle)
            line(0, -10, 0, 10)

def populate():
    global followers

    followers = []
    for i in range(30):
        follower = Particle(random(width), random(height))
        followers.append(follower)


def setup():
    size(800, 800)
    strokeWeight(1)
    stroke(COLORS.pop(0))
    background(BLACK)
    frameRate(1000)

    populate()


def draw():
    for follower in followers:
        follower.move()
        follower.display()

    if not frameCount % 9000:
        saveFrame("#######.png")
        if COLORS:
            populate()
            background(BLACK)
            stroke(COLORS.pop(0))
        else:
            noLoop()


def keyPressed():
    if key == 's':
        saveFrame("#######.png")
    elif key == 'n':
        populate()
        background(BLACK)