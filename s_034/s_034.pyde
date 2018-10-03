# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

bozo = None

WHITE = color(200, 200, 200)  
RED = color(184, 15, 10)
BLACK = color(10)


def setup():
    global bozo
    
    size(768, 512)
    bozo = loadImage("data/bozo.png")
    font = loadFont("Garuda-Bold-48.vlw")
    textFont(font)
    textSize(80)

def draw():   
    background(BLACK) 
    
    for y in range(0, height, 4):
        if random(1) > 0.66:
            continue
        
        
        for x in range(0, width):                
            c = bozo.get(int(x), int(y))
            if c == -58093: 
                stroke(c)
                point(x, y) 
    
    fill(RED)
    text("ELE", 50, 200)
    if random(1) > 0.4:
        fill(WHITE)
    text(u"NÃO", 540, 200)
