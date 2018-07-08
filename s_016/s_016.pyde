import math
from random import choice

from continuous_line import ContinuousLine


def hilbert(points, x0, y0, xi, xj, yi, yj, n):
    """
    From here: http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
    """
    if not n:
        line_x = x0 + (xi + yi)/2
        line_y = y0 + (xj + yj)/2
        points.append((line_x, line_y)) 
    else:
        n -= 1
        hilbert(points, x0,               y0,               yi/2, yj/2, xi/2, xj/2, n),
        hilbert(points, x0 + xi/2,        y0 + xj/2,        xi/2, xj/2, yi/2, yj/2, n),
        hilbert(points, x0 + xi/2 + yi/2, y0 + xj/2 + yj/2, xi/2, xj/2, yi/2, yj/2, n),
        hilbert(points, x0 + xi/2 + yi,   y0 + xj/2 + yj,  -yi/2,-yj/2,-xi/2,-xj/2, n),
        
COLORS = [
    (237,248,251, 200),
    (129,15,124, 200),
    (179,205,227, 200),
    (136,86,167, 200),
    (140,150,198, 200),
]

def setup():
    size(1200, 1000)
    background(0)
    strokeWeight(5)
    strokeCap(ROUND)
    global points_4, points_5, points_6, live_lines, radis, direction
    frameRate(8)
    direction = 1
    
    points_4, points_5, points_6, live_lines = [], [], [], []    
    hilbert(points_4, 0, 0, width / 2, 0, 0, height / 2, 4)
    hilbert(points_5, 0, 0, width / 2, 0, 0, height / 2, 5)
    hilbert(points_6, 0, 0, width / 2, 0, 0, height / 2, 6)
    
def draw():
    global points_4, points_5, points_6, radis, live_lines, direction
    
    noStroke()
    fill(0, 0, 0, 180)
    rect(0, 0, width, height)
            
    if frameCount % 5:
        points = choice([points_4, points_5, points_6])
        print(len(live_lines))
        if len(live_lines) > 200:
            live_lines = []
            direction *= -1
        colors = choice(COLORS)
        live_lines.append(ContinuousLine(points, colors=colors))    
        
    pushMatrix()
    translate(width / 2, height / 2)
    noStroke()
    for c_line in live_lines:
        c_line.display()
        rotate(frameCount % 365 * 0.01 * direction)            
            
    popMatrix()
