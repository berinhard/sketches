class DistortedLine:
    
    def __init__(self, l_start, l_end):
        self.l_start = l_start
        self.l_end = l_end

class CurveLine(DistortedLine):
    
    def display(self, len_wave, color_attrs):
        stroke(*color_attrs)            
        fill(0, 10, 10, 0)

        x_offset = width / len_wave
        
        beginShape();
        for i, x in enumerate(range(self.l_start[0], self.l_end[0], len_wave)):
            t = float(-1 * frameCount) / 75 + float(i) / 10
            distortion = noise(t) 
            y = self.l_start[1] + map(distortion, 0, 1, -30, 30)
            curveVertex(x, y)
        endShape()    
