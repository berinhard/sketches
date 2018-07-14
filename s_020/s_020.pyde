# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice

class Mover():

    def __init__(self, x, y, speed):
        if x is None:
            x = width
        self.location = PVector(x, y)
        self.speed = speed

    def check_limits(self):
        if not 0 <= self.location.x <= width:
            self.speed.x *= -1
        if not 0 <= self.location.y <= height:
            self.speed.y *= -1

    def move(self):
        self.location.add(self.speed)

    def display(self):
        fill(self.getColor())
        e_size = 16
        ellipse(self.location.x, self.location.y, e_size, e_size)

    def getColor(self):
        return choice(self.colors)

class MoverPallete1(Mover):
    colors =  ["#172938", "#172938", "#172938", "#111E29", "#111E29", "#0D161E", "#090f14"]

class MoverPallete2(Mover):
    colors = ["#0B3B6B", "#597C9A", "#597C9A", "#597C9A", "#625591", "#625591", "#001125"]

class MoverPallete3(Mover):
    colors = ["#e8bcde", "#e8bcde", "#e8bcde", "#bb8fb4", "#bb8fb4", "#8e55a8", "#0b3b6b"]

class MoverPallete4(Mover):
    colors = ["#7c04b4", "#7896a9", "#7896a9", "#7896a9", "#8ebae6", "#8ebae6", "#29a564"]

def setup():
    background("#788089")
    global mover_1, mover_2
    size(900, 640)
    mover_1 = MoverPallete2(random(width), height, PVector(2, 5))
    mover_2 = MoverPallete4(random(width), 0, PVector(5, 2))
    frameRate(1000)
    stroke("#040609")
    strokeWeight(0.4)

def draw():
    mover_1.check_limits()
    mover_1.move()
    mover_1.display()
    mover_2.check_limits()
    mover_2.move()
    mover_2.display()

def keyPressed():
    if key == 's':
        saveFrame("s_20-{}.png".format(frameCount))
