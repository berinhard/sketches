# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches

from random import choice, shuffle
from save_frames import save_video_frames

WHITE = color(235)  
RED = color(181, 32, 10)
BLACK = color(27, 27, 27)
GOLDEN = color(218, 145, 32)
GREEN = color(49, 114, 59)
COLORS = [BLACK] * 60 + [WHITE] * 40

def setup():
    global positions, colors
    size(800, 800)
    strokeWeight(6)
    line_space = 20
    frameRate(25)
    positions = range(-100, width / 2, line_space)
    colors = [choice(COLORS) for p in positions]

    
def draw():
    global positions, colors
    if not (frameCount - 1) % 200:
        colors = [choice(COLORS) for p in positions]
    
    background(RED)            
    for i, x in enumerate(positions):
        noise_scale = 74.0
        n = noise((frameCount + i) / noise_scale)
        #print("Noise: {}".format(n))
        x_offset = map(n, 0, 1, 0, width)
        x += x_offset         
        
        c = colors[i]
        stroke(c)
        y = x
        line(x, 0, 0, y)
        line(width - x, 0, width, y)
        
        line(x, height, 0, height - y)        
        line(width - x, height, width, height - y)
        
    #noLoop()
    #save_video_frames(25, 60 * 13)
