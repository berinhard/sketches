from string import ascii_uppercase
from random import shuffle, choice

BLACK = color(17, 17, 17)
BLACK_CLEAN = color(17, 17, 17, 220)
RED_CLEAN = color(217, 17, 42, 220)
dist_cache = {}

class ConnectablePoint():
    
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.num_neighbors = 5
        self.linked_neighbors = []
        self.live_links = 0

    def display_links(self, randomizer):
        x, y = self.pos.x, self.pos.y

        if random(1) < randomizer.reb_prob(y):
            stroke(RED_CLEAN)
            fill(RED_CLEAN)
        else:
            stroke(BLACK_CLEAN)
            fill(BLACK_CLEAN)
        strokeWeight(1)
        beginShape()
        vertex(x, y)
        for p in self.linked_neighbors:
            vertex(p.pos.x, p.pos.y)
        endShape()
            
    def display_points(self):
        x, y = self.pos.x, self.pos.y
        stroke(BLACK)
        fill(BLACK)
        ellipse(x, y, 2, 2)
            
    @property
    def can_be_connected(self):
        return self.live_links < self.num_neighbors
            
    def link_to_neighbor(self, neighbor):
        if self.can_be_connected and neighbor.can_be_connected:
            self.linked_neighbors.append(neighbor)
            self.live_links += 1
            neighbor.live_links += 1
        
    def link_neighbors(self, all_points):
        min_d = 18

        close_to_point = []
        for p in all_points:
            x, y = p.pos.x, p.pos.y
            x_in_range = self.pos.x - min_d < x < self.pos.x + min_d
            y_in_range = self.pos.y - min_d < y < self.pos.y + min_d 
            if x_in_range and y_in_range:
                close_to_point.append(p)

        shuffle(close_to_point)
        for p in close_to_point:
            key_1, key_2 = [
                (self.pos.x, self.pos.y, p.pos.x, p.pos.y),
                (p.pos.x, p.pos.y, self.pos.x, self.pos.y),
            ]        
            
            if key_1 in dist_cache:
                continue
            elif key_2 in dist_cache:
                continue

            distance = p.pos.dist(self.pos)
            dist_cache[key_1] = distance
            dist_cache[key_2] = distance

            if distance < min_d:
                self.link_to_neighbor(p)
                
            if not self.can_be_connected:
                break         
