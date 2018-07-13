class DistortedLine:
    
    def __init__(self, l_start, l_end, y_offset):
        self.l_start = l_start
        self.l_end = l_end
        self.y_offset = y_offset

class CurveLine(DistortedLine):
    
    def display(self, len_wave, color_attrs, noise_step=0.02):
        stroke(*color_attrs)
            
        x_offset = width / len_wave
        
        fill(0, 10, 10, 200)
        
        beginShape();
        curveVertex(self.l_start[0], self.l_start[1]);
        curveVertex(self.l_start[0], self.l_start[1]);
        current_step = self.l_start[1] + frameCount * noise_step
        for i in range(1, len_wave):
            x = self.l_start[0] + i * x_offset
            value = current_step + float(i) / 50
            y_diff = self.y_offset + map(noise(value), 0, 1, -1 * self.y_offset, self.y_offset) 
            if i % 2:
                y_diff *= -1
            
            y = self.l_start[1] + y_diff 
            curveVertex(x, y);

        curveVertex(self.l_end[0], self.l_end[1])
        curveVertex(self.l_end[0], self.l_end[1])
        endShape()    
