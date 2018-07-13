class Mover():    
    
    def __init__(self):
        self.location = PVector(random(width), random(height))
        self.velocity = PVector(0, 0)
        self.is_following = False
        self.top_speed = 5
                
    def update(self, to_follow=None):
        if to_follow:
            acceleration = PVector.sub(to_follow.location, self.location)
            self.is_following = True
            acceleration.add(PVector.random2D().mult(6))
            acceleration.normalize()
            acceleration.mult(0.2)
        else:
            acceleration = PVector.random2D()
            acceleration.mult(0.3)
            self.top_speed = 6.5
        self.velocity.add(acceleration)
        self.velocity.limit(self.top_speed)
        self.location.add(self.velocity)
        
    def display(self):
        if self.is_following:
            strokeWeight(4.6)
            stroke(0,168,42, 100)
        else:
            strokeWeight(6.4)
            stroke(235,71,71, 200)
        x, y = self.location.x, self.location.y
        point(x, y)
        
    def check_edges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = width
            
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height
            
def setup():
    global movers_
    frameRate(50)
    size(900, 780)
    movers_ = [[Mover() for i in range(6)] for j in range(4)]
    
def draw():
    global movers_
    noStroke()
    fill(0, 20)
    rect(0, 0, width, height)
    
    for movers in movers_:
        head = movers[0]
        head.update()
        head.check_edges()
        head.display()
        
        for i, mover in enumerate(movers[1:]): 
            mover.update(to_follow=movers[0])
            mover.check_edges()
            mover.display()
