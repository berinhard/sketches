from random import choice

WHITE = color(245)  
RED = color(201, 12, 10, 59)
BLACK = color(10, 10, 10, 44)

SPACING = 10
MARGIN = SPACING
DIMENSION = 900
ORDER = (DIMENSION - MARGIN) / SPACING

GRID_RANGE = range(ORDER)
LIVE_POINTS = []
WALKERS = []
VISITED_POINTS = set()

def grid_valid_neighbors(i, j):
    i_incs = [-1, 0, 1]
    j_incs = [-1, 0, 1]
    
    neighs = []
    for i_inc in i_incs:
        for j_inc in j_incs:
            new_i = i + i_inc
            new_j = j + j_inc
            
            conditions = [
                new_i in GRID_RANGE,
                new_j in GRID_RANGE,
                (new_i, new_j) not in LIVE_POINTS,    
            ]
            if all(conditions):
                neighs.append((new_i, new_j))
                
    return neighs

class GridWalker():
    
    def __init__(self, i, j, c):
        self.i = i
        self.j = j
        self.radius = 10
        self.color = c
        LIVE_POINTS.append((self.i, self.j))
        
    @property
    def x(self):
        return self.i * SPACING
    
    @property
    def y(self):
        return self.j * SPACING
        
    def display(self):
        fill(self.color)
        rect(self.x, self.y, self.radius, self.radius)
        
    def walk(self):
        neighs = grid_valid_neighbors(self.i, self.j)
        LIVE_POINTS.remove((self.i, self.j))
        self.i, self.j = choice(neighs)
        LIVE_POINTS.append((self.i, self.j))
        VISITED_POINTS.add((self.i, self.j))
        
    def destroy(self):
        LIVE_POINTS.remove((self.i, self.j))
        
    @classmethod
    def new_random_walker(cls):
        c = RED    
        if random(1) > 0.7:
            c = BLACK
        return cls(choice(GRID_RANGE), choice(GRID_RANGE), c)
                

def setup():
    size(DIMENSION + SPACING, DIMENSION + SPACING)
    background(WHITE)
    noStroke()
    strokeWeight(1)
    for i in range(10):
        WALKERS.append(
            GridWalker.new_random_walker()
        )
    
def draw():
    global VISITED_POINTS, WALKERS
    
    translate(MARGIN, MARGIN)     
    
    for walker in WALKERS:
        walker.walk()
        walker.display()
        
    total_points = len(GRID_RANGE) ** 2
    percent = len(VISITED_POINTS) / float(total_points)
    print(percent) 
    if percent > 0.95:
        #saveFrame("#######.jpg")
        
        WALKERS = []
        for i in range(10):
            WALKERS.append(
                GridWalker.new_random_walker()
            )
        VISITED_POINTS = set()
        background(WHITE)
        

def keyPressed():
    if keyCode == UP:
        WALKERS.append(
            GridWalker.new_random_walker()
        )
    elif keyCode == DOWN and WALKERS:
        walker = WALKERS.pop()
        walker.destroy()
