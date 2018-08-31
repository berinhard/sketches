def setup():
    global y
    size(800, 800)
    y = 0
    background(130)
    
def draw():
    global y
        
    if 0 <= y <= height / 2:
        y = (0 + frameCount % height) - height / 2
    else:
        y = (height - frameCount % height) - height / 2
    
    stroke(86,13,13)    
    pushMatrix()
    translate(height / 2, width / 2)
    fill(92,16,16, 10)
    rotate(radians(frameCount))
    triangle(10, height/2, width / 2, y, width - 10, height / 2)
    triangle(10, height/2, width / 2, height - y, width - 10, height / 2)
    popMatrix()

    red_rate = frameCount % 1000
    fill(map(red_rate, 0, 1000, 30, 220), 16, 16, 10)
    y2 = map(y, 0, height / 2, 0, 50)
    triangle(width / 2 - 40, height/2, width / 2, height/2 - y2, width / 2 + 40, height / 2)
    triangle(width / 2 - 40, height/2, width / 2, height/2 + y2, width / 2 + 40, height / 2)
