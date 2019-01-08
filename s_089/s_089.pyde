# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

WHITE = color(228)
BLACK = color(27, 27, 27)
RED = color(148, 22, 10)

def setup():
    size(700, 700)
    background(WHITE)
    strokeCap(ROUND)


class TiledLinesDrawer():

    def __init__(self, step, weight, c=None):
        self.x, self.y = 0, 0
        self.step = step
        self.c = c or BLACK
        self.weight = weight

    def draw_lines(self):
        new_y = self.y + self.step

        stroke(self.c)
        strokeWeight(self.weight)
        for x in range(self.x, width, self.step):
            for y in range(self.y, height, self.step):
                self.random_line_at(x, y)

    def random_line_at(self, x, y):
        turn = random(1) > 0.5

        size = self.step
        if turn:
            line(x, y, x + size, y + size)
        else:
            line(x + size, y, x, y + size)

drawer_1 = TiledLinesDrawer(15, 1, BLACK)
drawer_2 = TiledLinesDrawer(45, 3)
drawer_3 = TiledLinesDrawer(90, 6, RED)

def draw():
    global x, y

    drawer_1.draw_lines()
    drawer_2.draw_lines()
    drawer_3.draw_lines()

    #saveFrame("cover.png")
    noLoop()