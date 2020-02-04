class Particle(object):
    
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.velocity = PVector(0, 0)
        
    def move_to(self, reference):
        dir = PVector.sub(reference, self.pos)
        dir.normalize()
        dir.mult(0.5)
        acceleration = dir
        self.velocity.add(acceleration)
        self.velocity.limit(1)
        self.pos.add(self.velocity)

    def display(self):
        ellipse(self.pos.x, self.pos.y, 10, 10)
        
particles = []
NUM_PARTICLES = 30


def setup():
    size(900, 900)
    for i in range(NUM_PARTICLES):
        particles.append(Particle())
    

def draw():
    reference = PVector(mouseX, mouseY)
    for p in particles:
        p.move_to(reference)
        p.display()
    
