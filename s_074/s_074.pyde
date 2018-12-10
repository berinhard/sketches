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

COLORS = [RED, GREEN, GOLDEN]


followers = []


class PathFollower():

    def __init__(self, start, end, exponent=0.5, step=0.01):
        self.start = start
        self.exponent = exponent
        self.step = step
        self.current = self.start
        self.go_to(end)
        self.color = WHITE

    def go_to(self, end):
        self.end = end
        self.start = self.current
        self.percentage_travelled = 0.0


    @property
    def dist_x(self):
        return self.end.x - self.start.x

    @property
    def dist_y(self):
        return self.end.y - self.start.y

    @property
    def is_walking(self):
        return self.percentage_travelled < 1.0

    def walk(self):
        self.percentage_travelled += self.step

        if self.is_walking:
            x = self.start.x + self.percentage_travelled * self.dist_x
            y = self.start.y + self.percentage_travelled ** self.exponent * self.dist_y
            self.current = PVector(x, y)

    def display(self):
        fill(self.color)
        ellipse(self.current.x, self.current.y, 20, 20)


def populate():
    global followers

    followers = []
    for i in range(15):
        start = PVector(random(width), random(height))
        end = PVector(random(width), random(height))
        follower = PathFollower(start, end, random(1), (i + 1) / 1000.0)
        followers.append(follower)


def setup():
    size(800, 800)
    strokeWeight(2)
    noStroke()
    background(BLACK)

    populate()


def draw():
    print(frameCount)
    for follower in followers:
        if not follower.is_walking:
            end = PVector(random(width), random(height))
            follower.go_to(end)
        follower.walk()
        follower.display()


def keyPressed():
    if key == 's':
        saveFrame("#######.png")
    elif key == 'n':
        populate()
        background(BLACK)