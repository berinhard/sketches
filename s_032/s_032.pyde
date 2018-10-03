# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice

WHITE = color(200, 200, 200)  
RED = color(184, 15, 10)
BLACK = color(10)

COLORS = [RED] * 16 + [WHITE] * 10


def setup():
    size(900, 900)
    background(BLACK)
    noFill()
    
    
def sin_line_points(x_iter, y_offset=200, x_offset=20, angle_inc=PI/56.0, scale_val=60.0, start_angle=0):
    points = []
    angle = radians(start_angle)
    for x in x_iter:
        y = y_offset + sin(angle) * scale_val
        angle += angle_inc
        points.append((x + x_offset, y))
    return points
    
    
def draw():
    with pushMatrix():
        translate(width, 0)
        rotate(HALF_PI)
        angle = 0
        x_iter = range(0, width - 40, 2)
        points = []
        
        points.extend(sin_line_points(x_iter))
        points.extend(sin_line_points(x_iter, start_angle=123))
        points.extend(sin_line_points(x_iter, start_angle=36, scale_val=130.0, angle_inc = PI/32.0))
        points.extend(sin_line_points(x_iter, start_angle=54, scale_val=180.0, angle_inc = PI/18.0))
    
        if not frameCount % 140:
            fill(BLACK)
            noStroke()
            rect(0, 0, width, height / 2)
            noFill()
            strokeCap(ROUND)
            
            strokeWeight(1)
            stroke(200, 200, 200, 80)
            for x, y in points:
                point(x, y)
                
            stroke(choice(COLORS))
            strokeWeight(3) 
            beginShape()
            x1, y1 = choice(points)
            curveVertex(x1, y1)
            for i in range(8):
                x1, y1 = choice(points)
                curveVertex(x1, y1)
            endShape(CLOSE)
            
        pushMatrix()
        translate(0, height / 2)
        
        if not frameCount % 100:
            fill(BLACK)
            noStroke()
            rect(0, 0, width, height / 2)
            noFill()
            strokeCap(ROUND)
            
            strokeWeight(1)
            stroke(200, 200, 200, 80)
            for x, y in points:
                point(x, y)
                    
            stroke(choice(COLORS))
            strokeWeight(3)
            beginShape(TRIANGLE_STRIP)
            x1, y1 = choice(points)
            vertex(x1, y1)
            for i in range(8):
                x1, y1 = choice(points)
                vertex(x1, y1)
            endShape(CLOSE)
            
        popMatrix()            
