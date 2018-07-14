# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

import random as py_random

class ContinuousLine():

    def __init__(self, all_points, colors, life_cycle=10):
        p_start = py_random.choice(range(len(all_points)))
        self.points = all_points[p_start:p_start+life_cycle]
        self.num_points = len(self.points)
        self.start_index, self.end_index = 0, 0
        self.colors = colors
        self.rotation = None

    def display(self):
        """
        There's some logic error here, but I liked how is being displayed =]
        """
        next_index = self.end_index + 1
        stroke(*self.colors)
        reached_max = next_index == self.num_points
        if not reached_max:
            for i, current in enumerate(self.points[self.start_index:next_index]):
                previous = self.points[i - 1]
                line(previous[0], previous[1], current[0], current[1])
        else:
            self.start_index += 1
            for i, current in enumerate(self.points[self.start_index:self.start_index + self.end_index]):
                previous = self.points[i - 1]
                line(previous[0], previous[1], current[0], current[1])
