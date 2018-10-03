# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice

WHITE = color(200)  
RED = color(161, 4, 0)
BLACK = color(10)

class LinesPositioning():
    
    def __init__(self):
        self.lines = []
        
    def get_intersection(self, p1, p2, new_p1, new_p2):
        """
        p1 --> line start
        p2 --> line end
        new_p1 --> new line start
        new_p2 --> new line end
        """
        
        #uA = ((new_p2.x-new_p1.x) * (p1.y-new_p1.y) - (new_p2.y-new_p1.y) * (p1.x-new_p1.x)) / ((new_p2.y-new_p1.y) * (p2.x-p1.x) - (new_p2.x-new_p1.x) * (p2.y-p1.y))
        #uB = ((p2.x-p1.x) * (p1.y-new_p1.y) - (p2.y-p1.y) * (p1.x-new_p1.x)) / ((new_p2.y-new_p1.y) * (p2.x-p1.x) - (new_p2.x-new_p1.x) * (p2.y-p1.y))
        
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        x3, y3 = new_p1.x, new_p1.y
        x4, y4 = new_p2.x, new_p2.y
        
        try:
            uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
            uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
        except ZeroDivisionError:
            return 
        
        if not(0 <= uA <= 1 and 0 <= uB <= 1):
            return
        
        x = p1.x + uA * (p2.x - p1.x)
        y = p1.y + uA * (p2.y - p1.y)
        
        return PVector(x, y)        
        
    def add_new_line(self, p1, p2):
        """
        p1 --> line start
        p2 --> line end
        """
        
        dists = []
        for points in self.lines:
            xp1, xp2 = points            
            inter = self.get_intersection(xp1, xp2, p1, p2)
            if inter:
                p2 = inter 
        
        self.lines.append((p1, p2))        
        
    def display(self):
        for i, points in enumerate(self.lines):            
            p1, p2 = points
            if dist(p1.x, p1.y, p2.x, p2.y) < 43:
                stroke(RED)
            else:
                stroke(WHITE)
            line(p1.x, p1.y, p2.x, p2.y)
    
    
positions = LinesPositioning()

def setup():
    size(900, 900)
    #fullScreen()
    background(BLACK)
    noFill()
    frameRate(25)
    strokeWeight(3)

def draw():
    background(BLACK)
    p1 = PVector(choice(range(0, width)), choice(range(0, height)))
    p2 = PVector(choice(range(0, width)), choice(range(0, height)))
    
    positions.add_new_line(p1, p2)
    positions.display()
    print(frameCount)
    
    # saveFrame("#####.png")
    
    # if frameCount == 1000:
    #     noLoop()
    # elif not frameCount % 250:
    #     positions.lines = []
    #     redraw()
    
    
    
def keyPressed():
    if key == 'n':
        positions.lines = []
        redraw()
    
