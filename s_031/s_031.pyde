# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

import time
from datetime import datetime
from random import choice, shuffle

def equation_1(teta, x_offset=0, y_offset=0):
    r = 1 - (cos(teta) * sin(teta))
    x = r * cos(teta) * 150
    y = r * sin(teta) * 90
    return x + x_offset, y + y_offset

def equation_2(teta, x_offset=0, y_offset=0):
    r = cos(teta/2)
    x = r * cos(teta) * 50
    y = sin(teta) * 160
    return x + x_offset, y + y_offset

def setup():
    global ITER_POINTS
    
    size(800, 800)
    strokeWeight(5)
    background(0)    
    frameRate(70)
    refresh_colors()
    points_range = range(0, 360)        
    ITER_POINTS = [
        choice(points_range),
        choice(points_range),
        choice(points_range),
        choice(points_range),
        choice(points_range),
    ]
    
WHITE = (200, 200, 200)  
RED = (184, 15, 10)
COLORS = []
ITER_POINTS = []

def refresh_colors():
    global COLORS, LIVE_POINTS 
    
    COLORS = [RED] * choice(range(9, 25)) + [WHITE] * choice(range(5, 12))


def draw_lines_on_curve(points):
    if not frameCount % 200:
        refresh_colors()
        
    for i in points:
        stroke(*COLORS[(frameCount + i) % len(COLORS)])
        teta = radians(frameCount + i * 20)
        x1, y1 = equation_1(teta, width / 4, height/4)
        #point(x1, y1)
    
        x2, y2 = equation_2(teta, 3 * width/4, 3 * height/4)
        #point(x2, y2)
    
        line(x1, y1, x2, y2)


mode = 1    
def draw():
    global ITER_POINTS, mode
    if not frameCount % 50:
        mode = random(1)
    
    if not frameCount % 200:
        points_range = range(0, 360)        
        ITER_POINTS = [   # 5 random pointsc
            choice(points_range),
            choice(points_range),
            choice(points_range),
            choice(points_range),
            choice(points_range),
        ]
    
    background(0)
    if mode < 0.248:
        points_range = range(0, 18)
    else:
        points_range = ITER_POINTS
    draw_lines_on_curve(points_range)
    
    #saveFrame("#####.png")
    #if frameCount >= 7999:
    #    noLoop()
    #print(frameCount)
