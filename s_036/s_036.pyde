# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# First experimentation with Alexandre B A Villares' grid function
# Source: http://abav.lugaralgum.com/sketch-a-day/
 
# Cool bug found while studying the code

def setup():
    size(1000, 1000)
    noFill()
    rectMode(CENTER)
    
def random_line(s, t, x, y):
    if random(1) > 0.9:
        stroke(210, 210, 210, 200)
    elif random(1) > 0.8:
        stroke(210, 10, 10, 200)
    else:
        stroke(10, 10, 10, 200)
    line(s, t, x, y)
    
def draw():
    background(250) 
    
    grid(0, 0, width / 10, 20, random_line, width  / 3 + mouseX, height / 2 + mouseY)
    
    saveFrame("#####.png")
    print('print')
    noLoop()


def grid(x, y, order, spacing, function, *args):
    """
    Variation of Alexandre B A Villares's grid function - https://abav.lugaralgum.com/sketch-a-day
    """
    with pushMatrix():
        translate(x - order * spacing / 2, y- order * spacing / 2)
        for i in range(order):
            for j in range(order):
                with pushMatrix():
                    translate(spacing/2 + i * spacing, spacing/2 + j * spacing)                    
                    function(0, 0, *args) 
    
def keyPressed():
    if key == " ": 
        redraw()
        
