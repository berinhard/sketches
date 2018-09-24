# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from collections import defaultdict

live_points = []
skip_index_percentage = {
    1: [random(1) for i in range(500)],
    2: [random(1) for i in range(500)],
    4: [random(1) for i in range(500)],
}

def setup():
    size(700, 700)
    noCursor()
    
def draw():
    global live_points
    
    stroke(0)
    background(255)
        
    lines_by_stroke = defaultdict(list)
    points = []
    lines = []
    
    for x in range(-100, 710, 10):
        x += frameCount % 710
        if x > 700:
            x -= 800
            
        x1, y1 = x, 0
        x2, y2 = x + 20, height / 3
        points.append((x1, y1))
        points.append((x2, y2))
        lines_by_stroke[1].append((x1, y1, x2, y2))
        
    for x in range(-30, 745, 30):
        x -= frameCount % 40
        if x < -45:
            x = 745        
        
        x1, y1 = x, height / 3
        x2, y2 = x + 40, 2 * height / 3
        points.append((x1, y1))
        points.append((x2, y2))
        lines_by_stroke[4].append((x1, y1, x2, y2))
            
    for x in range(0, 730, 30):
        x += frameCount % 730
        if x > 700:
            x -= 755 
        x1, y1 = x + 35, 2 * height / 3
        x2, y2 = x, height
        points.append((x1, y1))
        points.append((x2, y2))
        lines_by_stroke[2].append((x1, y1, x2, y2))

        
    from random import choice
    print(frameCount)
    if frameCount % 150 == 1:
        live_points = []
        for i in range(42):
            x1, y1 = choice(points)
            x2, y2 = choice(points)
            while y1 == y2:
                x1, y1 = choice(points)
                x2, y2 = choice(points)     
            live_points.append((x1, y1, x2, y2))
        
    for weight, coords in lines_by_stroke.items():
        stroke(0)
        strokeWeight(weight)
        percents = skip_index_percentage[weight]
        for i, coord in enumerate(coords):
            if weight == 4:
                line(*coord)
            if percents[i] > 0.24 * weight:
                line(*coord)
            
    strokeWeight(2)
    stroke(222, 10, 16, 200)
    for x in live_points:
        line(*x)
        
    line(0, height / 3, width, height / 3)
    line(0, 2 * height / 3, width, 2 * height / 3)
