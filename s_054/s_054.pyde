num_lines = 10
lines_offset = (400) / num_lines
pys = [50 + lines_offset * i for i in range(num_lines)]

def setup():
    size(1600, 450)
    colorMode(HSB, 100)
    background(0, 0, 7)
    strokeWeight(2)
    
def draw():
    base_color = [0, 100, 100]
    if not frameCount % width:
        #saveFrame("#######.png")
        background(0, 0, 7)    
    
    for i in range(num_lines):
        noise_scale = (i + 1) * 10.0
        n = noise((frameCount + 1) / noise_scale)
        y = 50 + lines_offset * i + map(n, 0, 1, -50, 50)
        c = color(0, 0, 100 / (i / 5.0 + 1))
        stroke(c)
        x = (frameCount - 1) % width
        px = x - 1
        py = pys[i]
        line(px, py, x, y)
        pys[i] = y
        
        
        
