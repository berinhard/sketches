# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

def setup():
    size(900, 900)
    frameRate(10)
    background(50, 50, 50)
    stroke(50, 50, 50, 40)
    
COLORS = [    
  (209,147,4),
  (216,136,3),
  (221,129,49),
  (229,119,79),
  (204,122,137),
]

from random import choice
    
def draw():    
    p1 = PVector(430, 430)
    p2 = PVector(500, 607)
    p3 = PVector(420, 570)
        
    p_wing = PVector(width * noise(frameCount), height * noise(frameCount + 13 * 0.1))
    wing_dist = p2.dist(p_wing)
    
    LIMIT_C1 = 150
    LIMIT_C2 = 200
    LIMIT_C3 = 370
    LIMIT_C4 = 500
    
    if wing_dist < LIMIT_C1:
        wing_color = COLORS[4]
    elif wing_dist < LIMIT_C2:
        wing_color = COLORS[2]
    elif wing_dist < LIMIT_C3:
        wing_color = choice([COLORS[0], COLORS[4]])
    elif wing_dist < LIMIT_C4:
        wing_color = COLORS[3]
    else:
        wing_color = COLORS[4]
    fill(wing_color[0], wing_color[1], wing_color[2], 200)     
    triangle(p1.x, p1.y, p_wing.x, p_wing.y, p3.x, p3.y)
    
    fill(*COLORS[1])
    triangle(p3.x, p3.y, p2.x, p2.y, 380, 700)  # peak     
    triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
