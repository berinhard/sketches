# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice

gap = 30
thickness = 3

line_opacity = 140
BLACK = color(13, 0, 0, line_opacity)
WHITE = color(255)
RED = color(230, 13, 22, 240)

def setup():
    #noCursor()
    size(1000, 1000)
    noFill()
    strokeWeight(thickness)
    frameRate(3)
    
    
def get_start_angle(angle, arc_len):
    angle = map(random(1), 0, 1, angle - arc_len, angle + arc_len)
    return angle 
    
    
def draw():
    print(mouseX, mouseY)
    
    stroke(BLACK)
    base_angle = 10
    background(WHITE)
    arc_len = radians(base_angle)
    
    x, y = width / 2, height / 2
    arcs = range(gap, width - gap, gap)
    angles = [radians(a) for a in range(0, 361, base_angle)]
    
    red_arc = choice(arcs)
    
        #fill(210, 13, 42, 100)
    rect_weight = 50 
    strokeWeight(rect_weight)
    stroke(RED)
    rectMode(CENTER)
    #blendMode(ADD)
    rect_width = arcs[-1] * sin(radians(45)) - rect_weight
    rect_height = arcs[-1] * sin(radians(45)) - rect_weight 
    rect(x, y, rect_width, rect_height)
    
    noFill()
    strokeWeight(thickness)
    angle_rate = 360.0 / len(angles)
    for i, angle in enumerate(angles):
        stroke(BLACK)
        for j, arc_r in enumerate(arcs):
            prob = randomGaussian()
            if prob < 0:
                prob *= -1
        
            prob_limit = map(i, angles[0], angles[-1], 1 / 8.0, 1/3.0)
            angle = get_start_angle(angle, arc_len)
            if prob > prob_limit:
                arc(x, y, arc_r, arc_r , angle, angle + arc_len)
            color_random = random(1)
            if color_random > 0.98:
                stroke(color(37,152,98, 240))
            elif color_random > 0.95:
                stroke(RED)
            else:
                stroke(BLACK)            
                
    noLoop()
    
def keyPressed():
    if key == 'n':
        redraw()
        saveFrame("######.png")
