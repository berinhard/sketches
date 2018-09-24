# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice

SIZE = 800
CIRCLE_RADIUS = 25

COLORS = [
    (94, 0, 0),
    (56, 37, 21),
    (162, 57, 0),
]  # THE SHINNING

def setup():
    size(SIZE, SIZE)
    noStroke()
    
def get_noise_distortion(x, y, noise_dict, step=0.013):
    noise_t = (x + y + frameCount) * step
    if noise_t not in noise_dict:
        noise_dict[noise_t] = noise(noise_t)
    return noise_dict[noise_t]

def draw():
    noise_dict = {}
    background(20, 20, 4)
    
    columns = range(0, width + CIRCLE_RADIUS, CIRCLE_RADIUS * 2)
    lines = range(0, height + CIRCLE_RADIUS, CIRCLE_RADIUS)
    
    for i, x in enumerate(columns):
        for j, y in enumerate(lines):
            diff = get_noise_distortion(x, y, noise_dict)
                        
            circle_width = map(diff, 0, 1, CIRCLE_RADIUS, CIRCLE_RADIUS * 3)  
            ellipse_x = x
            
            if j % 2:
                ellipse_x += CIRCLE_RADIUS

            e_color = COLORS[(j - i) % 3]         
            fill(*e_color)                                 
            ellipse(ellipse_x, y, circle_width, circle_width)
