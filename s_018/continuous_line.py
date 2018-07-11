import random as py_random

class ContinuousLine():
    
    def __init__(self, all_points, colors, life_cycle=25):
        p_start = py_random.choice(range(len(all_points)))
        self.points = all_points[p_start:p_start+life_cycle]
        self.num_points = len(self.points)
        self.start_index, self.end_index = 0, 0
        self.colors = colors
                
    def display(self):
        """
        There's some logic error here, but I liked how it is being displayed =]
        """               
        next_index = self.end_index + 1
        reached_max = next_index == self.num_points
        
        stroke(self.colors)
        if not reached_max:
            for i, current in enumerate(self.points[self.start_index:next_index]):
                previous = self.points[i - 1]  # links last point with first 
                line(previous[0], previous[1], current[0], current[1])
                self.end_index = next_index
        else:
            self.start_index += 1
            for i, current in enumerate(self.points[self.start_index:self.start_index + self.end_index]):
                previous = self.points[i - 1]
                line(previous[0], previous[1], current[0], current[1]) 
                
    @property
    def is_dead(self):
        return self.start_index == self.end_index == self.num_points - 1 
