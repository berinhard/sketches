# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
from random import choice


def setup():
    size(900, 1200)
    background(27)
    strokeWeight(3)

colors = [
    color(255, 255, 0),
    color(0, 255, 255),
    color(255, 0, 255),
]
all_shapes = []
y_values_map = {}
def draw():
    global y_values_map, all_shapes
    
    col_width = width / 5
    x_pos = range(0, width + col_width, col_width)

    y_pos = []

    px = 0
    py = 0
    stop = False
    shape_vertexes = [(0, height)]
    for x in x_pos:
        if x not in y_values_map:
            speed = random(-30, -10)
            y_values_map[x] = [height, speed]
        
        y, speed = y_values_map[x]
        y += speed
    
        if y <= 30:
            stop = True
    
        if x == x_pos[0]:
            py = y

        stroke(27)
        #line(px + 1, py, x - 1, y)
        shape_vertexes.append((x, y))

        y_values_map[x] = [y, speed]
        px, py = x, y
        
    shape_vertexes.append((width, height))
    
    all_shapes.append((shape_vertexes, choice(colors)))
    for shape_vertexes, c in all_shapes[::-1]:
        fill(c)
        beginShape()
        for x, y in shape_vertexes:
            vertex(x, y)
        endShape()
        
    if stop:
        y_values_map = {}
        all_shapes = []
    

def keyPressed():
    if key == 's':
        saveFrame("cover.png")
    elif key == 'n':
        global y_values_map, all_shapes
        loop()
        background(27)
        y_values_map = {}
        all_shapes = []
        redraw()
