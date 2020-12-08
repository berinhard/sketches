#!/usr/bin/env python
# Sketch used to generate videos for 
# Author: berin & vin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
#from berin.coords import draw_at_center, polar_coordinate
#from berin.grids import VirtualGrid
#from berin.palettes import get_color_palette
#from berin.save_frames import save_video_frames
#from berin.shapes import regular_polygon, draw_shape, lines_intersection, IntersectionLine
#from berin import easings

import itertools
from random import choice

WIDTH, HEIGHT = 1080, 1920
RES = 1

WHITE_IMG_PATH = "imgs/clean-algobr-white.png"
BLACK_IMG_PATH = "imgs/clean-algobr.png"
BLACK = color(0)
WHITE = color(255)

OUTPUT_DIR = "insta_black/"
BACKGROUND = BLACK
IMG_PATH = BLACK_IMG_PATH
#BACKGROUND = WHITE
#IMG_PATH = WHITE_IMG_PATH

IMG = None
img_size = 900
cell_size = img_size / 10 * 2
    
fps = 24
angle = 0
angle_rate = 0.1
angle_inc = TWO_PI / 24 * 0.1

def setup():
    global IMG
    size(WIDTH / RES, HEIGHT / RES)
    imageMode(CENTER)
    IMG = loadImage(IMG_PATH)
    IMG.resize(cell_size, cell_size)
    
class Logo:
    
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.angle = 0
        self.orientation = choice([-1, 1])
        
    @property
    def angle_inc(self):
        step = random(1)
        n = noise(self.x, self.y, frameCount * 0.01)
        step = n#map(n, 0, 1, )
        step = map(n, 0, 1, -1, 1)
        return angle_inc * step * self.orientation
        
    def update(self):
        self.angle += self.angle_inc

    def draw(self):
        with pushMatrix():
            translate(self.x, self.y - 5)
            rotate(self.angle)
            image(IMG, 0, 0)


logos = []

def draw():
    global angle
    
    if not logos:
        x_range = range(cell_size / 2, width, cell_size)
        y_range = range(cell_size / 2, height, cell_size)
        logos.extend([Logo(x, y) for x, y in itertools.product(x_range, y_range)])
    
    x_range = range(cell_size / 2, width, cell_size)
    y_range = range(cell_size / 2, height, cell_size)
        
    background(BACKGROUND)
    for logo in logos:
        logo.draw()
        logo.update()
        
    if frameCount < 7200:
        saveFrame(OUTPUT_DIR + "######.png")
        print("faltam: ", 7200 - frameCount)


def keyPressed():
    if key == 's':
        saveFrame("results/######.png")
