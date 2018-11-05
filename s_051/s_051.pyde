from random import choice
from save_frames import save_video_frames
WIDTH, HEIGHT = 900, 900

v1 = PVector(WIDTH / 2, 0)
v2 = PVector(v1.x + random(20, 60), v1.y + random(20, 60))

WHITE = color(198)  
RED = color(181, 12, 10)
BLACK = color(17, 17, 17)
GOLDEN = color(218, 145, 32)
COLORS = [
    WHITE,
    RED,
    BLACK,
    GOLDEN,
]
p_color = None

def setup():
    size(WIDTH, HEIGHT)
    frameRate(5)
    stroke(BLACK)
    strokeWeight(2)
    smooth()
    background(RED)
    
def draw():
    global v1, v2, p_color
    
    # define V3
    v3_angle = radians(random(360))
    v3 = PVector.fromAngle(v3_angle)
    v3.normalize()    
    multiplier = map(noise(frameCount / 150.0), 0, 1, 50, 150)
    v3.mult(multiplier)
    x, y = (v1.x + v3.x) % width, (v1.y + v3.y) % height 
    v3 = PVector(x, y)
    
    # paint new triangle choosing with a random color different from the previous triangle color
    valid_colors = [c for c in COLORS if not c == p_color]
    p_color = choice(valid_colors)
    fill(p_color)
    triangle(v1.x, v1.y, v2.x, v2.y, v3.x, v3.y)
    
    # calc
    dv1 = v3.dist(v1)
    dv2 = v3.dist(v2)
    if dv1 >= dv2:
        v1, v2 = v2, v3
    else:
        v2 = v3
        
    #save_video_frames(5, 13 * 60)
    if not frameCount % 1000: 
        background(RED)
