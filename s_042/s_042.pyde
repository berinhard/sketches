from random import choice


WHITE = color(245)  
RED = color(201, 12, 10, 109)
BLACK = color(17, 17, 17, 94)

WIDTH, HEIGHT = 900, 900
SCALE = 20
COLS = floor(WIDTH / SCALE)
ROWS = floor(HEIGHT / SCALE)

x_off = 0
y_off = 1042 


class Particle():
    
    def __init__(self):
        self.pos = PVector(random(WIDTH), random(HEIGHT))
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.max_speed = 1
        self.color = choice([BLACK, RED])        
    
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.max_speed)
        self.pos.add(self.vel)
        self.acc.mult(0)
        self.edges()
        
    def apply_force(self, force):
        self.acc.add(force)
        
    def display(self):
        strokeWeight(1)
        fill(self.color)
        ellipse(self.pos.x, self.pos.y, 2, 2)
        
    def edges(self):
        self.pos.x = self.pos.x % width
        self.pos.y = self.pos.y % width 
        
    def follow(self, vectors):
        x, y = floor(self.pos.x / SCALE), floor(self.pos.y / SCALE)
        index = x + y * COLS
        force = vectors[index]
        self.apply_force(force)

particles = [Particle() for x in range(120)]

def setup():
    size(WIDTH, HEIGHT)
    #frameRate(5)
    background(WHITE)
    strokeCap(ROUND)
    noStroke()
    
    
def draw():
    #background(255)
    z_off = frameCount / 100.0
    
    flow_field = [None for i in range(COLS * ROWS)]
    for i in range(COLS):
        x_off = i * 0.01  
        for j in range(ROWS):
            index = i + j * ROWS
            y_off = (1042 + j) * 0.01
            x, y = i * SCALE, j * SCALE
            
            angle = noise(x_off, y_off, z_off) * TWO_PI
            vector = PVector.fromAngle(angle)
            vector.setMag(0.01)
            flow_field[index] = vector            
            
    for particle in particles:
        particle.follow(flow_field)
        particle.update()
        if frameCount > 50:
            particle.display()
    
    #if frameCount == 25003:
    #    saveFrame("######png")
    #    noLoop() 
    #print(frameCount)
    #noLoop()
    
    
def keyPressed():
    if key == 's':
        saveFrame("#################.png")
