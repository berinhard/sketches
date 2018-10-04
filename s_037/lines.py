# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice

WHITE = color(240)  
RED = color(221, 12, 10)
BLACK = color(10)


class CustomLine():
    
    def __init__(self, p1, p2, l_color=None):
        self.p1, self.p2 = p1, p2
        self.color = l_color
        self.inter_lines = []
        
    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2
    
    def line_size(self):
        return abs(dist(self.p1.x, self.p1.y, self.p2.x, self.p2.y))
        
    def display(self):
        if self.color:
            stroke(self.color)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        
    def get_intersection(self, other_line):        
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = other_line.p1.x, other_line.p1.y
        x4, y4 = other_line.p2.x, other_line.p2.y
        
        try:
            uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
            uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
        except ZeroDivisionError:
            return 
        
        if not(0 <= uA <= 1 and 0 <= uB <= 1):
            return
        
        x = self.p1.x + uA * (self.p2.x - self.p1.x)
        y = self.p1.y + uA * (self.p2.y - self.p1.y)
        
        return PVector(x, y)
    
    def set_color(self):
        p1, p2 = self.p1, self.p2
        
        if len(self.inter_lines) == 0:  # line without intersection
            self.color = RED
        elif len(self.inter_lines) == 1:  # line with single intersection keeps same color
            self.color = self.inter_lines[0].color
        else:
            p1_color = self.inter_lines[0].color
            p2_color = self.inter_lines[0].color 
    
            if p1_color == RED and p2_color == RED:  # intersection between 2 red lines strokes to black
                self.color = BLACK
            elif p1_color == BLACK and p2_color == BLACK:  # intersection between 2 black lines strokes to red
                self.color = RED
            else:
                self.color = choice([RED, BLACK])  # intersection between a red and a black line uses random
            
    def add_line_intersection(self, inter_line):
        if not inter_line:
            return
        self.inter_lines.append(inter_line)        


class LinesPositioning():
    
    def __init__(self, min_x=0, min_y=0, max_width=None, max_height=None, max_lines=100):
        self.lines = []
        self.min_x, self.min_y = min_x, min_y
        self.max_width = max_width or width
        self.max_height = max_height or width
        self.max_lines = max_lines
        
    @property
    def is_full(self):
        return len(self.lines) >= self.max_lines
        
    def add_new_line(self, p1, p2):
        """
        p1 --> line start
        p2 --> line end
        """   
        if self.is_full:
            return
                  
        p1, p2 = sorted([p1, p2], key=lambda p: p.x)
        new_line = CustomLine(p1, p2, RED)

        intersections = []   # compute all intersection points with existing lines            
        for c_line in sorted(self.lines, key=lambda l: l.p1):
            inter = new_line.get_intersection(c_line)
            if inter:
                intersections.append((inter, c_line))

        if not intersections:
            self.lines.append(new_line)
            return new_line

        segments = []            
        previous = p1
        previous_line = None
        for inter, inter_line in sorted(intersections, key=lambda p: p[0].x):  # split line into segments
            inter = PVector(inter.x, inter.y)
            
            segment = CustomLine(previous, inter)
            segment.add_line_intersection(previous_line)
            segment.add_line_intersection(inter_line)
            segments.append(segment)
                        
            previous = inter
            previous_line = inter_line
        else:
            segments.append(CustomLine(previous, p2))  # we can't forget the last point
        
        valid_line = sorted(segments, key=lambda s: s.line_size(), reverse=True)[0]  # keeps the segment with the greatest size                    
        self.lines.append(valid_line)    
        
    def new_random_line_and_display(self, *args, **kwargs):
        x_range = range(self.min_x, self.max_width)
        y_range = range(self.min_y, self.max_height)
        p1 = PVector(choice(x_range), choice(y_range))
        p2 = PVector(choice(x_range), choice(y_range))
    
        self.add_new_line(p1, p2)    
        
        self.display()
        
    def refresh(self, *args, **kwargs):
        if self.is_full and random(1) > 0.99825:
            self.lines = []
        
    def debug_display(self, *args, **kwargs):
        ellipse(self.min_x, self.min_y, 5, 5)
        rect(self.min_x, self.min_y, 5, 5)
        
    def display(self):
        strokeWeight(2)
        for c_line in self.lines:
            if not c_line.color:                            
                c_line.set_color()
            c_line.display()
