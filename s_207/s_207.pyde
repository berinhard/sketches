# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from berin.coords import draw_at_center, polar_coordinate
from berin.grids import VirtualGrid
from berin.palettes import get_color_palette
from berin.save_frames import save_video_frames
from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
from berin import easings
from random import choice


block_size = 30
falling_blocks = []
blocks = []
colors = get_color_palette()

class BlocksFrontier(object):

    def __init__(self):
        self.blocks_frontier = {}
        self.blocks = []
        x_range = range(0, width + block_size, block_size)
        for x in x_range:
            self.blocks_frontier[x] = height

    def hit(self, block):
        x, y = int(block.pos.x), int(block.pos.y)
        max_y = self.blocks_frontier[x] - block_size
        return y >= max_y

    def add(self, block):
        x, y = int(block.pos.x), int(block.pos.y)
        self.blocks_frontier[x] = y
        self.blocks.append(block)

    def display(self):
        for block in self.blocks:
            block.display()

    @property
    def is_packed(self):
        return bool([y for y in self.blocks_frontier.values() if y == 0])


class Block(object):

    def __init__(self):
        x_range = range(0, width + block_size, block_size)
        self.pos = PVector(choice(x_range), 0)
        self.speed = PVector(0, 15)
        self.color = choice(colors)

    def move(self):
        self.pos.add(self.speed)

    def display(self):
        strokeWeight(4)
        fill(self.color)
        stroke(27)
        rect(self.pos.x, self.pos.y, block_size, block_size)


def init_blocks():
    global frontier, falling_blocks, colors

    colors = get_color_palette()
    falling_blocks = []
    falling_blocks.append(Block())
    frontier = BlocksFrontier()

def setup():
    #size(600, 600)
    fullScreen()
    init_blocks()
    frameRate(24)

def draw():
    background(27)


    if not frameCount % 5:
        falling_blocks.append(Block())

    hit_frontier = []
    for block in falling_blocks:
        if frontier.hit(block):
            hit_frontier.append(block)
        else:
            block.move()
            block.display()

    for block in hit_frontier:
        falling_blocks.remove(block)
        frontier.add(block)

    if frontier.is_packed:
        init_blocks()
    else:
        frontier.display()

    print(frameRate)
    #save_video_frames(24, 60)