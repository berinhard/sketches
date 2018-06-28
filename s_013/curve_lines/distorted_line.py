import random
from coord import Coord

class DistortedLine:
    
    def __init__(self, l_start, l_end, y_offset, color):
        self.l_start = l_start
        self.l_end = l_end
        self.y_offset = y_offset
        self.color = color

class CurveLine(DistortedLine):
    
    def display(self, wave):
        stroke(self.color)
            
        len_wave = len(wave.noises)
        x_offset = width / 2 / len_wave
        
        fill(10, 10, 10, 0)
        
        beginShape();
        curveVertex(self.l_start.x, self.l_start.y);
        curveVertex(self.l_start.x, self.l_start.y);
        for i in range(1, len_wave):
            x = self.l_start.x + i * x_offset
            y_diff = self.y_offset * wave.index_noise(i) 
            if i % 2:
                y_diff *= -1
            
            y = self.l_start.y + y_diff 
            curveVertex(x, y);

        curveVertex(self.l_end.x, self.l_end.y)
        curveVertex(self.l_end.x, self.l_end.y)
        endShape()    
        
class StraightLine(DistortedLine):
        
    def display(self, wave):
        stroke(self.color)
            
        len_wave = len(wave.noises)
        x_offset = width / 2 / len_wave
        
        px, py = self.l_start
        for i in range(1, len_wave):
            x = self.l_start.x + i * x_offset
            y_diff = self.y_offset * wave.index_noise(i) 
            if i % 2:
                y_diff *= -1
            
            y = self.l_start.y + y_diff
            line(px, py, x, y)
            px, py = x, y
        line(px, py, self.l_end.x, self.l_end.y)  
