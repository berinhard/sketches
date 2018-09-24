from random import choice

gap = 30
thickness = 3

BLACK = color(0)
WHITE = color(255)
RED = color(255, 0, 0)

def setup():
    size(1000, 1000)
    noFill()
    strokeWeight(thickness)
    frameRate(3)
    
    
def draw():
    stroke(BLACK)
    base_angle = 10
    background(WHITE)
    arc_len = radians(base_angle)
    
    x, y = width / 2, height / 2
    arcs = range(gap, width - gap, gap)
    angles = [radians(a) for a in range(base_angle, 361, base_angle)]
    
    red_arc = choice(arcs)
    
    for angle in angles:
        stroke(BLACK)
        for arc_r in arcs:
            prob = randomGaussian()
            if prob < 0:
                prob *= -1

            if arc_r == red_arc:
                stroke(RED)        
            if prob > 0.3:
                arc(x, y, arc_r * random(1), arc_r * random(1) , angle, angle + arc_len)
                
    noLoop()
    
def keyPressed():
    if key == 'n':
        redraw()
