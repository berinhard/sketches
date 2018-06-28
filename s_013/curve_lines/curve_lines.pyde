import random
from coord import Coord
from custom_noise import NoiseWave
from distorted_line import CurveLine, StraightLine           

Y_OFFSET = 40
noise_wave_left, noise_wave_right = NoiseWave(10), NoiseWave(10)

def setup():
    frameRate(50)
    size(1200, 600)
    strokeWeight(5)
    strokeCap(ROUND)
    
    global left_curve_lines, right_straight_lines
    left_curve_lines, right_straight_lines = [], []
    
    for y in range(Y_OFFSET, height - Y_OFFSET, 10):
        line_color = random.choice([                                   
            "#2e2c28",
            "#2d5208",
            "#206169",
            "#2d5208",
            "#206169",
            "#e2e0d0"
        ])
        left_curve_lines.append(StraightLine(
            l_start=Coord(0, y),
            l_end=Coord(width/2, y),
            y_offset=Y_OFFSET,
            color=line_color,
        ))
        right_straight_lines.append(CurveLine(
            l_start=Coord(width/2, y),
            l_end=Coord(width, y),
            y_offset=Y_OFFSET,
            color=line_color
        ))
    
def draw():
    background("#0a0a0a")
    global curve_lines
    
    for curve_line in left_curve_lines:        
        curve_line.display(wave=noise_wave_left)
    for curve_line in right_straight_lines:
        curve_line.display(wave=noise_wave_right)
        
    line(width / 2, 0, width / 2, height)  
        
    inc = 0.05
    noise_wave_left.increment(inc)
    if frameCount <= len(noise_wave_left.noises):
        noise_wave_right.noises[0] = noise_wave_left.noises[-1]
    else:
        noise_wave_right.increment(inc)
        
