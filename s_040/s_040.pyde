# Author - Berin
# Sketches repo: https://github.com/berinhard/sketches/

WHITE = color(230)  
RED = color(221, 12, 10, 30)
BLACK = color(10)


px, py = 0, 0
prx, pry = 0, 0

def setup():
    size(900, 900)
    background(WHITE)    
    strokeWeight(2)

    
def draw():
    global px, py, prx, pry
    
    ry = height * random(1)
    rx = prx + 1 
    if prx and pry:
        #stroke(202, 14, 12, 30)
        stroke(RED)
        line(prx, pry, rx, ry) 
    
    x, y = width * noise(frameCount / 1500.), height * noise(frameCount / 343.)
    x = px + 1    
    if px and py: 
        stroke(BLACK)
        line(px, py, x, y)            
        
    if x > height:
        x = 0
    if rx > height:
        rx = 0
    
    prx, pry = rx, ry
    px, py = x, y
    
    #print(frameCount)
    #saveFrame("######.png")
    #if frameCount > 18000:
    #    noLoop()
    #elif frameCount in [4505, 9010, 13515]:
    #    background(WHITE)
    
