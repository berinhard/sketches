# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

import random as py_random

class ContinuousLine():

    def __init__(self, all_points, colors, life_time=15):
        p_start = py_random.choice(range(len(all_points)))
        
        points = all_points[p_start:p_start+life_time]
        if random(1) > 0.5: # inverted
            self.points = points[::-1]
        self.points = points
        self.num_points = len(self.points)
        self.start_index, self.end_index = 0, 0
        self.colors = colors

    def display(self):
        """
        There's some logic error here, but I liked how it is being displayed =]
        """
        next_index = self.end_index + 1
        reached_max = next_index == self.num_points

        r, g, b = self.colors
        if not reached_max:
            self.end_index = next_index
        else:
            self.start_index += 1
            
        for i, current in enumerate(self.points[self.start_index:self.end_index][:-1]):
            next = self.points[self.start_index + i + 1]
            stroke(r, g, b, 200)
            line(current[0], current[1], next[0], next[1])


    @property
    def is_dead(self):
        return self.start_index == self.end_index == self.num_points - 1
