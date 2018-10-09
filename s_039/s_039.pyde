# Author - Berin
# Sketches repo: https://github.com/berinhard/sketches/

def setup():
    size(1100, 1100)
    noStroke()
    frameRate(20)
    

noise_factors_per_range = {
    0: {'x': 10.0, 'y': 50.0, 'z': 10.0},
    1: {'x': 50.0, 'y': 10.0, 'z': 10.0},
    2: {'x': 10.0, 'y': 10.0, 'z': 10.0},
    3: {'x': 10.0, 'y': 10.0, 'z': 50.0},
    4: {'x': 50.0, 'y': 25.0, 'z': 10.0},    
        
    5: {'x': 100.0, 'y': 100.0, 'z': 30.0},
    
    6: {'x': 25.0, 'y': 50.0, 'z': 10.0},
    7: {'x': 10.0, 'y': 10.0, 'z': 100.0},  
    8: {'x': 10.0, 'y': 10.0, 'z': 10.0},
    9: {'x': 100.0, 'y': 10.0, 'z': 10.0},
    10: {'x': 10.0, 'y': 100.0, 'z': 10.0},                                     
}
    
    
def draw():
    background(0)
    step = 10
    for x in range(0, width, step):
        scale_index = x / 100
        #if 3 < scale_index < 7:
        #    scale_index = 0
        noise_scale = noise_factors_per_range[scale_index]
        for y in range(0, height, step):
            
            n = noise(
                x / noise_scale['x'], 
                y / noise_scale['y'],
                frameCount / noise_scale['z']
            )
            c = 210 * n
            fill(c, 14, 13, 200)
            r_size = step# - step * n
            rect(x, y, r_size, r_size)
            
        fill(255)
        text(scale_index, x, 10)
                
    #saveFrame("#####.png")
    #print(frameCount)
    #if frameCount == 4800:
    #    noLoop()
              
