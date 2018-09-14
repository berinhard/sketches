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
    size(800, 800)
    strokeWeight(5)
    background(30)    
    frameRate(70)
    
YELLOW = (218, 165, 32, 200)
GREEN = (57, 255, 77, 200)
RED = (184, 15, 10, 200)
COLORS = [YELLOW] * 16 + [GREEN] * 12 + [RED] * 8
    
def draw():
    background(30)
    
    for i in range(5):
        stroke(*COLORS[(frameCount + i) % len(COLORS)])
        teta = radians(frameCount + i * 20)
        x1, y1 = equation_1(teta, width / 4, height/4)
        #point(x1, y1)
    
        x2, y2 = equation_2(teta, 3 * width/4, 3 * height/4)
        #point(x2, y2)
    
        line(x1, y1, x2, y2)
        
    #print(frameCount)
    #if frameCount < 720:
    #    saveFrame("img###.jpg")
